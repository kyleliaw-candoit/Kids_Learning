# Thinking Detectives

Static website containing approved Cases 1–2 PDFs and the complete five-mission Case 2 interactive adaptation. Case 1 remains PDF-only at the user's request.

Canonical educational materials: https://github.com/kyleliaw-candoit/Kids_Learning
PDFs copied from main following PR #9. Supplied case illustrations are extracted from the approved PDFs. PDF bytes remain unchanged.

## Implementation

Plain HTML/CSS/JavaScript. `dist/` is authored source and deployment output. `app.js` contains the catalog, opening and approved Mission 1; `case2.js` contains Missions 2–5, transitions and reflection. `navigation-route.js` contains sequential page navigation, earned access and the pointer/tap/keyboard route builder. Scripts load in that order before rendering. Future cases extend the catalog with their PDF, artwork and their own routes/content. Do not enable an interactive catalog link before its complete route is available.

Responses remain in browser localStorage, with an in-memory fallback when unavailable; no learner data is sent to a server. Mission 1 retains its existing storage key. Remaining missions have a separate versioned key. Each story gate checks saved earned progress. A successful answer check unlocks the next story and mission. Editing a mission invalidates its current answer check but preserves previously earned page access. Freeform explanations accept written or grown-up-supported spoken/drawn work without semantic grading.

## Quality requirements from the review

- Every thinking mission explicitly states what the learner is solving for before clues or steps.
- Checkboxes and bullets align vertically with the first line of their text. Labels wrap without overlapping controls; controls remain usable on narrow screens.
- Check My Answer precedes Continue the Story. Incorrect answers keep continuation disabled and acknowledge effort before inviting another attempt.
- Use “Give it another try :)”; do not condition trying on feeling ready.
- Hints are optional and revealed only by an explicit button, one at a time. Incorrect answers do not automatically expose hints or solutions.
- Written explanations remain in the thinking record and are not automatically graded. Deterministic checking covers only the structured answer and specified evidence/rules.
- Preserve supportive messages about trying, checking and revising, including the approved closing strong-thinker message. No speed pressure or performance score.
- Validate mission goals, all answer paths, retry feedback, hint progression, disabled continuation, saved progress, and revisions before publication.

## Validation

Run `node --check dist/app.js`, `node --check dist/case2.js`, `node tests/answer-flow.cjs`, `node tests/full-case.cjs`, and `node tests/navigation-route.cjs`. Tests cover Mission 1 regressions, answer validators, all 120 Mission 5 permutations, permissible Mission 4 detours, story gates, mocked screen rendering, hint steps, invalidation and reflection. PDF bytes are compared with approved source files.

Browser visual QA is unavailable for this plain static project under the environment's supervised-preview rules. Mock DOM tests do not establish browser layout, keyboard or print fidelity; these remain a review limitation.

## Cloudflare Pages

Root directory: `sites/thinking-detectives`. Output directory: `dist`. No build command or backend is required. Publish the approved source using Git integration. PDFs are duplicated in the deployment directory so the website is self-contained. Learner progress remains browser-local and does not migrate automatically from the old domain.

Deployment source: exported from the approved Sites revision `5ca8f969acda0cf9c3cc0174ca25dacdc643ddc1`. All image and PDF references use portable same-origin paths; hash navigation preserves asset URLs. The Cloudflare edition is public and requires no OpenAI account.
