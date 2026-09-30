# RUN CONFIG — Settings for This Session

Edit these before starting a run. The agent reads this file fresh every
session — it does NOT persist changes back into RULEBOOK.md.

```yaml
platform: indeed + naukri         # indeed | linkedin | naukri | other (name it)
                                  # THIS RUN: both platforms in one session —
                                  # 30 actionable applications on Indeed AND
                                  # 30 actionable applications on Naukri (60 total).
target_cities: []  # empty [] = no city restriction
max_jobs_to_process: 30          # stop after processing this many actionable listings this run
auto_fill_external_forms: false # true = agent will also fill Google Forms / career-site
                                 # ATS forms it finds, not just Indeed's own apply flow.
                                 # Keep false until you've reviewed a few logged links
                                 # and trust the agent's judgement.
send_manual_emails: false       # true = agent will draft AND send emails where JD only
                                 # lists an email address (requires separate email-sending
                                 # tool/access to be wired up — leave false otherwise).
include_less_technical_roles: false  # true = also consider QA/testing, support, BD roles
                                      # per earlier conversation with the user.
resume_path: "docs/Rahul_Pal_Resume_Latest.pdf"
notes_for_this_run: "Candidate is Rahul Pal. Target 30 actionable applications on Indeed AND 30 on Naukri (60 total) this session, using the stack/role list in docs/RULEBOOK.md Section 2. Listings already logged in applications.md dated 2026-09-30 are duplicates — do not re-apply to them; find fresh ones to reach 30 per platform."
```