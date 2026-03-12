
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from _common import connect_db, write_json

HEADING_RE = re.compile(r"^(chapter\s+\d+|part\s+[ivx]+|[A-Z][A-Z0-9 ,\-:]{8,})$", re.IGNORECASE)

def detect_content_kind(text: str) -> str:
    lower = text.lower()
    if "list of terms used in this book" in lower:
        return "glossary"
    if "contents" in lower or "table of contents" in lower:
        return "contents"
    if "index" in lower and len(text) < 4000:
        return "index"
    return "chapter_body"

def detect_heading(text: str) -> str | None:
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    for line in lines[:8]:
        if HEADING_RE.match(line):
            return line
    return None

def make_chunks(pages: list[dict], target_words: int = 1000) -> list[dict]:
    chunks = []
    current = []
    current_words = 0
    chunk_start = None
    last_kind = None

    for page in pages:
        text = page["text"]
        words = len(text.split())
        kind = detect_content_kind(text)
        if chunk_start is None:
            chunk_start = page["page_number"]
            last_kind = kind

        if current and (current_words + words > target_words and kind == last_kind):
            chunk_text = "\n\n".join(p["text"] for p in current)
            chunks.append({
                "page_start": chunk_start,
                "page_end": current[-1]["page_number"],
                "content_kind": last_kind,
                "text": chunk_text,
                "word_count": len(chunk_text.split()),
            })
            current = []
            current_words = 0
            chunk_start = page["page_number"]
            last_kind = kind

        current.append(page)
        current_words += words

    if current:
        chunk_text = "\n\n".join(p["text"] for p in current)
        chunks.append({
            "page_start": chunk_start,
            "page_end": current[-1]["page_number"],
            "content_kind": last_kind,
            "text": chunk_text,
            "word_count": len(chunk_text.split()),
        })

    return chunks

def main() -> None:
    parser = argparse.ArgumentParser(description="Segment extracted pages into sections and chunks.")
    parser.add_argument("--pages", required=True, help="Path to *.pages.json file.")
    parser.add_argument("--out-dir", required=True, help="Base output directory.")
    parser.add_argument("--db", required=True, help="Path to SQLite database.")
    parser.add_argument("--source-id", required=True, help="Source ID.")
    args = parser.parse_args()

    pages_path = Path(args.pages).resolve()
    out_dir = Path(args.out_dir).resolve()
    db_path = Path(args.db).resolve()
    source_id = args.source_id

    pages = json.loads(pages_path.read_text(encoding="utf-8"))
    sections = []
    for page in pages:
        heading = detect_heading(page["text"])
        sections.append({
            "source_id": source_id,
            "page_number": page["page_number"],
            "heading_guess": heading,
            "content_kind": detect_content_kind(page["text"]),
            "quality_flag": page["quality_flag"],
        })

    chunks = make_chunks(pages)

    write_json(out_dir / "sections" / f"{source_id}.sections.json", sections)
    write_json(out_dir / "chunks" / f"{source_id}.chunks.json", chunks)

    conn = connect_db(db_path)
    conn.execute(
        "UPDATE runs SET sections_extracted = ?, chunks_created = ?, status = ? WHERE source_id = ?",
        (len(sections), len(chunks), "segmented", source_id),
    )
    conn.commit()
    conn.close()

    print(f"Sections: {len(sections)} | Chunks: {len(chunks)}")

if __name__ == "__main__":
    main()
