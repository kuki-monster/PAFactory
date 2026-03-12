
from __future__ import annotations

import argparse
import time
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import subprocess
import sys

class PdfHandler(FileSystemEventHandler):
    def __init__(self, root: Path):
        self.root = root

    def on_created(self, event):
        if event.is_directory:
            return
        path = Path(event.src_path)
        if path.suffix.lower() != ".pdf":
            return
        time.sleep(2)
        cmd = [
            sys.executable,
            str(self.root / "scripts" / "run_pipeline.py"),
            "--pdf", str(path),
            "--root", str(self.root),
        ]
        subprocess.run(cmd, check=False)

def main() -> None:
    parser = argparse.ArgumentParser(description="Watch the inbox folder and run the phase-1 pipeline on new PDFs.")
    parser.add_argument("--root", required=True, help="Project root.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    inbox = root / "inbox"
    inbox.mkdir(parents=True, exist_ok=True)

    observer = Observer()
    observer.schedule(PdfHandler(root), str(inbox), recursive=False)
    observer.start()
    print(f"Watching: {inbox}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
