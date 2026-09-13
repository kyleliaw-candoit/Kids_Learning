# Thinking Detectives — pending change requests

## Review process

Collect the user's feedback here. Do not implement or publish these requests until the user asks to apply the collected changes together. Recording feedback does not authorize implementation.

## CR-001 — Previous/next page navigation

Status: Implemented in the user-authorized batch.
Requested: 2026-09-13.
Scope: Case 2 interactive edition.

Problem: While on Mission 2, the reader wanted to reread the story immediately preceding it. Navigation should support moving through the case in story order, rather than returning only to the case opening or jumping between missions.

Requested behavior:

- Provide Previous Page and Next Page navigation on both mission and story pages.
- Previous Page returns to the immediately preceding page in the case sequence.
- Readers can revisit any already unlocked page and move forward again without repeating solved missions.
- Forward navigation ends at the next unsolved mission. The story after that mission stays locked until the mission is solved through the approved answer-checking flow.
- Example: after solving Missions 1 and 2, the reader can move backward through all earlier pages and forward through the story before Mission 3, up to Mission 3 itself. They cannot reach the story after Mission 3 until solving it.
- Preserve the learner's answers, explanations, revealed hints, and progress when navigating.
- Apply the same access limit to page controls, mission links, and direct page navigation.

Implementation is deferred while the user continues reviewing and submitting requests.

## CR-002 — Simplify Mission 3 presentation

Status: Implemented in the user-authorized batch.
Requested: 2026-09-13.
Scope: Case 2 interactive edition, Mission 3.

Purpose: Make the task more straightforward and less confusing by focusing directly on why DASH-3 left the stage and using its diagnostic record to choose the most likely reason.

Requested wording, in presentation order:

| Element | Current text | Requested text |
| --- | --- | --- |
| Mission title | Remy’s Extremely Convincing Theory | Why DASH-3 left the stage? |
| Introductory text below the title | Remy thinks someone remotely steered DASH-3 to steal the trophy. Does the record support his theory? | Use DASH-3's diagnostic record to determine the most likely reason why it left the stage. |
| Diagnostic record | DASH-3 diagnostic record | Keep as is, including its contents. |
| Answer section heading | Which explanation fits? | Which is the most likely reason? |
| Instruction below answer section heading | Check each explanation against the record before choosing. | Select the most likely reason based on DASH-3's diagnostic record |

Preserve the user's requested wording above. No implementation or publication is authorized yet; include this request in the next user-authorized batch alongside CR-001.

### CR-002 follow-up — Align the story immediately after Mission 3

Status: Implemented in the user-authorized batch.

The user also requests revising the opening paragraph of the story immediately after Mission 3, because the revised mission no longer frames the task around Remy's remote-steering theory.

Current paragraph:

> “Zero remote commands,” said Cammy. That was where Remy’s remote-steering theory broke. With 78% power, DASH-3 did not need an automatic recharge either.

Proposed replacement for the implementation batch:

> “Zero remote commands,” said Cammy. “So nobody was steering DASH-3 remotely. And its power was at 78%—well above the level that would send it back to recharge.”

Keep the following explanation of DELIVERY mode and the active programmed route. The transition should compare the possible reasons against the diagnostic evidence without assuming the learner encountered Remy's theory in Mission 3. This is part of pending CR-002; do not implement or publish until the user authorizes the batch.

## CR-003 — Restore Mission 4's visual route map

Status: Implemented in the user-authorized batch.
Requested: 2026-09-13.
Scope: Case 2 interactive edition, Mission 4.

Replace the visible text-only “Available connections” list with the visual route map from the approved Case 2 PDF, as shown in the user's second screenshot. Retain the PDF's spatial arrangement, labeled locations, connections, and conspicuous closed-skybridge indication.

Reference layout:

- Prototype Plaza at left connects to Blue Arch.
- Blue Arch branches upward to Striped Skybridge and downward to Workshop Hall.
- Striped Skybridge connects to Control Booth at right; show the skybridge crossed out in red and labeled CLOSED.
- Workshop Hall connects horizontally to Ground Passage, which connects upward to Control Booth.
- Preserve this topology and the map's usefulness for reasoning; do not replace it with a prose list as the primary presentation.

Reference: approved PDF at `dist/assets/Case2_RunawayRobot_001.pdf`; user-supplied screenshot `c7b2fe7f-2f15-4d91-ad86-ef4c4e1322a0.png` shows the desired map. The other screenshot, `74101c11-ba84-475b-9028-3717467878ec.png`, shows the current text-only list to replace.

Ensure map labels remain readable at desktop and mobile sizes, and provide an accessible text equivalent. This request changes the presentation of the route information; no additional interaction changes were requested. Defer implementation and publication until the user authorizes the collected batch.

## CR-004 — Preserve all Case 2 PDF illustrations in the interactive edition

Status: Implemented in the user-authorized batch.
Requested: 2026-09-13.
Scope: Entire Case 2 interactive adaptation.

The user identified a missing PDF illustration on “A Plan That Almost Works,” the story immediately after Mission 3. Restore that illustration when the batch is authorized.

The request also applies across the full case: do not omit illustrations from the approved PDF. During implementation, inventory the PDF's illustrations page by page, compare them against their corresponding interactive story and mission screens, and restore all omitted illustrations in the appropriate narrative positions. Preserve the original artwork and its story context, with readable, responsive display and suitable alternative text. Include the visual route map covered by CR-003 in the completeness check; do not treat restoring that map alone as completing this request.

Source: `dist/assets/Case2_RunawayRobot_001.pdf`. Record the illustration-to-screen mapping and check completeness before presenting the batch as finished.

This records the requested change only. Do not implement or publish until the user authorizes the collected batch.

## CR-005 — Mission 4 draggable route construction

Status: Implemented in the user-authorized batch.
Requested: 2026-09-13.
Scope: Case 2 interactive edition, Mission 4, “Your route” section.

With the visual map restored under CR-003, replace the current click-to-append location buttons and route list with draggable location tags and numbered route slots (Step 1, Step 2, Step 3, and so on). The learner should construct an alternative route to Control Booth now that Striped Skybridge is closed.

Requested interaction and implementation acceptance:

- Show location tags that the learner can drag into numbered steps to construct the route.
- Allow the learner to revise the sequence, including moving, replacing, or removing a placed tag.
- Keep the starting context clear: the team has already reached Blue Arch. Preserve the mission's goal of finding an open route to Control Booth.
- Use the restored visual map as the reference for route construction. Do not reveal the correct alternative route in advance.
- Retain the approved Check My Answer, encouraging retry, optional one-at-a-time hints, and gated story continuation.
- Check the constructed route against the actual map connections and closed skybridge. Do not impose an unstated shortest-route requirement.
- Support touch dragging and an accessible tap/keyboard alternative for placing and rearranging tags.
- Preserve the constructed route when leaving and returning to the mission.

Reference: user screenshot `bacd401e-0ce2-47b6-b573-88b4ba715949.png` shows the current “Your route” section to replace. This extends CR-003's presentation change with an explicitly requested interaction change.

Defer implementation and publication until the user authorizes the collected batch.

## Batch implementation

User authorized implementation of CR-001 through CR-005. All five requests are implemented. Prior deferral instructions above are retained as review history and were superseded by this authorization. Navigation uses a saved earned-progress boundary, separate from current answer edits, so revisiting solved missions does not revoke story access. See ILLUSTRATION-INVENTORY.md for the PDF visual completeness check.

## Story fidelity corrections after batch review

Implemented at the user's request: retained the approved diagnostic opening on “A Plan That Almost Works” and restored the user's supplied subsequent passage. Restored “The Last Stop” verbatim from PDF page 20, including the explicit F-stop sequence in its first paragraph. Restored page 21's following text under its own “Case Closed” heading instead of blending it into “The Last Stop.” Both original illustrations are retained. Compared pages 20–21 narrative with the PDF, normalizing only line breaks.
