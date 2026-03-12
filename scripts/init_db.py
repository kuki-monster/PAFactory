
from pathlib import Path
import argparse
import sqlite3

def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize the SQLite database.")
    parser.add_argument("--db", required=True, help="Path to SQLite database file.")
    parser.add_argument("--schema", required=True, help="Path to schema.sql file.")
    args = parser.parse_args()

    db_path = Path(args.db)
    schema_path = Path(args.schema)

    db_path.parent.mkdir(parents=True, exist_ok=True)

    schema_sql = schema_path.read_text(encoding="utf-8")
    conn = sqlite3.connect(str(db_path))
    try:
        conn.executescript(schema_sql)
        conn.commit()
        print(f"Database initialized: {db_path}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
