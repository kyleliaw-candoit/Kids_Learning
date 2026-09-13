# Interactive Thinking Detectives: requirements and build standard

## Purpose and status

Build interactive editions that strengthen problem understanding, reasoning, exploration and confidence. The interaction supports the thinking process; it must not turn the case into a speed test or an answer-guessing game.

The repeatable learner loop is:

> Look for a fact or clue you can start with. Use it to try a path. Check your path. Revise if you need to.

This document captures the founder's approved Case 2 review decisions and the observed implementation as of September 13, 2026. Case 2's reviewed changes are approved. A complete play-through with Amira and real-device visual, touch, keyboard and print verification remain outstanding. Founder approval is not evidence that every production-quality check passed.

Case 1 remains PDF-only. Do not build its interactive version until requested. Future cases may use this standard without changing the underlying educational architecture.

Related standards: [Learning Philosophy](../Learning-Philosophy.md), [Design Principles](../Design-Principles.md), [Production Quality Gate](../Production-Quality-Gate.md), and [Story Framework](../story-missions/framework.md).

## Source of truth and adaptation boundaries

The approved PDF is the baseline for story text, clues, illustrations, diagrams, answers and sequence. Explicit founder-approved web edits override only the passages or interactions identified in the request.

1. Inventory every PDF page and map it to a web screen or an explicitly linked guide section before adapting it.
2. Preserve narrative wording and character dialogue. Do not silently summarize, rewrite, remove story beats or blend chapters merely to make a shorter web page.
3. Preserve every story illustration at the corresponding point in the story. Extract original artwork; do not generate substitutes for approved illustrations.
4. Preserve functional visual information. A visual map must remain a map, not become only a prose connection list. Maintain topology, labels, closed routes, scale relationships and other puzzle signals.
5. Adapt writing spaces into appropriate controls, but preserve the task, available evidence and valid reasoning paths.
6. Keep chapter headings when combining PDF pages on one web screen. For example, “The Last Stop” and “Case Closed” have separate headings even though the current website displays them on one screen.
7. Record intentional differences in a change log. After an edit, inspect neighboring story and mission screens for references that no longer make sense.

Lessons from Case 2: explicitly identify the Golden Question Mark **trophy** before it is taken; retain the diagnostic reasoning and route-planning dialogue; retain the F-1 through F-5 sequence in “The Last Stop.” A content adaptation must not omit details simply because the implementation can evaluate the answer without them.

## Learner experience and presentation

Every mission states a concrete objective before clues, rules or steps. The learner must know what they are solving for without inferring it from surrounding story text.

Use this conceptual order: objective, evidence, Show Your Path, Your Answer, self-check and Check My Answer, then story continuation. Preserve the established “Show Your Path before Your Answer” principle. Structured manipulation can itself be part of showing a path, such as building a route. Current Case 2 places some answer controls above its notebook; this is an implementation discrepancy to consider in a future review, not a new standard that supersedes the principle.

Use age-appropriate mystery/adventure language, readable text, restrained colors and expressive original characters. Align checkboxes and bullets with their associated text. Keep labels readable when wrapping. Provide meaningful image descriptions, visible keyboard focus and adequately sized controls. On small screens, permit an explicitly labeled map region to scroll rather than shrinking location labels into illegibility.

No countdown, performance score or penalty for hints. Story clock times create narrative stakes; they are not a learner timer. End with reflection on thinking behaviors and preserve:

> A strong thinker does not always know the answer first. A strong thinker knows how to keep moving.

## Navigation and earned access

Use an explicit ordered list of screens. Previous Page goes to the preceding screen in that sequence, not to an arbitrary browser-history entry. Next Page advances only within earned access. Mission links and direct links obey the same boundary.

Current Case 2 sequence:

| Position | Screen / route |
| --- | --- |
| 1 | Opening: `case2` |
| 2 | Mission 1: `mission1` |
| 3 | A Trail with Two Points: `trail` |
| 4 | Mission 2: `mission2` |
| 5 | Seventy-Five Meters: `after2` |
| 6 | Mission 3: `mission3` |
| 7 | A Plan That Almost Works: `after3` |
| 8 | Mission 4: `mission4` |
| 9 | The Part That Still Worked / Five Stops, No Numbers: `after4` |
| 10 | Mission 5: `mission5` |
| 11 | The Last Stop / Case Closed: `after5` |
| 12 | Thinking record: `reflection` |

Initially the opening and Mission 1 are available. Solving Mission N unlocks its following story and Mission N+1. After solving Missions 1–2, every earlier page and Mission 3 are available, but the story after Mission 3 is locked. Solving Mission 5 unlocks the ending and reflection.

Store earned progress separately from the validity of the current edited response. Returning to a solved mission never requires solving it again merely to revisit unlocked pages. Editing an answer invalidates its current check but does not revoke already earned access. Previous/Next navigation must not erase answers, explanations, routes or revealed hints.

The current implementation uses a contiguous `solvedThrough` count from 0–5. A successful check awards the next contiguous mission. Re-checking an earlier mission does not advance this count. Direct links beyond the boundary return to the next unsolved mission. This is a learner-flow guard, not a security boundary: the static application contains its validators and answers client-side.

## Answer-check loop

| State or action | Required result |
| --- | --- |
| New unsolved mission | Continuation disabled; invite the learner to try a path and check an answer. |
| Check an incorrect answer | Acknowledge effort, encourage another attempt, point to optional hints; keep the next story locked. |
| Correct structured answer, incomplete path/self-check | Recognize the answer; ask the learner to show or explain the path and self-check. |
| Correct answer with path or spoken/drawn alternative and self-check | Mark current response verified, award earned progress, enable continuation. |
| Edit a response | Clear current verification and prompt another check. Preserve already earned story access. |
| Reveal a hint | Reveal only one next hint; neither mark the answer correct nor unlock the story. |
| Revisit a solved mission | Restore work; Previous/Next navigation retains earned access. |

Check objective correctness with deterministic rules. Do not claim to assess arbitrary written reasoning. A non-empty explanation establishes that a thinking record was supplied; it is not proof that the explanation is sound. Accept the checkbox alternative for explaining or drawing a path with a grown-up. Display: “Your explanation stays in your thinking record. It is not automatically graded.”

For incorrect attempts use the approved style:

> Good effort—you gave it a try! This answer needs another look. Give it another try :) If you’d like some help, use the hint section below to reveal one hint at a time.

Do not condition trying on feeling ready. Praise the attempt without pretending an incorrect answer is correct. For an incorrect submitted answer, effort feedback must not be replaced by a generic missing-prerequisites reminder. Empty inputs may receive a specific prompt to add an answer.

Current implementation detail: an edited solved mission can have its Check/Continue controls requiring another check while its Previous/Next controls still allow access to already earned story pages. Those represent different states, not contradictory access rules.

## Hints

Hints are opt-in and progressive: start with a useful question, then narrow attention, then provide a stronger foothold. Label the final strong hint clearly. Reveal only one per explicit click and stop when all hints are shown. Wrong answers must not automatically open hints. A “Go to optional hints” action scrolls to the section without revealing anything. Persist the revealed count when navigating or reloading.

## Case 2 correctness contracts (builder/grown-up reference; spoilers)

| Mission | Deterministic acceptance |
| --- | --- |
| 1: useful facts and destination | North Concourse; select wheel-tread fact A and matching-tracks fact B. Sealed-passage fact C is optional. Distractors D–F prompt revision. Accept supported capitalization/punctuation and common destination phrasing; reject negations and conflicting destinations. |
| 2: tracker | Interval 25 meters; distance 75 meters; Prototype Plaza. The optional transfer answer is 20 and does not block continuation. |
| 3: reason for leaving | Programmed delivery. Diagnostic record stays unchanged: 78% power, recharge only below 20%, zero remote commands, DELIVERY mode and active stop 2 of 5. Do not grade the written explanation. |
| 4: alternate route | Start Blue Arch, finish Control Booth, follow actual connected edges, and never pass through the closed Striped Skybridge. Accept connected open detours; do not require the shortest route. |
| 5: delivery model | Check all five ordering rules and require the selected F5 destination to match the model. The resulting unique order is Charging Dock, Snack Lab, Bubble Lab, Gear Gallery, Final Station. |

All main missions additionally require a recorded path or the spoken/drawn alternative and the learner's self-check. These requirements establish participation in the loop, not machine evaluation of reasoning quality.

Mission 3's approved title is “Why DASH-3 left the stage?” Its instruction is “Use DASH-3's diagnostic record to determine the most likely reason why it left the stage.” Follow with the unchanged diagnostic record, “Which is the most likely reason?”, and the approved selection instruction. Avoid prompts that assume the learner evaluated Remy's former remote-steering theory.

## Mission 4 route-builder design

Keep the original PDF map visible, including the red crossed-out skybridge and CLOSED label. Provide an accessible connection list as a secondary equivalent.

The team has already reached Blue Arch: Step 1 is fixed there. Provide location tags and numbered steps. Drag a bank tag to append or replace a step; drag a placed tag to rearrange the sequence. Allow removal of non-start steps. Add another empty step as the route grows. Repeated locations are permitted so a valid detour is not accidentally disallowed.

Provide a tap/keyboard alternative: select a tag, then activate the placement button for a step. Use pointer handling for mouse and touch; give visible selected/drop-target feedback. Cancelled or invalid drops must not corrupt the route. Save the route after changes. The map must not pre-highlight the correct alternative route. Check correctness only through Check My Answer.

## State, privacy and implementation reference

Current live site: [Thinking Detectives](https://thinking-detectives.reptile-k.chatgpt.site). Access is owner-private. Changing the audience requires a separate user request.

Educational requirements and official PDFs live in this `Kids_Learning` repository. The executable website is in a separate Sites-managed Git repository; do not imply this repository contains that application source. The reviewed published source revision is `5ca8f969acda0cf9c3cc0174ca25dacdc643ddc1` (Sites version 8).

Current source structure in that repository:

| File | Responsibility |
| --- | --- |
| `dist/app.js` | Catalog, opening, Mission 1 and route dispatch |
| `dist/case2.js` | Remaining mission content, validators, story transitions and reflection |
| `dist/navigation-route.js` | Earned navigation and draggable route builder |
| `dist/style.css` | Shared presentation and responsive styles |
| `dist/assets/` | Approved PDFs, extracted illustrations and original map rendering |
| `docs/CHANGE-REQUESTS.md` | Review requests and implementation history |
| `docs/ILLUSTRATION-INVENTORY.md` | All 36 PDF pages mapped to web content or linked guide |

Scripts load in the listed JS order before the initial render. This is a plain static HTML/CSS/JavaScript application; no AI grading service, backend learner account, analytics or server-side response storage is required.

Persist responses in browser localStorage with a truthful in-memory fallback message if saving fails. Current keys are `thinking-detectives.case2.mission1.v1` and `thinking-detectives.case2.remaining.v1`. Store selected facts, text, spoken/self-check flags, structured answers, hint counts, current verification, earned progress and reflection. Explain that progress is browser-local: it does not synchronize across devices and can be lost when browser data is cleared. Escape learner text before inserting it into HTML. Validate restored data and version future migrations; preserve existing work rather than silently resetting it.

## Build and review workflow

1. Confirm the requested case/scope and approved PDF revision. Record requirements before drafting or adapting content.
2. Create the PDF-to-screen text and illustration inventory, including functional diagrams and the grown-up guide destination.
3. Define each mission's objective, structured-answer contract, valid alternate paths, hint ladder and following story unlock.
4. Build one representative mission when a new interaction mechanism needs review. Obtain feedback before repeating that mechanism across the case.
5. Implement the full authorized scope using shared navigation/state behavior. Add case-specific content without silently changing approved story prose.
6. Check fidelity against the PDF, including paragraph sequence, dialogue, labels and all illustrations. Compare normalized text where exact fidelity is intended; inspect intentional exceptions manually.
7. Run targeted functional and state tests, then inspect every screen at desktop and the learner's device size. Exercise keyboard, pointer and touch interactions, reloads, browser navigation and the printable record.
8. Fix defects, recheck affected screens and adjacent transitions, and record evidence and outstanding limitations. Apply the Production Quality Gate; do not equate a successful build or mock DOM test with visual QA.
9. Publish the verified source to the existing Site only when implementation/publication is authorized. Preserve access settings. Record the source revision and verify deployment success.
10. Collect founder and learner feedback. If the user asks to batch requests, document them without changing the website until authorized. Mark implemented and approved states separately.

## Acceptance checklist and current evidence

- Objectives precede evidence and explain what is being solved.
- Approved story paragraphs, dialogue and all illustrations are accounted for; diagrams agree with task rules.
- All correct and representative incorrect answers behave as specified; alternate valid paths work.
- Wrong answers acknowledge effort; hints remain optional and sequential.
- Freeform explanations are preserved without semantic grading claims.
- Every Previous/Next link and direct route respects the earned boundary.
- Revisits, edits and reloads preserve work and earned access; unavailable storage is reported honestly.
- Drag, rearrange, replace, remove, cancel, tap and keyboard alternatives work without accidental answers or lost data.
- No overlapping text, cropped illustrations, unreadable map labels or misaligned controls; focus and feedback are perceivable.
- Reflection and printing work on the learner's device.

Existing source tests: `tests/answer-flow.cjs`, `tests/full-case.cjs`, and `tests/navigation-route.cjs`, plus syntax checks for all three JS files. They cover answer variants, distractors, all 120 Mission 5 permutations, open detours, progress boundaries, saved state, and simulated pointer/tap handlers. PDF story pages 20–21 were compared exactly after normalizing line breaks; original artwork and map crop were visually inspected.

Outstanding: real-browser full-screen visual inspection, real touch dragging, keyboard usability and print fidelity. The managed environment did not provide a compatible browser-preview path for this static project. Record these as unverified; do not weaken the existing quality gate or claim they passed. The next Amira session can supply learner feedback, while technical defects remain the builder's responsibility to investigate and fix.
