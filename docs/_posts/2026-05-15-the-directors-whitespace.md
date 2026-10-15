---
layout: post
title: "The Director's Whitespace"
date: 2026-05-15 10:00:00 +0000
categories: work
---

At 12:18 on a Tuesday, I used a 45-minute gap between meetings to pair-review already-merged validator and exception code with a mid-level engineer. The feature was live and working. We still spent the hour reading handlers together, arguing about why a generic catch-all should catch a specific exception, and trimming database setup from unit tests.

Management books tell directors to stay technical by blocking out a mythical "maker day." Those days never survive a director's calendar. What survives are the cracks between meetings, and choosing code over chat when one opens up.

## Plumbing and pair reviews in the cracks

Thirty-to-sixty-minute calendar cracks are too short for features, which is why most directors stop trying. They fit interruptible work: CI plumbing and post-merge reviews. Two weeks earlier, I used a few calendar gaps to migrate a CI pipeline and discovered our static analysis check had been silently passing for months. A misconfigured step returned a zero exit code without scanning a file. Every dashboard was green, so nobody looked until I wandered through the plumbing.

The Tuesday pair review did different work. Reviewing shipped code without a release deadline lets you debate design instead of policing style. Near the end, I told him: "My collaboration with you will have succeeded if, whenever you next update your CV, you have more to write." He now leads the architecture for his squad's next major integration, and those validator patterns show up across the team's PRs unprompted.

## What the silence still needs from you

Those calendar cracks only exist because my three teams now ship 25 PRs and 50 tasks a day without escalating. With that reclaimed capacity, my job shifts to the two things autonomous teams do not build for themselves.

First is outward legibility and goal ownership. To me, a quiet week means the structure is holding; to a new VP in week one, that silence looks like a data void. And when 359 tasks move in two weeks while I am the only one asking if our OKRs are wired up, execution has drifted from direction. I had to coach my leads to broadcast delivery and risks upward, and to own whether the roadmap works, not just whether it ships.

Second is naming the product-identity question ("are we one product or two?") hidden underneath circular architecture debates. When rooms loop for months on mobile frameworks or shared components, the blocker is rarely technical. Once leadership named a unified suite model (shared backend, subscription-gated UI), months of technical arguments resolved in five minutes.
