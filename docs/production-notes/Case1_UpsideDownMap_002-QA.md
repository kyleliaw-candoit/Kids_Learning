# Case 01 Version 002 Production and QA Record

## Artifact

- File: `Case1_UpsideDownMap_002.pdf`
- Page count: 21
- Audience: approximately age nine
- Package: learner pages and grown-up guide in one PDF
- Release status: **QA passed**

## Production decisions

- Preserve the approved story and all five Thinking Missions.
- Preserve **Show Your Path before Your Answer** on every mission.
- Keep text and illustrations in separate, non-overlapping layout regions.
- Use the approved medium-complexity, hand-drawn Remy treatment.
- Use generated art for story scenes and precisely constructed graphics for functional puzzle information.
- Include the grown-up guide at the end of the same PDF.

The Version 002 story art was accepted. For later versions, retain the character and focal-object complexity but simplify the backgrounds so they do not compete with the main action.

## Initial rendered-page inspection

Every page was rendered to PNG at 150 DPI and visually inspected in sequence.

Defects found:

1. The finale illustration initially placed Remy's purple slipper inside the chest, conflicting with the story statement that it was behind the chest.
2. The Mission 1 windmill symbol was too abstract to identify quickly.
3. The Mission 4 facts and Mission 5 route-card text were smaller than preferred for print.
4. Answer lines began at a fixed horizontal position and could run beneath longer answer labels.
5. The badge tally used the letter `O` instead of a true empty circle.

## Corrections

- Moved the purple slipper behind the chest and removed the conflicting copy inside it.
- Replaced the windmill symbol with a recognizable tower, hub, and four sails.
- Increased critical facts, logic-grid labels, and route-card text.
- Made answer-line placement depend on the measured label width.
- Replaced letter marks with drawn empty circles.

Corrected pages and relevant neighboring pages were re-rendered and re-inspected.

## Functional diagram validation

| Mission | Validation result |
| --- | --- |
| 1 - Which Way Is Up? | Map shows windmill at top, pond at right, and clock at bottom; a 180-degree turn matches the stated real-world relationships. |
| 2 - The Clock That Stopped | Clock shows 4:10; timeline moves backward 35 minutes; intended answer remains 3:35. |
| 3 - The Three-Part Trail | Segments are 3, 4, 2, and unknown; whole journey is 12; intended remainder remains 3. |
| 4 - The Suspicious Shed | Facts, three clue objects, three animals, and the one-to-one logic grid agree; intended carrier remains Benny Beaver. |
| 5 - Beat the Sunset | Plan A totals 35 minutes and Plan B totals 36 minutes; both finish before the 40-minute limit. |

## Final full-sequence pass

After corrections, the complete 21-page PDF was rendered again and every rendered page was inspected for:

- text overflow, clipping, and collisions;
- readability and print-safe margins;
- writing-space adequacy;
- diagram correctness and clue clarity;
- illustration clarity, continuity, and age fit;
- story-to-mission-to-hint sequence;
- separation of learner content from grown-up answers;
- preservation of **Show Your Path before Your Answer**.

Automated checks also confirmed:

- all 21 pages were present;
- all five mission pages contained a Show Your Path region;
- all five Hint Stations were present;
- both grown-up guide pages were present;
- all extracted text remained inside the page bounds.

Final result: **QA passed - ready to present.**

## Repository copy

The PDF stored in `assets/missions-in-story/` uses lossless document-structure compression plus 144 DPI, quality-82 JPEG compression for the story images so the asset can be managed efficiently in GitHub. The text extraction, page count, dimensions, layout, and sequence match the delivered PDF. All 21 pages of the repository copy were rendered again at 150 DPI and visually inspected after compression; no new defects or unreadable illustration artifacts were found.
