
from __future__ import annotations

import argparse
from pathlib import Path
import fitz  # PyMuPDF

from _common import connect_db, write_json

def clean_text(text: str) -> str:
    return text.replace("\x00", "").strip()

def quality_flag(text: str) -> str:
    if len(text.strip()) < 80:
        return "low_text"
    if "�" in text:
        return "encoding_noise"
    return "clean_text"

def main() -> None:
    parser = argparse.ArgumentParser(description="Extract text from each page of a PDF.")
    parser.add_argument("--pdf", required=True, help="Path to PDF.")
    parser.add_argument("--out", required=True, help="Output directory for page JSON.")
    parser.add_argument("--db", required=True, help="Path to SQLite database.")
    parser.add_argument("--source-id", required=True, help="Source ID.")
    args = parser.parse_args()

    pdf_path = Path(args.pdf).resolve()
    out_dir = Path(args.out).resolve()
    db_path = Path(args.db).resolve()
    source_id = args.source_id

    pages = []
    conn = connect_db(db_path)

    with fitz.open(str(pdf_path)) as doc:
        for idx, page in enumerate(doc, start=1):
            text = clean_text(page.get_text("text"))
            flag = quality_flag(text)
            page_obj = {
                "source_id": source_id,
                "page_number": idx,
                "text": text,
                "quality_flag": flag,
            }
            pages.append(page_obj)
            conn.execute(
                """
                INSERT OR REPLACE INTO source_passages
                (passage_id, source_id, page_start, page_end, chapter, section, text, quality_flag, char_count)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    f"{source_id}_p{idx:04d}",
                    source_id,
                    idx,
                    idx,
                    None,
                    None,
                    text,
                    flag,
                    len(text),
                ),
            )

    out_file = out_dir / f"{source_id}.pages.json"
    write_json(out_file, pages)

    conn.execute(
        "UPDATE sources SET text_quality = ? WHERE source_id = ?",
        ("mixed" if any(p["quality_flag"] != "clean_text" for p in pages) else "clean", source_id),
    )
    conn.commit()
    conn.close()

    print(f"Wrote {len(pages)} pages to {out_file}")

if __name__ == "__main__":
    main()
