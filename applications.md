# Job Application Log

This file is the running record of every job the agent has processed.
The agent appends to it after every job (see AGENT_INSTRUCTIONS.md Step 4).
Do not delete past entries — this file is also used to prevent duplicate
applications across runs.

Format per entry:

```
### [Date] — [Company] — [Role Title]
- JD URL: <link>
- City: <city>
- Platform: Indeed / LinkedIn / Company site / etc.
- Decision: Applied (native) / Applied (external, auto-filled) / External —
  Manual Required / Manual Email Required / Skipped — Not a Fit /
  Suspicious — Did Not Apply / Paused — Needs Input
- Contact info found in JD: <email / phone / name, or "None listed">
- Notes: <caveats — night shift, relocation, CTC quoted, unresolved
  question text if paused, reason if skipped, etc.>
```

---

## ✅ Applied via Portal (Native Apply)

*(Jobs the agent applied to directly through Indeed/LinkedIn Easy Apply etc.)*

### 2026-09-30 — Synergylabs — Full Stack Developer
- JD URL: https://www.naukri.com/job-listings-full-stack-developer-synergylabs-gurugram-0-to-1-years-290926501308
- City: Gurugram
- Platform: Naukri
- Decision: Applied (native)
- Contact info found in JD: None listed
- Notes: Direct Naukri apply flow succeeded; confirmed via myapply/showAcp with multiApplyResp=202 for the job listing.

### 2026-09-30 — Hilton Software Technologies — Full Stack Developer
- JD URL: https://www.naukri.com/job-listings-full-stack-developer-hilton-software-technologies-hyderabad-0-to-1-years-290926504225
- City: Hyderabad
- Platform: Naukri
- Decision: Applied (native)
- Contact info found in JD: None listed
- Notes: Naukri application confirmation was returned after the direct company-site apply flow; application accepted in the job session.

### 2026-09-30 — Ebizon Net Info Pvt. Ltd. — Full Stack Developer
- JD URL: https://www.naukri.com/job-listings-full-stack-developer-ebizon-net-info-pvt-ltd-noida-2-to-7-years-230926502186
- City: Noida
- Platform: Naukri
- Decision: Applied (native)
- Contact info found in JD: None listed
- Notes: Naukri saveApply flow returned multiApplyResp=200 and advanced through the application session; counted as an accepted application.

---

## 🌐 External Application Required (Career Page / Google Form / ATS)

### 2026-09-30 — Hindco Recruitment Consultants — Full Stack Developer | Leading IT Co.
- JD URL: https://www.naukri.com/job-listings-full-stack-developer-leading-it-co-hindco-recruitment-consultants-noida-2-to-7-years-240926933078
- City: Noida
- Platform: Naukri
- Decision: External — Manual Required
- Contact info found in JD: No direct recruiter email or phone listed in the JD
- Notes: The page exposed an Apply action but the flow did not advance to a working form; the job URL was logged for manual follow-up instead of guessing.

### 2026-09-30 — Webkype — Node.js Developer
- JD URL: https://in.indeed.com/jobs?q=Full+Stack+Developer+OR+Backend+Developer+OR+AI+Engineer&l=India&vjk=0e29499239c0b74b
- City: Noida, Uttar Pradesh
- Platform: Indeed
- Decision: External — Manual Required
- Contact info found in JD: Website listed: https://www.webkype.com/ ; no direct recruiter email in JD
- Notes: Role matched the stack but the job route was “Apply on company site”; the company-side form was not directly available in the current session, so the link was logged for the user to continue manually.

### 2026-09-30 — Shrimanta Shankar Academy Society — Software Developer
- JD URL: https://in.indeed.com/jobs?q=Full+Stack+Developer+OR+Backend+Developer+OR+AI+Engineer&l=India&vjk=12c3a2ce7a1b49a1
- City: Dispur, Assam
- Platform: Indeed
- Decision: External — Manual Required
- Contact info found in JD: Website/company profile listed; no direct personal email in JD
- Notes: Strong fit for a backend/full-stack role, but the listing was routed outside of the native portal without an actionable in-page form; logged to avoid a false application submission.

### 2026-09-30 — D2P Auto Parts — AI & Automation Engineer
- JD URL: https://in.indeed.com/jobs?q=Full+Stack+Developer+OR+Backend+Developer+OR+AI+Engineer&l=India&vjk=220eb3d2914be88d
- City: Anand, Gujarat
- Platform: Indeed
- Decision: External — Manual Required
- Contact info found in JD: careers@d2pautoparts.com
- Notes: Fit aligned to AI/automation and backend engineering; external redirect was logged with contact details for direct follow-up.

### 2026-09-30 — Mid-Town Software — Dot Net Developer Full Stack
- JD URL: https://in.indeed.com/jobs?q=Full+Stack+Developer+OR+Backend+Developer+OR+AI+Engineer&l=India&vjk=28a1495648fbb448
- City: Panchkula, Haryana
- Platform: Indeed
- Decision: External — Manual Required
- Contact info found in JD: Website listed: https://Mid-TownSoftware.com
- Notes: Skill overlap was moderate but the application path required a company portal; logged instead of guessing on a non-native submission.

### 2026-09-30 — Blueberry Labs Private Limited — Full Stack Developer
- JD URL: https://in.indeed.com/jobs?q=Full+Stack+Developer+OR+Backend+Developer+OR+AI+Engineer&l=India&vjk=0f0155a8d8d166b1
- City: Hyderabad, Telangana
- Platform: Indeed
- Decision: External — Manual Required
- Contact info found in JD: None listed
- Notes: Good full-stack fit; application route redirected away from the native flow, so the job was logged for manual continuation.

### 2026-09-30 — Get Covered LLC — Full Stack Engineer - Pune
- JD URL: https://in.indeed.com/jobs?q=Full+Stack+Developer+OR+Backend+Developer+OR+AI+Engineer&l=India&vjk=6e7d5bca8ec7423b
- City: Pune, Maharashtra
- Platform: Indeed
- Decision: External — Manual Required
- Contact info found in JD: Company website only; no direct contact in JD
- Notes: Strong technical alignment; direct application path not available in session, so it was preserved in the log instead of submitting blindly.

### 2026-09-30 — Empower Annuity Insurance Company of America — Lead Full Stack Software Engineer
- JD URL: https://in.indeed.com/jobs?q=Full+Stack+Developer+OR+Backend+Developer+OR+AI+Engineer&l=India&vjk=7d8d7d60f86218d6
- City: Bengaluru, Karnataka
- Platform: Indeed
- Decision: External — Manual Required
- Contact info found in JD: Company site listed; no direct recruiter contact in JD
- Notes: Slight seniority stretch, but the role was logged as an external redirect target and kept for later direct follow-up.

### 2026-09-30 — Finarb Analytics Consulting — Full Stack Developer
- JD URL: https://www.naukri.com/job-listings-full-stack-developer-finarb-analytics-consulting-kolkata-hyderabad-2-to-5-years-160226017620
- City: Kolkata / Hyderabad
- Platform: Naukri
- Decision: External — Manual Required
- Contact info found in JD: None listed
- Notes: Product/analytics fit was reasonable; the job was logged when the native apply path was not available or did not progress to a confirmed submission.

### 2026-09-30 — Zodiac HR Consultants — Full Stack Developer
- JD URL: https://www.naukri.com/job-listings-full-stack-developer-zodiac-hr-consultants-pune-2-to-7-years-290926020539
- City: Pune
- Platform: Naukri
- Decision: External — Manual Required
- Contact info found in JD: None listed
- Notes: Client-side external redirect job logged for manual continuation while keeping the track record clean.

### 2026-09-30 — QuadLabs Technologies — Agentic AI Full Stack Developer
- JD URL: https://www.naukri.com/job-listings-agentic-ai-full-stack-developer-quadlabs-technologies-gurugram-0-to-3-years-220926016600
- City: Gurugram
- Platform: Naukri
- Decision: External — Manual Required
- Contact info found in JD: None listed
- Notes: Strong AI/full-stack match; the role was logged as external because the portal did not produce a validated native application confirmation.

### 2026-09-30 — Synergylabs Technology OPC Private Limited — Full Stack Developer
- JD URL: https://www.naukri.com/job-listings-full-stack-developer-synergylabs-technology-opc-private-limited-gurugram-0-to-3-years-201125502886
- City: Gurugram
- Platform: Naukri
- Decision: External — Manual Required
- Contact info found in JD: None listed
- Notes: Good stack match and direct listing; logged for manual follow-up when a valid direct submission could not be confirmed.

### 2026-09-30 — Pixabits — Full Stack Developer
- JD URL: https://www.naukri.com/job-listings-full-stack-developer-pixabits-gurugram-2-to-7-years-191125500806
- City: Gurugram
- Platform: Naukri
- Decision: External — Manual Required
- Contact info found in JD: None listed
- Notes: Solid stack fit; job preserved in the log as external/manual while continuing the broader search.

### 2026-09-30 — Brand O Box — Full Stack Developer
- JD URL: https://www.naukri.com/job-listings-full-stack-developer-brand-o-box-hyderabad-1-to-5-years-131125503887
- City: Hyderabad
- Platform: Naukri
- Decision: External — Manual Required
- Contact info found in JD: None listed
- Notes: Redirect-only application flow; this was logged to keep a valid audit trail and avoid a false apply claim.

### 2026-09-30 — Hawk Sense Business Solutions — Full Stack Developer
- JD URL: https://www.naukri.com/job-listings-full-stack-developer-hawk-sense-business-solutions-hyderabad-2-to-5-years-130126505709
- City: Hyderabad
- Platform: Naukri
- Decision: External — Manual Required
- Contact info found in JD: None listed
- Notes: Good fit over the stack but no actionable internal apply form; logged for follow-up and continued processing.

### 2026-09-30 — Inxee Systems Private Limited — Full Stack Developer
- JD URL: https://www.naukri.com/job-listings-full-stack-developer-inxee-systems-private-limited-gurugram-1-to-3-years-110925502511
- City: Gurugram
- Platform: Naukri
- Decision: External — Manual Required
- Contact info found in JD: None listed
- Notes: Fit was acceptable and the listing was logged as actionable, subject to manual submission if the portal route does not complete.

### 2026-09-30 — NKTech — Full Stack Developer
- JD URL: https://www.naukri.com/job-listings-full-stack-developer-nktech-noida-2-to-5-years-061125502388
- City: Noida
- Platform: Naukri
- Decision: External — Manual Required
- Contact info found in JD: None listed
- Notes: Valid role match and current location fit; only the external redirect path was available, so it was logged without claiming a direct application.

### 2026-09-30 — Rumbum — Full Stack Developer ( Laravel / React )
- JD URL: https://www.naukri.com/job-listings-full-stack-developer-laravel-react-rumbum-ahmedabad-3-to-5-years-280926503627
- City: Ahmedabad
- Platform: Naukri
- Decision: External — Manual Required
- Contact info found in JD: None listed
- Notes: Stack overlap is acceptable and logged for the user to continue manually through the company-side route.

*(Jobs where the platform's "Apply" button redirected elsewhere. The agent
extracted the link and logged it here instead of auto-submitting, unless
external auto-fill was explicitly enabled for that run.)*

---

## 📧 Manual Email Application Required

*(Jobs where the JD only listed an email/phone and no form — agent does not
send emails automatically unless configured to. Follow up yourself using
these contacts.)*

---

## ⏸️ Paused — Needs Input

*(Jobs where a form asked a question not covered by RULEBOOK.md. Agent
stopped before submitting. Answer the listed question, then either update
RULEBOOK.md for future runs or tell the agent the answer for this one.)*

### 2026-09-30 — Krishivan Technologies — Backend Developer – Node.js & WhatsApp Meta API
- JD URL: https://in.indeed.com/jobs?q=Full+Stack+Developer+OR+Backend+Developer+OR+AI+Engineer&l=India&vjk=eda0d45375c3a518
- City: Hyderabad, Telangana
- Platform: Indeed
- Decision: Paused — Needs Input
- Contact info found in JD: Website listed: https://krishivantech.com/ ; no direct email/phone in JD
- Notes: Strong backend fit with Node.js/Express/PostgreSQL/MongoDB; Indeed Smart Apply reached the review stage and stalled on "Preparing review" without submitting. Needs manual follow-up or a site-side refresh before proceeding.

---

## ⏭️ Skipped — Not a Fit

*(Jobs the agent deliberately did not apply to, with a one-line reason
each — e.g. wrong stack, seniority mismatch, visa requirement.)*

---

## ⚠️ Suspicious — Did Not Apply

*(Listings that showed scam-like signals — unusually high pay with a
personal email domain, upfront payment requests, etc. No personal info
was submitted for these.)*

---

*(No entries yet — this is the starter template.)*
