
from __future__ import annotations

import argparse
import json
from pathlib import Path
import yaml
import fitz  # PyMuPDF

from _common import now_iso, sha256_file, connect_db, slugify

def load_source_config(config_path: Path, file_name: str) -> dict:
    data = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    for item in data.get("sources", []):
        if item.get("file_name") == file_name:
            return item
    return {
        "source_id": slugify(Path(file_name).stem),
        "priority": 999,
        "role": "unclassified",
        "family": "unclassified",
    }

def main() -> None:
    parser = argparse.ArgumentParser(description="Register a PDF source in the SQLite database.")
    parser.add_argument("--pdf", required=True, help="Path to the PDF file.")
    parser.add_argument("--db", required=True, help="Path to SQLite database.")
    parser.add_argument("--config", required=True, help="Path to config/sources.yaml.")
    args = parser.parse_args()

    pdf_path = Path(args.pdf).resolve()
    db_path = Path(args.db).resolve()
    config_path = Path(args.config).resolve()

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    conf = load_source_config(config_path, pdf_path.name)
    file_hash = sha256_file(pdf_path)

    with fitz.open(str(pdf_path)) as doc:
        meta = doc.metadata or {}
        page_count = doc.page_count

    title = meta.get("title") or pdf_path.stem
    author = meta.get("author") or ""
    source_id = conf["source_id"]
    year = None

    conn = connect_db(db_path)
    try:
        existing = conn.execute("SELECT source_id, file_hash FROM sources WHERE source_id = ?", (source_id,)).fetchone()
        if existing and existing["file_hash"] == file_hash:
            print(f"Source already registered with same hash: {source_id}")
            return

        conn.execute(
            """
            INSERT OR REPLACE INTO sources
            (source_id, file_name, file_hash, file_path, title, author, year, priority, role, family, page_count, text_quality, processed_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                source_id,
                pdf_path.name,
                file_hash,
                str(pdf_path),
                title,
                author,
                year,
                conf.get("priority"),
                conf.get("role"),
                conf.get("family"),
                page_count,
                "unknown",
                now_iso(),
            ),
        )
        run_id = f"run_{source_id}_{file_hash[:8]}"
        conn.execute(
            """
            INSERT OR REPLACE INTO runs
            (run_id, started_at, ended_at, status, source_id, file_hash, message)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (run_id, now_iso(), now_iso(), "registered", source_id, file_hash, "Source registered"),
        )
        conn.commit()
        print(json.dumps({"source_id": source_id, "page_count": page_count, "run_id": run_id}, indent=2))
    finally:
        conn.close()

if __name__ == "__main__":
    main()
