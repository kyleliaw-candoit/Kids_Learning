# Production Quality Gate

## Purpose

Every learner-facing artifact must pass a dedicated quality inspection **after generation and before it is presented to the user or treated as complete**.

This applies to standalone Thinking Missions, story-mission booklets, welcome pages, case files, grown-up guides, and future printable or digital learning materials.

The learning design and story design may be experimental. Production defects are not experiments.

> **No learner-facing artifact is considered finished until the rendered output has been inspected and passed.**

## Required workflow

Use this sequence every time:

1. **Create the artifact.**
2. **Render every page** of the final PDF or document into viewable page images at a readable resolution.
3. **Inspect every rendered page**, not only selected pages.
4. **Record defects** found during inspection.
5. **Fix all blocking production defects.**
6. **Re-render the affected artifact.**
7. **Re-inspect the corrected pages and any adjacent pages affected by reflow.**
8. **Present the artifact only after the quality gate passes.**

If the output has not been rendered and visually inspected, it has not passed QA.

Do not present a newly generated PDF immediately after generation. Generation success is not release approval.

After corrections, perform two levels of reinspection:

1. re-render and inspect every corrected page plus any adjacent page affected by reflow;
2. render the complete final PDF again and inspect the full page sequence before delivery.

## Blocking production defects

The following defects must be fixed before release:

### Layout and typography

- text flows outside its intended box or page;
- text overlaps illustrations, diagrams, or other text;
- clipped or cropped text;
- text is too small for the intended age group;
- headings or labels collide with content;
- awkward line breaks materially reduce readability;
- insufficient margins or unsafe print areas;
- writing areas are too small for the task.

### Illustration placement

- artwork overlaps learner-facing text;
- important artwork is cropped unintentionally;
- illustration scale is visually unbalanced;
- an illustration creates ambiguity about what belongs to the problem;
- decoration competes with functional information.

### Illustration quality and age fit

Characters should remain visually simple and consistent, while the overall treatment should feel like middle-grade illustrated fiction: appealing around age ten and older while remaining clear to the current nine-year-old learner.

Reject or revise illustrations that:

- look like placeholder clip art or overly simple line symbols;
- do not communicate their intended meaning within roughly two seconds;
- feel too babyish for the target age;
- are visually confusing or semantically unclear;
- add decoration without supporting story, emotion, or reasoning;
- make critical puzzle information difficult to distinguish.

Use the principle:

> **Simple characters, richer worlds, clear puzzle signals.**

Story scenes may include purposeful atmosphere and a few distinctive setting cues while keeping Remy and recurring characters simple and recognizable. Do not use edge-to-edge environmental detail merely to make a scene feel finished.

Interpret “richer worlds” as richer than placeholder clip art, not as maximum detail. The approved focal hierarchy is now:

> **Medium-detail characters and key objects; quieter backgrounds; clear puzzle signals.**

Backgrounds must use fewer secondary props, broader shapes, softer contrast, and less texture than the focal characters and story-critical objects. The learner should notice the action or clue first and the setting second.

See `Illustration-Production-Standard.md` for the complete complexity target.

Functional mission graphics—maps, routes, clocks, timelines, grids, tables, diagrams—must be both visually engaging and logically precise.

## Illustration roles

Every illustration should have a clear job. It should normally do at least one of the following:

1. **Tell the story** — show a meaningful scene, place, action, or reveal.
2. **Support reasoning** — provide accurate information needed to solve the mission.
3. **Show character emotion** — communicate confusion, curiosity, effort, surprise, persistence, or pride.

Avoid unexplained collections of decorative icons that require an adult to interpret.

## Functional graphics versus story art

Treat these as separate production systems.

### Functional graphics

Examples: maps, logic grids, clocks, timelines, route diagrams, tables.

Requirements:
- precise;
- internally consistent;
- easy to read;
- problem-critical information visually prominent;
- decorative richness must not obscure reasoning.

### Story illustrations

Examples: Remy at the town clock, Dottie near the shed, the sunset at the oak door.

Requirements:
- engaging and age-appropriate;
- visually richer than simple diagrammatic symbols;
- expressive;
- clearly connected to the surrounding story;
- consistent with the approved Remy character design.

## Semantic clarity test

For every illustration, ask:

- Can a nine-year-old understand what this is showing without adult explanation?
- Is the intended action, location, or relationship obvious?
- If it supports a problem, can the learner identify the relevant information quickly?
- Does the image help rather than merely occupy space?

If the answer is no, revise or remove the illustration.

## Page-level inspection checklist

Inspect every rendered page for:

- no overflow;
- no collisions;
- no clipping;
- readable font sizes;
- balanced whitespace;
- adequate response/writing space;
- correct page order;
- correct story-to-mission transitions;
- hints do not reveal answers prematurely;
- diagrams match the written problem exactly;
- story illustrations are understandable and age-appropriate;
- artwork feels middle-grade rather than like a toddler picture book;
- color, when used, follows a restrained coordinated palette;
- open space is preserved where it improves hierarchy and readability;
- characters and key objects dominate quieter backgrounds;
- background detail does not compete with the focal action or clue;
- Remy remains visually consistent;
- answer/guide content is not accidentally exposed on learner pages.

## Artifact-level inspection checklist

After page-level review, inspect the artifact as a whole:

- Does the reading flow make sense from page to page?
- Are story sections and missions visually distinguishable?
- Does the learner know when to stop, solve, use hints, and continue?
- Are repeated components consistent?
- Does the visual treatment have middle-grade appeal without becoming distracting or inaccessible to the current learner?
- Does the artifact still reinforce **Path before answer**?

## QA record

For each production artifact, record at least:

- total page count rendered and inspected;
- defects found during the first inspection;
- pages re-rendered after correction;
- confirmation that corrected pages and affected neighbors passed reinspection;
- confirmation that the complete final sequence passed visual review;
- validation of all problem-critical diagrams against the written specification.

The QA record may live in production notes, a pull request, or the delivery report. It does not need to appear inside the learner-facing PDF.

## Automated guardrails

Where the production system supports it, add preflight checks before rendering:

- calculate actual text height against available region height;
- fail generation instead of allowing text overflow;
- reserve separate non-overlapping regions for text and illustrations;
- enforce minimum font sizes;
- validate that required writing regions meet minimum dimensions;
- keep functional diagrams within defined bounds.

Automated checks do not replace visual inspection. They reduce obvious defects; the rendered-page QA pass remains mandatory.

## Release status

A learner-facing artifact should be described internally as one of:

- **Draft — not QA inspected**
- **QA failed — revision required**
- **QA passed — ready to present**

Only **QA passed** artifacts should be presented as finished work.
