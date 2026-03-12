
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

def run_step(cmd: list[str]) -> None:
    print("RUN >", " ".join(cmd))
    result = subprocess.run(cmd, check=False)
    if result.returncode != 0:
        raise SystemExit(result.returncode)

def main() -> None:
    parser = argparse.ArgumentParser(description="Run the basic phase-1 pipeline on a single PDF.")
    parser.add_argument("--pdf", required=True, help="Path to PDF.")
    parser.add_argument("--root", required=True, help="Project root path.")
    parser.add_argument("--source-id", required=False, help="Optional explicit source ID.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    pdf = Path(args.pdf).resolve()
    db = root / "db" / "expert_factory.db"
    sources = root / "config" / "sources.yaml"
    pages_out = root / "extracted" / "pages"

    register_cmd = [sys.executable, str(root / "scripts" / "register_source.py"), "--pdf", str(pdf), "--db", str(db), "--config", str(sources)]
    run_step(register_cmd)

    source_id = args.source_id or pdf.stem.lower().replace(" ", "_")
    extract_cmd = [sys.executable, str(root / "scripts" / "extract_pdf.py"), "--pdf", str(pdf), "--out", str(pages_out), "--db", str(db), "--source-id", source_id]
    run_step(extract_cmd)

    pages_json = pages_out / f"{source_id}.pages.json"
    segment_cmd = [sys.executable, str(root / "scripts" / "segment_source.py"), "--pages", str(pages_json), "--out-dir", str(root / "extracted"), "--db", str(db), "--source-id", source_id]
    run_step(segment_cmd)

    print("Pipeline finished.")

if __name__ == "__main__":
    main()
