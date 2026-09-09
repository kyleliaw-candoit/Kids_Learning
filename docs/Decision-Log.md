# Design Decision Log

This file records important design choices and—more importantly—the reason each choice was made.

## 2026-09-07 — Define the project around general problem solving

**Decision:** The project will focus on reasoning, exploration, and problem solving rather than subject-specific procedures.

**Why:** A learner may know that a school problem is “a subtraction problem” without understanding why subtraction represents the situation. The project aims to build the ability to construct a method from understanding.

---

## 2026-09-07 — Keep math light and reasoning moderately challenging

**Decision:** Early missions should use manageable calculations while asking for meaningful reasoning.

**Why:** Difficult computation would compete with the mental capacity needed to understand, plan, explore, and revise.

---

## 2026-09-07 — Protect productive struggle with a hint ladder

**Decision:** Provide optional progressive hints rather than immediately explaining how to solve the problem.

**Why:** The learner needs the experience of figuring something out, but extended confusion can produce paralysis rather than useful struggle.

---

## 2026-09-07 — Recognize process, including unsuccessful attempts

**Decision:** Positive feedback should acknowledge useful thinking moves even when the final answer is initially wrong.

**Why:** Trying, checking, discovering that an approach does not work, and revising are central components of real problem solving.

---

## 2026-09-07 — Introduce Remy the Raccoon as a thinking sidekick

**Decision:** Use a playful animal mascot throughout the missions.

**Why:** A recurring character can make the activity feel safer and more game-like. The mascot models curiosity rather than authority.

---

## 2026-09-07 — Make Remy sillier and more expressive

**Decision:** Increase Remy's personality and simplify the cartoon style.

**Why:** The learner enjoys silly cartoon characters. Strong personality improves engagement; simpler lines and flatter colors keep the character visually clean and reusable.

---

## 2026-09-07 — Put “Show Your Path” before “Your Answer”

**Decision:** The debrief will ask for the reasoning path before asking for the final answer.

**Why:** The order should reinforce the project's value system: the path is the main learning artifact; the answer comes after.

---

## 2026-09-07 — Reduce visual dominance of headings, problem text, and mascot

**Decision:** Beginning with Problems 4–5, use smaller headers, smaller problem-statement text, and make Remy about 10% smaller.

**Why:** Preserve a playful visual identity while giving more space and visual priority to the learner's own thinking and writing.

---

## 2026-09-07 — Delay creation of a master template

**Decision:** Prototype multiple problems before standardizing the format.

**Why:** The format should be based on observed learner behavior, not assumptions made before real use.

---

## 2026-09-07 — Use one PDF per problem

**Decision:** Each problem will have one printable PDF containing student pages plus a grown-up guide.

**Why:** It is simpler to manage and keeps facilitation guidance with the corresponding activity.

---

## 2026-09-07 — Classify each Thinking Mission by one Primary Dimension and up to two Secondary Dimensions

**Decision:** Every future Thinking Mission receives exactly one Primary Thinking Dimension and zero to two Secondary Thinking Dimensions.

**Why:** This creates a usable capability map for curriculum planning. It allows the mission library to be balanced intentionally, makes gaps visible, and supports future requests such as creating more practice in elimination, working backward, representation, or strategy flexibility without reducing missions to school subjects.

---

## 2026-09-07 — Use short self-contained stories to unlock Thinking Missions

**Decision:** Prototype a gamification layer in which a short mystery/adventure contains roughly five Thinking Missions. Completing each mission unlocks the next meaningful clue, scene, twist, or reveal.

**Why:** Story progression can provide a stronger intrinsic reason to continue than generic points or worksheet completion. The learner solves the next mission partly because they want to discover what happens next.

---

## 2026-09-07 — Prefer chapter-length cases over one long continuous novel

**Decision:** Each story-integrated case should normally have its own beginning, mystery/adventure, reveal, and ending rather than depending on one large continuous plot.

**Why:** Short cases are easier to create, test, pause, revise, and vary. They reduce continuity burden and allow lessons from one case to improve the next without committing the project to a large story architecture.

---

## 2026-09-07 — Story unlocks must be meaningful, not filler rewards

**Decision:** Each mission should unlock an actual story development: a clue, location, suspect, twist, funny complication, reveal, or finale step.

**Why:** If story progression merely says “good job, now do another problem,” the narrative becomes cosmetic gamification. The story itself should be something the learner wants to continue.

---

## 2026-09-07 — Keep story and education as separate but cooperating design layers

**Decision:** The educational architecture determines thinking dimensions, difficulty, hints, checking, and solution paths; the story architecture determines characters, suspense, humor, clues, and reveals. Connect them naturally when possible, but do not sacrifice a strong reasoning task simply to make it fit the plot.

**Why:** This preserves educational quality and makes the system reusable across different stories, genres, and future learners.

---

## 2026-09-07 — Keep badges as a complementary layer, not the primary reward

**Decision:** Continue using badges that recognize thinking behaviors, while treating story progression as the main chapter-level reward.

**Why:** Badges make invisible reasoning behaviors visible and reinforce process recognition, but story curiosity may be a stronger sustained motivator than accumulating points. The badge system should never become a punitive score for correctness.

---

## 2026-09-07 — Require a rendered-page quality inspection before presentation

**Decision:** Every learner-facing artifact must pass a dedicated production QA gate after generation and before it is presented as finished work. The complete PDF/document must be rendered page-by-page, every rendered page must be visually inspected, defects must be corrected, and affected pages must be re-rendered and re-inspected before release.

**Why:** Text overflow, text/graphic collisions, clipping, weak illustration semantics, inaccurate functional diagrams, and age-inappropriate visual quality are production defects rather than legitimate curriculum experiments. A mandatory rendered-page review catches issues that code generation and source-level inspection can miss.

The canonical process is documented in `docs/Production-Quality-Gate.md`.

---

## 2026-09-07 — Separate character simplicity from illustration richness

**Decision:** Keep recurring characters such as Remy visually simple, iconic, and consistent while allowing story environments and mission illustrations to be substantially richer and more engaging for approximately nine-year-old learners. Functional puzzle graphics must remain precise and easy to read.

**Why:** Simple character design supports recognition and reuse, but overly simple scene graphics can feel babyish or placeholder-like. The visual standard is: **simple characters, richer worlds, clear puzzle signals.**

---

## 2026-09-07 — Calibrate future backgrounds below focal subjects

**Decision:** Use the approved medium-complexity hand-drawn treatment for Remy, recurring characters, and story-critical objects. Make future backgrounds simpler, quieter, and less detailed than those focal subjects by reducing secondary props, contrast, texture, and color variation.

**Why:** The Case 01 Version 002 illustrations were accepted, but their environments were sometimes more detailed than expected and could compete with the characters and clues. A nine-year-old should first notice the character, action, or important object, then understand the environment. The updated production rule is: **medium-detail characters and key objects; quieter backgrounds; clear puzzle signals.**

The complete standard is documented in `docs/Illustration-Production-Standard.md`.

---

## 2026-09-07 — Require a final full-sequence QA pass after corrections

**Decision:** When the first rendered-page inspection finds defects, correct them, re-render the affected pages and any adjacent pages influenced by reflow, then render and inspect the complete final PDF again before delivery. Record the page count, defects, corrections, and final result.

**Why:** An affected-page recheck confirms the local correction, while a final full-sequence pass confirms that the delivered artifact—not an earlier intermediate build—is the version that passed QA.
