
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS sources (
    source_id TEXT PRIMARY KEY,
    file_name TEXT NOT NULL,
    file_hash TEXT NOT NULL,
    file_path TEXT,
    title TEXT,
    author TEXT,
    year INTEGER,
    priority INTEGER,
    role TEXT,
    family TEXT,
    page_count INTEGER,
    text_quality TEXT,
    processed_at TEXT
);

CREATE TABLE IF NOT EXISTS runs (
    run_id TEXT PRIMARY KEY,
    started_at TEXT NOT NULL,
    ended_at TEXT,
    status TEXT NOT NULL,
    source_id TEXT,
    file_hash TEXT,
    pages_extracted INTEGER DEFAULT 0,
    sections_extracted INTEGER DEFAULT 0,
    chunks_created INTEGER DEFAULT 0,
    candidates_created INTEGER DEFAULT 0,
    review_items_created INTEGER DEFAULT 0,
    approved_objects_created INTEGER DEFAULT 0,
    notes_written INTEGER DEFAULT 0,
    message TEXT,
    FOREIGN KEY (source_id) REFERENCES sources(source_id)
);

CREATE TABLE IF NOT EXISTS source_passages (
    passage_id TEXT PRIMARY KEY,
    source_id TEXT NOT NULL,
    page_start INTEGER,
    page_end INTEGER,
    chapter TEXT,
    section TEXT,
    text TEXT,
    quality_flag TEXT,
    char_count INTEGER,
    FOREIGN KEY (source_id) REFERENCES sources(source_id)
);

CREATE TABLE IF NOT EXISTS objects (
    object_id TEXT PRIMARY KEY,
    object_type TEXT NOT NULL,
    canonical_name TEXT,
    status TEXT NOT NULL,
    domain_family TEXT,
    canonical_owner_book TEXT,
    short_definition TEXT,
    content_json TEXT,
    extraction_confidence REAL,
    merge_confidence REAL,
    doctrinal_confidence REAL,
    created_run_id TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS relationships (
    relationship_id TEXT PRIMARY KEY,
    from_object_id TEXT NOT NULL,
    relationship_type TEXT NOT NULL,
    to_object_id TEXT NOT NULL,
    FOREIGN KEY (from_object_id) REFERENCES objects(object_id),
    FOREIGN KEY (to_object_id) REFERENCES objects(object_id)
);

CREATE TABLE IF NOT EXISTS object_sources (
    object_id TEXT NOT NULL,
    passage_id TEXT NOT NULL,
    support_type TEXT,
    PRIMARY KEY (object_id, passage_id),
    FOREIGN KEY (object_id) REFERENCES objects(object_id),
    FOREIGN KEY (passage_id) REFERENCES source_passages(passage_id)
);

CREATE TABLE IF NOT EXISTS review_queue (
    review_id TEXT PRIMARY KEY,
    object_id TEXT,
    issue_type TEXT NOT NULL,
    reason TEXT NOT NULL,
    priority TEXT NOT NULL,
    status TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY (object_id) REFERENCES objects(object_id)
);
