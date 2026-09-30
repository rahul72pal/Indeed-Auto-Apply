# Job Application Agent — Setup

## 1. Folder structure

```
project/
├── README.md                  ← this file
├── AGENT_INSTRUCTIONS.md       ← the agent's operating manual (read this first, every run)
├── RUN_CONFIG.md               ← toggles you edit before each run
├── applications.md             ← running log the agent writes to (also prevents duplicates)
└── docs/
    ├── RULEBOOK.md                  ← your personal info, CTC logic, standard Q&A answers
    └── Rahul_Pal_Resume_Latest.pdf  ← put your actual resume file here
```

## 2. One-time setup

1. Open this `project/` folder in VS Code.
2. Copy your resume PDF into `docs/` and name it
   `Rahul_Pal_Resume_Latest.pdf` (or update the `resume_path` in
   `RUN_CONFIG.md` to match whatever you name it).
3. Open `docs/RULEBOOK.md` and double-check every value in Section 1 and 2
   is correct and current (CTC, notice period, stack priorities). Update
   this file any time your CTC, notice period, or target stack changes —
   it's the permanent source of truth across all future runs.
4. Make sure your Playwright MCP server is configured and available to
   your agent (Cline / Antigravity / whichever coding-agent client you're
   using), and that it can open a real, visible browser window (not
   headless) so you can log in manually when prompted.

## 3. Before each run

Open `RUN_CONFIG.md` and set:
- `platform` — which site to work on this run (start with Indeed).
- `target_cities` — leave empty for all-India, or restrict to specific cities.
- `max_jobs_to_process` — a safe batch size (25 is a reasonable default to
  review before going bigger).
- `auto_fill_external_forms` — keep `false` for your first several runs.
  Review the "External Application Required" section of `applications.md`
  manually first, get a feel for the kinds of forms that show up, THEN
  consider turning this on.
- `send_manual_emails` — keep `false` unless you've separately wired up an
  email-sending tool/MCP and explicitly want the agent sending emails too.

## 4. The kickoff prompt

Paste this into your agent (Cline / Antigravity / etc.) once the Playwright
MCP tool is connected and you have this folder open as the workspace:

---

> Read `AGENT_INSTRUCTIONS.md`, `RUN_CONFIG.md`, `docs/RULEBOOK.md`, and
> `applications.md` in this project folder in full before doing anything
> else. Then open a real (non-headless) browser window using the
> Playwright MCP tool and navigate to the platform named in
> `RUN_CONFIG.md`. If a login page appears, pause and tell me so I can log
> in manually — do not attempt to log in yourself. Once I confirm I'm
> logged in, search using the role keywords and criteria from
> `docs/RULEBOOK.md` Section 2, respecting any city or count limits set in
> `RUN_CONFIG.md`. For every job listing: read the full JD, check
> `applications.md` for duplicates, decide fit using the rulebook's
> hard-skip and suspicious-signal criteria, determine whether it's a
> native apply / external form / career-page redirect / email-only
> listing, and act according to the rules in `AGENT_INSTRUCTIONS.md`
> Step 3–4. Log every single job you process — applied, external, skipped,
> or paused — in `applications.md` immediately, using its existing
> section format, including any contact info (email/phone/name) found in
> the JD regardless of how you applied. If you hit a question not covered
> by the rulebook, stop, log it under "Paused — Needs Input" with the
> exact question text, and ask me directly rather than guessing. Stop once
> you reach the `max_jobs_to_process` limit or run out of new listings, and
> give me a short summary of how many were applied to, logged externally,
> skipped, or paused.

---

## 5. Reviewing results

After a run, open `applications.md` and check the sections in this order:
1. **⏸️ Paused — Needs Input** — answer these first, since the agent
   stopped mid-way and is waiting on you.
2. **⚠️ Suspicious — Did Not Apply** — sanity check the agent's judgement;
   adjust rulebook wording if it flagged something you disagree with.
3. **🌐 External Application Required** / **📧 Manual Email Application
   Required** — these need you to personally click through and finish
   applying (or explicitly enable auto-fill for next time).
4. **✅ Applied via Portal** — jobs fully handled already; skim for
   anything you want to personally follow up on with a LinkedIn message.
5. **⏭️ Skipped — Not a Fit** — spot-check occasionally to make sure the
   agent isn't being over- or under-cautious with your stack/domain rules.

## 6. Maintenance

- Got a raise / new CTC? Update `docs/RULEBOOK.md` Section 1 and Section 3
  worked examples.
- Notice period changed? Update Section 1.
- Want to target a new city or role type for a while? Either edit
  `RUN_CONFIG.md` for a single run, or update `RULEBOOK.md` Section 2 if
  it's a permanent shift in what you're looking for.
- If the agent keeps getting stuck on the same type of question, add it as
  a permanent standard answer in `RULEBOOK.md` Section 4 so future runs
  don't pause on it.
