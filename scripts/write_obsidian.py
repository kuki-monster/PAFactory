
from __future__ import annotations

import argparse
import json
from pathlib import Path
from jinja2 import Template

def main() -> None:
    parser = argparse.ArgumentParser(description="Render one object JSON into an Obsidian Markdown note.")
    parser.add_argument("--object-json", required=True, help="Path to object JSON.")
    parser.add_argument("--template", required=True, help="Path to Jinja2 Markdown template.")
    parser.add_argument("--out", required=True, help="Path to output Markdown note.")
    args = parser.parse_args()

    object_path = Path(args.object_json)
    template_path = Path(args.template)
    out_path = Path(args.out)

    data = json.loads(object_path.read_text(encoding="utf-8"))
    template = Template(template_path.read_text(encoding="utf-8"))
    rendered = template.render(**data)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(rendered, encoding="utf-8")
    print(f"Wrote note: {out_path}")

if __name__ == "__main__":
    main()
