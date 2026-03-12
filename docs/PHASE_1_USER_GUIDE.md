
# Price Action Expert Factory — Phase 1 User Guide

## Purpose

This guide walks you through every manual step needed to implement Phase 1 of the Windows-based creation stack.

Phase 1 goal:
- set up the local project
- install the tools
- initialize the database
- process the first foundation PDF
- inspect the outputs
- verify that the pipeline is working before you scale up

This guide is written for a beginner. It assumes Windows 11, PowerShell, Python, VS Code, and Obsidian.

## What Phase 1 includes

You are setting up the creation stack for:
- source registration
- page-level PDF text extraction
- section and chunk creation
- a local SQLite database
- starter Obsidian note templates
- a watched-folder path for later automation

Phase 1 does not yet include:
- high-quality concept extraction
- Mem0 sync
- OpenClaw integration
- full conflict-resolution automation
- polished note writing into the live expert vault

Those come later. This phase is the foundation.

## Deliverables created by this phase

After Phase 1 is working, you should have:
- a project root folder
- a Python virtual environment
- installed Python packages
- a SQLite database file
- extracted page JSON for one PDF
- section JSON for one PDF
- chunk JSON for one PDF
- logs that show what ran

## Project root used in this guide

This guide uses the following example path:

D:\PriceActionExpertFactory

Use that exact path unless you have a reason not to.

## Before you start

You need:
- Windows 11
- an account with permission to install software
- one of the Brooks PDFs already available on your PC
- enough disk space for PDFs and extracted files
- PowerShell

Recommended:
- VS Code
- Obsidian already installed

## Step 1 — Create the root folder

1. Open File Explorer.
2. Go to your D: drive.
3. Create a folder named:

   PriceActionExpertFactory

4. Inside that folder, create these folders:

   inbox
   archive
   failed
   logs
   config
   db
   runs
   extracted
   knowledge
   vault

5. Inside extracted, create:

   pages
   sections
   chunks
   figures

6. Inside knowledge, create:

   candidates
   canonical
   review
   exports

7. Inside vault, create:

   00_System
   01_Sources
   02_Glossary
   03_Concepts
   04_Patterns
   05_Setups
   06_Procedures
   07_Principles
   08_Context_Rules
   09_Nuance_Conflicts
   10_Review

Checkpoint:
Your folder tree now exists.

## Step 2 — Copy the phase package into the root

Take the package files you downloaded from this chat and copy them into:

D:\PriceActionExpertFactory

At minimum you should now have:
- README.md
- config\
- db\schema.sql
- templates\
- scripts\
- docs\PHASE_1_QUICKSTART.md

Checkpoint:
The scripts folder exists and contains Python files.

## Step 3 — Install Python

If Python 3.11 or 3.12 is not installed:

1. Download Python from the official Python website.
2. During install, check:

   Add Python to PATH

3. Finish the install.
4. Open a new PowerShell window.
5. Verify with:

   python --version

Expected result:
A version like Python 3.11.x or 3.12.x

If PowerShell says python is not recognized:
- close and reopen PowerShell
- if still broken, reinstall Python and make sure PATH was enabled

## Step 4 — Open PowerShell in the project root

1. Open File Explorer.
2. Navigate to:

   D:\PriceActionExpertFactory

3. Click the address bar.
4. Type:

   powershell

5. Press Enter.

Checkpoint:
PowerShell opens in the correct folder.

Verify with:

   pwd

## Step 5 — Create a virtual environment

Run:

   python -m venv .venv

Wait until it finishes.

Then activate it:

   .\.venv\Scripts\Activate.ps1

If PowerShell blocks the script, run:

   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Then run the activation command again.

Checkpoint:
You should see (.venv) at the start of the PowerShell prompt.

## Step 6 — Install the required Python packages

Run:

   pip install --upgrade pip
   pip install pymupdf pypdf pyyaml watchdog jinja2 rapidfuzz python-frontmatter pandas

If one package fails:
- copy the exact error into a note
- do not install random substitute packages
- fix the named package issue directly

Checkpoint:
No package install error remains.

## Step 7 — Initialize the database

Run:

   python scripts\init_db.py --db db\expert_factory.db --schema db\schema.sql

Expected result:
A message confirming that the database was initialized.

Then check that this file now exists:

   D:\PriceActionExpertFactory\db\expert_factory.db

Checkpoint:
The database file exists.

## Step 8 — Review the source config

Open:

   config\sources.yaml

You should see the four foundation books already listed.

If your file names differ from the config:
- either rename your PDFs to match the config
- or edit sources.yaml so the file_name values match your actual PDF file names exactly

Important:
The source_id values should stay stable once you begin using them.

Checkpoint:
At least one PDF file name in sources.yaml matches a real file you own.

## Step 9 — Put one test PDF into the inbox

Copy one of the foundation PDFs into:

   D:\PriceActionExpertFactory\inbox

Recommended first test:
Trading Price Action Trends (2012)

Checkpoint:
The PDF is physically present inside inbox.

## Step 10 — Register the source

Run this command, replacing the file name if needed:

   python scripts\register_source.py --pdf inbox\Brooks_2012_Trading_Price_Action_Trends.pdf --db db\expert_factory.db --config config\sources.yaml

Expected result:
JSON output that includes:
- source_id
- page_count
- run_id

Checkpoint:
The source registers without an error.

If you get a file-not-found error:
- check spelling
- check that the file is really in inbox
- check the extension is .pdf

## Step 11 — Extract page text

Run:

   python scripts\extract_pdf.py --pdf inbox\Brooks_2012_Trading_Price_Action_Trends.pdf --out extracted\pages --db db\expert_factory.db --source-id brooks_trends_2012

Expected result:
A message showing how many pages were written.

Then confirm this file exists:

   extracted\pages\brooks_trends_2012.pages.json

Checkpoint:
The pages JSON file exists.

## Step 12 — Segment into sections and chunks

Run:

   python scripts\segment_source.py --pages extracted\pages\brooks_trends_2012.pages.json --out-dir extracted --db db\expert_factory.db --source-id brooks_trends_2012

Expected result:
A message with section and chunk counts.

Then confirm these files exist:

   extracted\sections\brooks_trends_2012.sections.json
   extracted\chunks\brooks_trends_2012.chunks.json

Checkpoint:
Both files exist.

## Step 13 — Inspect the outputs manually

This is important. Do not skip it.

### A. Open the pages JSON
Look for:
- page_number values increasing correctly
- text present on most pages
- some noise is acceptable
- not every page should be blank

### B. Open the sections JSON
Look for:
- heading_guess values on some pages
- content_kind values like chapter_body, glossary, or contents

### C. Open the chunks JSON
Look for:
- page_start and page_end ranges
- word_count values that are not zero
- content_kind labels

Checkpoint:
The extracted files look plausible to a human.

## Step 14 — Open the database if you want a spot-check

Optional but useful:
Use a SQLite viewer or extension in VS Code.

Check:
- sources table has one source
- source_passages has many rows
- runs table has one or more rows

Checkpoint:
The data is actually landing in the database.

## Step 15 — Optional: run the basic one-command pipeline

After the manual steps work, test the orchestrator:

   python scripts\run_pipeline.py --pdf inbox\Brooks_2012_Trading_Price_Action_Trends.pdf --root D:\PriceActionExpertFactory --source-id brooks_trends_2012

This runs:
- register_source.py
- extract_pdf.py
- segment_source.py

Use this only after the individual commands already work.

## Step 16 — Optional: start inbox watching

This is the first automation step.

Run:

   python scripts\watch_inbox.py --root D:\PriceActionExpertFactory

Then drop a new PDF into inbox.

What should happen:
- the watcher notices the new PDF
- it triggers the phase-1 pipeline

Important:
For early testing, keep the watcher in a visible PowerShell window so you can see errors.

## What “success” looks like for Phase 1

Phase 1 is successful when:
- Python runs without environment confusion
- the database initializes
- one PDF registers
- page extraction works
- section and chunk files are created
- the folder structure is stable
- you can repeat the process for another foundation book

## Common problems and fixes

### Problem: Python command not found
Fix:
- reinstall Python with PATH enabled
- close and reopen PowerShell

### Problem: Activation script is blocked
Fix:
- run:
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

### Problem: Package install fails
Fix:
- read the exact package name and error
- retry that package alone
- do not change Python version unless necessary

### Problem: PDF path error
Fix:
- verify exact file name
- verify the PDF is inside inbox
- verify the extension is .pdf

### Problem: Empty or near-empty extraction
Possible causes:
- image-heavy PDF
- damaged PDF
- extractor issue

What to do:
- try opening the PDF normally and confirm it contains selectable text
- if the PDF is image-only, note it and do not force Phase 1 to solve OCR yet

### Problem: source_id mismatch
Fix:
- use the source_id from sources.yaml
- keep source IDs stable across runs

## What not to change yet

Do not change these until later phases:
- canonical source priority
- database schema
- folder names
- source_id values already in use
- ontology family names

Keeping these stable will save work later.

## Recommended first run order for the four books

1. Trading Price Action Trends
2. Trading Price Action Trading Ranges
3. Trading Price Action Reversals
4. Reading Price Charts Bar by Bar

That order matches the canonical priority already defined.

## After Phase 1

When Phase 1 is working, the next phase should add:
- candidate extraction
- concept and definition records
- first merge logic
- first Obsidian note writing

## Your Phase 1 checklist

- [ ] Root folder created
- [ ] Package copied into root
- [ ] Python installed
- [ ] Virtual environment created
- [ ] Packages installed
- [ ] Database initialized
- [ ] sources.yaml reviewed
- [ ] One PDF copied into inbox
- [ ] Source registered
- [ ] Pages extracted
- [ ] Sections created
- [ ] Chunks created
- [ ] Outputs inspected manually
- [ ] Pipeline repeat tested on another book

## Final note

This phase is deliberately simple. The win is not elegance. The win is getting a repeatable base running on Windows without hidden moving parts.
