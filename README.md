# Code Design Assistant

An AI assistant for Indian building/structural codes (NBC 2026, IS codes) that answers your question **and shows you the actual source PDF page, highlighted**, so you're never just trusting an AI's word for it. See [`CODES-COVERED.md`](CODES-COVERED.md) for exactly what's covered and which edition.

This repo contains no copyrighted material — only reference notes (our own writing, page-anchored back to the source) and a small tool that works with *your own* copies of the code PDFs. You bring the PDFs; nothing is provided or downloaded for you.

## Do I need a paid Claude plan, and where does it work?

**For the full version (Claude Code): yes, a paid plan is required.** Claude Code is not included in the free Claude plan. You need **Claude Pro or higher** (Max, Team or Enterprise), or an Anthropic API account with credits.

**For the lookup-only version in the Chat tab: no, the free plan works too**, as long as you switch on code execution (Settings → Capabilities). Free plans have tighter usage limits, and Anthropic changes what each plan includes, so check [claude.com/pricing](https://claude.com/pricing) and the [skills help page](https://support.claude.com/en/articles/12512180-use-skills-in-claude) before relying on it.

| Where you open it | Works? | Notes |
|---|---|---|
| **Claude Code in a terminal** (PowerShell, Terminal) | ✅ Full | Open the repo folder and run `claude`. Pulls the page and opens it in your PDF viewer. |
| **Claude desktop app → Code tab** | ✅ Full | Choose **Local**, select this repo's folder. Same tool as the terminal, in a window. |
| **Claude desktop app → Chat tab** | ⚠️ Lookup only | Answers from the notes with clause and page citations, but cannot pull up, highlight or open your PDF. See below. |
| **claude.ai in a web browser / phone app** | ⚠️ Lookup only | Same as the Chat tab. |

**Best experience: Claude Code, in a terminal or the Code tab.** Use the Chat tab or the website only for quick lookups you'll check yourself.

### Using it in the Chat tab / claude.ai (lookup only)

Chat can run this skill in a cut-down mode. It runs in Anthropic's sandbox, which cannot see the files on your computer or open your PDF viewer.

| | In Claude Code (terminal / Code tab) | In Chat tab / claude.ai |
|---|---|---|
| Answer from the reference notes, with clause and page | ✅ | ✅ |
| Know which edition is covered and the known gaps (`CODES-COVERED.md`) | ✅ | ✅ |
| Pull the real PDF page and highlight the clause | ✅ | ❌ |
| Open the page on your screen | ✅ | ❌ |
| Read your own PDFs (`sources.json`) | ✅ | ❌ |
| Build a new note for a code that isn't covered | ✅ | ❌ |
| Needs Python / `pymupdf` installed | Yes | No |
| Needs a paid plan | Yes | No, free works if code execution is switched on (Settings → Capabilities) |

In this mode the skill tells you in every answer that the page was **not** shown, and gives you the clause and PDF page number so you can open your own copy of the code and check it yourself. Treat it as a fast pointer, not a verified answer.

To set it up in Chat: in the Claude app go to **Customize → Skills → Upload a skill**, and upload a ZIP made like this:
1. Make a new folder named `code-lookup`.
2. Copy `.claude/skills/code-lookup/SKILL.md` and the whole `vault` folder from this repo into it.
3. Right-click the `code-lookup` folder, choose **Send to → Compressed (zipped) folder**, and upload that ZIP.

(Not yet tested end-to-end in the Chat tab. Tell the maintainer if it misbehaves.)
## What you need

1. **[Claude Code](https://code.claude.com)** (needs a paid plan, see above) — either the terminal CLI, or the **Code tab in the Claude desktop app** for a proper chat/GUI interface (recommended if you don't want to use a terminal — same underlying tool, just a nicer window).
2. **Python 3.9+** with `pymupdf` installed: `pip install pymupdf`
3. A PDF viewer (Adobe Acrobat or your OS's default) — only needed if using the terminal CLI. Claude Code Desktop can display pages in its own Browser pane instead.
4. **Your own legally-obtained copies** of the codes you want to use — see "Getting the source PDFs" below.

## Setup

On Windows, steps 1–2 and 4 can be done by copy-pasting one line each into PowerShell — no downloads-page hunting required. Open PowerShell first: search "PowerShell" in the Start menu and open it, then paste each command below and press Enter.

### 1. Install Claude Code (skip if you already have it)
```powershell
irm https://claude.ai/install.ps1 | iex
```
Close and reopen PowerShell afterward (so it picks up the change), then check it worked:
```powershell
claude --version
```
Prefer a proper window over a black terminal screen? Download the [Claude Code Desktop app](https://claude.com/download) instead — same tool, just double-click the installer, no commands needed.

### 2. Install Python (skip if you already have it)
```powershell
winget install -e --id Python.Python.3.12
```
This installs Python *and* sets it up correctly on its own — no checkbox to remember. Close and reopen PowerShell, then check it worked:
```powershell
python --version
```
You should see something like `Python 3.12.4`. (If PowerShell says `winget` isn't recognized — rare, only on older/unupdated Windows — get Python from [python.org/downloads](https://www.python.org/downloads/) instead, and tick "Add python.exe to PATH" on the installer's first screen.)

### 3. Get this repo onto your computer
Pick whichever is easier for you — both give you the same files:

- **No extra install needed:** on the repo's GitHub page, click the green **Code** button → **Download ZIP**, then unzip it anywhere on your computer.
- **Using git** (lets you get future updates with one command instead of re-downloading): install Git from [git-scm.com/downloads](https://git-scm.com/downloads), then in PowerShell:
  ```powershell
  git clone https://github.com/Roger5289/Civil-Engineering-Code-Assistant.git
  ```

### 4. Install the Python dependency
In PowerShell, navigate into the folder from step 3 (e.g. `cd Downloads\Civil-Engineering-Code-Assistant`), then run:
```powershell
pip install pymupdf
```

### 5. Open the folder in Claude Code (or Claude Code Desktop)
The skill is picked up automatically — no separate install step.

- **Terminal CLI:** in PowerShell, make sure you're inside the repo folder (same `cd` as step 4), then run:
  ```powershell
  claude
  ```
- **Claude Code Desktop:** open the app, click the **Code** tab at the top, choose **Local**, click **Select folder**, and pick the repo folder you cloned/unzipped.

### 6. Tell it where your PDFs are
This is the one step that needs your own files, and there are two ways to do it — pick whichever you're comfortable with:

   **Easy way (recommended — no file-editing at all):** Just ask, in plain language, right in the chat:
   > "Set up sources.json for me. My IS 456 PDF is at D:\MyCodes\IS 456.pdf, and my NBC 2026 PDF is at C:\Users\me\Documents\NBC2026.pdf"

   List only the codes you actually own — skip the rest. Claude Code will create the file for you correctly, no JSON syntax to get right.

   **Manual way (if you'd rather do it yourself):** Copy `sources.template.json`, rename the copy to `sources.json`, and fill in the path to each code PDF you own:
   ```json
   {
     "IS456": "D:/MyCodes/IS 456.pdf",
     "NBC2026": "C:/Users/you/Documents/NBC2026.pdf"
   }
   ```

   Either way, `sources.json` never leaves your computer — it's excluded from git, so it's never uploaded or shared, even if you later contribute improvements back to the project.

## Using it

Just ask a question in plain language:

> "What's the minimum cover for a beam under IS 456?"
> "What's the required staircase width for an assembly occupancy under NBC 2026?"

The assistant finds the relevant clause in the knowledge notes, tells you the answer with its clause/page citation, and pulls up the actual source page — highlighted — so you can verify it yourself. If you don't have that code's PDF in `sources.json` yet, it'll tell you which key to add rather than guessing or answering unverified.

**Push back on the first answer.** The most reliable way to use this is to cross-question it — "so is that actually mandatory?" or "does that apply above a certain height?" — the same way you'd sanity-check a junior engineer. That's genuinely how real ambiguities in the source codes have been caught during this project's own testing.

## Getting the source PDFs

Get your own copies from **BIS's official channels only**:
- [bis.gov.in](https://www.bis.gov.in/?lang=en) — Bureau of Indian Standards, the publisher
- [standardsbis.bsbedge.com](https://standardsbis.bsbedge.com/) — BIS's authorized digital distribution partner (runs their free-of-cost download program for standards that qualify, and paid purchase for the rest)

**Do not use third-party "free PDF" sites** (Internet Archive, pdfcoffee, scribd, random blog mirrors, etc.). Beyond the legal issue, they're also a real accuracy risk — you have no guarantee you're getting the actual current edition rather than an old scan someone reposted. Always verify the edition/revision year on the title page against [`CODES-COVERED.md`](CODES-COVERED.md) before assuming a PDF you've found matches what this project expects.

## Getting updates

This project gets updated as more codes get built out.

- **If you used git:** run `git pull` inside the folder.
- **If you downloaded the ZIP:** just download it again from the **Code** button and unzip over the old folder.

Either way, your `sources.json` is untouched (it's gitignored) — new codes just mean new keys you can add whenever you get that PDF. Check `CODES-COVERED.md` after each update for what's new.

## If a code you need isn't covered

Two options:
1. **Ask the assistant to build it**, if you have that code's PDF — it uses the same method (full read, page-anchored, dense tables verified against page images, audited after building) described in `.claude/skills/code-lookup/SKILL.md`. This happens locally on your machine.
2. **Send it back**, if you want it added for everyone — a locally-built note doesn't automatically merge into the shared project. Send the maintainer the note (or open a pull request) for review first. The whole value of this project is that everything in it has been read in full and audited — that only holds if new contributions get the same scrutiny.

## Licence and copyright

The skill, script and our own writing are under the [MIT licence](LICENSE). The Indian Standards content they refer to belongs to BIS and is **not** covered by it, and no source PDFs are included. Read [NOTICE.md](NOTICE.md), which also explains how to report an error or request removal.
## What this is not

Not legal advice, and not a replacement for the actual code or your jurisdiction's Authority Having Jurisdiction (AHJ). It's a fast, verifiable way to find and read the clause you need — always confirmed against the real source page, never invented. Where the source text itself is genuinely ambiguous, the assistant is built to say so rather than guess.

Always check the highlighted source page yourself before using a number in real design work — this project is built and audited carefully, but the highlight exists precisely so you never have to just take the AI's word for it.
