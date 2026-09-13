# Case 02 Version 001 Production and QA Record

## Artifact

- File: `Case2_RunawayRobot_001.pdf`
- Page count: 36
- Page size: US Letter portrait
- Audience: readable and solvable at age nine; tone and visual treatment intended to remain engaging for readers around age ten and older
- Package: learner case, five optional Hint Station pages, and nine-page grown-up guide
- Release status: **QA passed; ready for pull-request review**

## Production decisions

- Preserve the approved educational architecture and five-mission sequence.
- Preserve **Show Your Path before Your Answer**.
- Use the exact Thinking Detective Loop:
  1. Look for a fact or clue you can start with.
  2. Use it to try a path.
  3. Check your path.
  4. Revise if you need to.
- Use generated artwork only for story scenes. Construct every clue-bearing chart, route, table, evidence card, and model prompt deterministically.
- Use the approved restrained palette, simplified textures, quiet backgrounds, and older-reader page treatment.
- Preserve the approved character specifications for Remy, Sunburned Calamari, Cammy Clammy, and DASH-3.

## Illustration validation

Five story scenes were generated and inspected against the approved style anchor:

- cover chase;
- stage presentation;
- DASH-3's departure;
- foam-volcano skybridge complication;
- Final Station reveal.

The final selected scenes use restrained background detail and a limited palette. Calamari has sunglasses, a simple Hawaiian shirt, shorts, flip-flops, exactly two human-like arms and hands, and two legs, with no additional tentacles. Cammy's coat is simplified. Remy's fur is rendered with clean shapes rather than dense brush texture. DASH-3 retains the approved design.

## Initial rendered-page inspection

The complete PDF was rendered and inspected in sequence. The first pass found:

1. a supporting sentence touching the Mission 1 `STOP & SOLVE` box;
2. the DASH-3 label on the tracking scale extending into the location board;
3. Mission 3 explanation choices crowding the evidence table;
4. debrief checklist rows colliding vertically;
5. a missing story bridge from the diagnostic conclusion to the Control Booth plan;
6. the final debrief writing line sitting too close to the closing statement.

## Corrections

- Added separation below the Mission 1 box.
- Shortened and repositioned the tracker signal label without changing its alignment.
- Added space between the Mission 3 evidence table and choices.
- Set fixed checklist-row spacing.
- Added the diagnostic-record story unlock before the interception plan.
- Reduced the last debrief response area from three writing lines to two.

## Functional graphic validation

| Mission | Validation result |
| --- | --- |
| 1 - The First Useful Trail | Six equal evidence cards appear in unambiguous A-F reading order. No useful card receives extra pictorial emphasis. |
| 2 - The Half-Labeled Tracker | Five horizontal reference lines use exactly equal spacing. Labels are 0 m, 50 m, and 100 m; the marker is centered on the unlabeled 75 m line. The transfer scale has three equally spaced ticks labeled 10, blank, and 30. |
| 3 - Remy's Extremely Convincing Theory | All six evidence records and three explanations appear exactly, with no decorative meters or icons that introduce evidence. |
| 4 - Back Up One Paw | The map contains only the six approved connections. The Striped Skybridge is marked with a readable `CLOSED` label and barrier; no direct Blue Arch-Control Booth route exists. |
| 5 - Build the Delivery Model | Five equal location cards and five separate routing rules appear without a supplied solution. Exhaustive permutation testing confirms exactly one valid order. |

## Automated checks

- The build script compiles and completes successfully.
- PDF metadata reports 36 US Letter pages.
- All 36 final pages render successfully at 150 DPI.
- Extracted text contains the approved Thinking Detective Loop, all critical diagnostic records, the routing constraints, learner working prompts, and grown-up guide.
- Mission 5 constraint enumeration returns exactly one solution: Charging Dock, Snack Lab, Bubble Lab, Gear Gallery, Final Station.

## Final full-sequence pass

After corrections, all 36 pages were rendered again and inspected in order for:

- clipping, collisions, and overflow;
- print-safe margins and readable hierarchy;
- handwriting and drawing space;
- story-to-mission-to-unlock continuity;
- accuracy of clue-bearing graphics;
- separation of learner missions from hints and grown-up answers;
- illustration continuity and approved character details;
- restrained backgrounds and absence of unexplained decorative icons;
- consistent prominence of **Show Your Path** before **Your Answer**.

Final result: **QA passed - ready for pull-request review.**
