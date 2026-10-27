---
name: code-lookup
description: Answer Indian building/structural code questions (NBC 2026, IS codes) using the page-anchored reference notes in vault/02 - Civil Engineering, and show the actual source PDF page — highlighted — as proof. Also supports building new reference notes for codes not yet covered, using the same no-hallucination method. Use whenever the user asks a question about NBC 2026, an IS code, or SP 16/34, or asks to add coverage for a new code.
---

# Code Lookup & Reference Builder

This skill answers Indian building-code questions from a curated set of reference notes, and — critically — never just states an answer from memory. Every real answer gets verified against, and shown from, the actual source PDF page.

## Which mode are you in? (check this first)

- **Full mode** — you are running in Claude Code (terminal or Code tab), can run `python scripts/pull_source.py`, and `sources.json` exists. Follow everything below, including showing the highlighted source page.
- **Lookup-only mode** — you are in the Chat tab / claude.ai, or you cannot run scripts, or the user has no PDFs configured. Answer from the notes in `vault/02 - Civil Engineering/` only, and:
  1. Give the clause number and PDF page for every figure, exactly as the note states them.
  2. State plainly in every answer: **"I have not shown you the source page. Open your own copy of the code to PDF page N and check clause X before relying on this."** Never imply the answer was verified against the PDF.
  3. Check `CODES-COVERED.md` and warn if the code is one with a known edition gap (IS 13920, IS 1893 Part 1, IS 875 Part 3).
  4. Do not offer to build new notes in this mode; that needs the user's PDF and Claude Code.
  5. If the user asks you to open or highlight a page, say that needs Claude Code (terminal or the Code tab) and point them to the README.
## How this project is put together

- `vault/02 - Civil Engineering/` — the knowledge layer. Page-anchored reference notes, one per code (or per Part/Section for large codes), built by reading the actual source PDFs cover to cover. Not a summary — each note cites the exact clause number and PDF page for every figure it states.
- `CODES-COVERED.md` — the manifest: which codes are covered, which edition, how deep, and any known edition gaps (a code here might not be the current BIS edition — check this file before trusting an answer where currency matters).
- `sources.json` (gitignored, user-created from `sources.template.json`) — maps a short code key (e.g. `IS456`, `NBC2026`) to the absolute path of *that user's own* copy of the source PDF. Never assume this file exists or is complete — see Setup below.
- `scripts/pull_source.py` — extracts a page range from a source PDF, optionally highlights exact text on it, saves a copy, and opens it. This is the "show your work" mechanism. Never modifies the original PDF.

## Setup check (do this before the first lookup in a session)

If `sources.json` doesn't exist at the repo root, tell the user to copy `sources.template.json` to `sources.json` and fill in paths to their own PDFs — do not proceed with a source-pull until it exists. If it exists but is missing the specific code being asked about, tell the user which key to add (check `CODES-COVERED.md` for the exact key name) rather than guessing a path or answering without verification.

## Answering a question (lookup mode)

1. **Find the right note.** Identify which code/Part/Section the question is about, and open the relevant note(s) in `vault/02 - Civil Engineering/`. These notes are small and fast to read — that's the point of having them; you don't need to touch the source PDF just to find the clause number.
2. **Extract the clause + page citation** from the note. Every note gives a clause number and PDF page for its figures.
3. **Verify and show the source.** Run:
   ```
   python scripts/pull_source.py <SOURCE_KEY> <start_page> <end_page> --highlight "<exact phrase from the clause>"
   ```
   Use the note's cited page(s) directly — don't pad with extra "context" pages, and don't re-verify things already confirmed (e.g. don't re-check that pymupdf is installed every time). One call does extract + highlight + open.
4. **Answer with the verbatim clause text + plain-language explanation + citation** (clause number, page). The opened/highlighted PDF page is the proof — the user should be able to see for themselves that nothing was invented.
5. **If running in Claude Code Desktop**, the opened PDF will typically appear in the Browser pane — reference its path clearly in your response either way, in case the user needs to open it manually. If running in the terminal, it opens in the OS default PDF viewer.

**No-hallucination rule**: never answer a code question from memory or training data when a source note exists for it. If a note doesn't cover the specific clause asked about, say so plainly and offer to pull the relevant page directly from the source PDF (via `pull_source.py`, using the code's known page range from the note's front matter) rather than guessing.

**Validation method — encourage cross-questioning.** The most reliable way this system has been tested is the user asking a follow-up ("so is X actually mandatory then?") rather than accepting the first answer. If a follow-up surfaces a genuine ambiguity in the source's own wording, say so plainly — flag it as needing AHJ (Authority Having Jurisdiction) confirmation rather than picking a reading and presenting it as settled.

## Building a new reference note (extension mode)

If asked about a code not in `CODES-COVERED.md`, or asked to add one, this skill can build a new note the same way the existing ones were built — but it needs the user's own copy of that code's PDF (added to `sources.json` first).

1. **Confirm the edition before reading a single page.** Open the PDF's title page and check the revision number/year. Source libraries often contain multiple editions of the same code (e.g. an old working-stress edition next to the current limit-state one, or a superseded seismic-code edition) — sometimes under confusingly similar filenames. State which edition you're building from and ask the user to confirm it's the one they want, especially if an even newer edition might exist that isn't in their library at all (check BIS's official portal, see README, rather than assuming the local copy is current).
2. **Read the whole document, or the whole relevant Part/Section**, before writing anything. No sampling.
3. **Page-anchor everything.** Every clause, table, and figure in the note gets a source PDF page number.
4. **Verify dense or multi-column tables against a rendered page image, not linear text extraction.** This is the single most important lesson from building this project: PDF text extraction reads multi-column tables (side-by-side data blocks, or even categorized lists split into columns) out of order, silently swapping values between rows or dropping cells — and the resulting text often *looks* clean, giving false confidence. Any table with more than one data column per row needs either word-level coordinate extraction or a rendered page image (`page.get_pixmap()`) checked directly before it goes in a note.
5. **Flag genuine ambiguity instead of resolving it.** If the source text itself doesn't cleanly settle a question (conflicting clauses, ambiguous wording), say so in the note rather than picking an interpretation and presenting it as fact.
6. **For very large, low-stakes reference material** (a huge lookup table, an appendix of standard section properties, a bibliography) where full transcription would be mostly redundant or low-value, a navigation-guide/index treatment (what's on which page) is an acceptable alternative to full transcription — but say explicitly that's what was done, don't silently thin out coverage.
7. **Audit after building.** Re-read the finished note against the source once more, specifically re-checking anything pulled from linear text rather than an image, before calling it done. This has caught real errors on every code built so far.

**Contribution note**: a note built this way is local until it's reviewed. If you want it added to the shared project, send it to the maintainer rather than assuming it merges automatically — the value of this project is the audit discipline, and that only holds if new material gets the same scrutiny as what's already here.

## What this skill will not do

- Never invent a clause, number, or citation. If it isn't in a note and can't be verified against a source page, say so.
- Never redistribute or upload a copyrighted source PDF anywhere. `pull_source.py` only ever reads a user's own local file and writes a highlighted copy locally (gitignored, never committed).
