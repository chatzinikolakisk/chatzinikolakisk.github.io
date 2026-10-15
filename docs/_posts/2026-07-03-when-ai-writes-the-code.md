---
layout: post
title: "When AI Writes Half the Code, What Happens to Review?"
date: 2026-07-03 10:00:00 +0000
categories: work
---

Midway through a 54-minute strategy meeting on a new natural-language reporting feature, someone asked about end-to-end testing. Would we validate the AI agent's behavior against real conditions in CI before release?

A senior engineer answered in five words: "It would be too expensive." Nobody forgot the quality gate. We waived it as a cost decision and moved on.

Across our engineering organization, 54% of shipped code is now AI-authored, putting us in the 86th percentile of our benchmarks. At that volume, our old habits around authorship and review are breaking in two opposite ways at once.

## The open-book exam

A few weeks earlier, an engineer voiced a quiet doubt in a retrospective: "I do the work. But most of it is AI. I don't feel like I've done something wow." Meanwhile, teams without that doubt fail in the opposite direction. At a leadership sync, engineers argued that humans will stop reviewing AI code altogether, right before someone pointed to a 7-line AI script that merged without scrutiny and triggered 15 critical vulnerability alerts.

A teammate in that retrospective offered the frame I use now: an open-book exam. Having the book never made the test easy. You still have to know which formula applies, where it breaks, and which 10% of the output is load-bearing while the other 90% is plausible noise. Because you cannot see your own taste while using it, I ran a two-person live-prompting workshop on a real problem. Watching themselves sharpen prompts, catch a subtle bug, and reject a bad abstraction put their own judgment back on the table.

## Two thousand arguments as a reviewer

Engineers who say human line-by-line review does not scale to doubled output are doing honest math. When PR volume doubles, reviewers tire out on mechanical conventions and miss structural risks, leaving nobody able to answer who owns the 3am alert when a service ships without a dependency map or an E2E test.

Instead of giving up on review, one of my teams built an AI reviewer grounded in their own codebase. They trained it on roughly 2,000 of their historical PRs and review threads, paired with a self-updating findings checklist that evolves as the team rejects noisy rules or catches new bug classes. A reviewer trained on two thousand of your own arguments clears the mechanical noise so humans can own what a model cannot: dependencies, failure modes, and accountability.
