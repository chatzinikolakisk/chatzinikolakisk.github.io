---
layout: post
title: "When AI Writes Half the Code, What Happens to Review?"
date: 2026-07-03 10:00:00 +0000
categories: work
---

Somewhere in the middle of a 54-minute strategy meeting, a senior engineer said something I haven't been able to shake.

We were discussing a new AI feature: natural language reports over read-only queries, genuinely useful product work. The conversation had been running through infrastructure costs, data compliance, token authentication mismatches, and multi-region complexity. Then someone asked about end-to-end testing. Would we validate the AI agent's behaviour against real conditions in CI before releasing?

The answer: "It would be too expensive."

The end-to-end test wasn't missing because nobody thought of it. It was explicitly ruled out as a cost decision. The quality gate was waived, and everyone in the room accepted that and moved on.

Across our engineering organisation, 54% of shipped code is now AI-authored, putting us in the 86th percentile of our benchmarks. More than half of our production code is no longer written by a human sitting with their hands on a keyboard. And at that volume, our old assumptions about authorship and review are breaking in two opposite ways at the same time.

## The open-book exam

A few weeks before that strategy meeting, an engineer on one of my teams said something quieter in a retrospective.

"I do the work. But most of it is AI. I don't feel like I've done something wow."

He wasn't fishing for reassurance. He was naming a doubt a lot of thoughtful engineers are carrying in private. You write the prompts, you read the output critically, you catch the wrong turns, you ship something that works, and then you sit there wondering whether any of it was actually you.

Another engineer on his team handed me the frame I've used ever since: "Remember open-book exams? You could still feel like the book helped too much. But you still had to know what to look for."

Open-book exams were never easy because you didn't have to memorise the formula. They were hard because knowing which formula applied, when it broke down, and why this approach worked instead of that one was still entirely on you. The book just let the examiner ask harder questions.

AI coding is an open-book exam at an absurd scale. The book writes its own chapters and argues for its own answers. Someone still has to know what the question is. Someone has to know which ten percent of the output is load-bearing and which ninety percent is plausible noise.

From the inside, exercising that judgment feels like nothing at all. Deciding the model is confidently wrong feels like a shrug. You cannot watch your own taste while you're using it.

Telling an engineer "the work is still yours" doesn't fix that. Reassurance is the management equivalent of "looks good, approved": it costs nothing and changes nothing. Instead, I ran a short workshop with two of the engineers, prompting an AI on a real problem out loud while I watched. Not to prove the tool works, but to make them watch their own judgment happen in real time: the question being sharpened, the subtle bug caught, the bad abstraction rejected. The skill they swore they weren't using was sitting right on the table between us.

## When the review layer evaporates

The uncomfortable flip side is what happens when teams stop feeling that doubt.

At an engineering leadership meeting earlier this year, a senior engineer stated the new reality plainly: "Once deployed, no one here will re-write code or re-read or review code" for AI-generated systems. Another added: "Let the agent decide what's right; document assumptions; accept that humans won't review code, so documentation for agents is what matters."

Documentation for agents, not engineers.

At the same meeting, someone shared a concrete data point: a small Python script, five to seven lines long, had triggered twenty vulnerability flags in our dependency scanner, fifteen of them rated critical. Five to seven lines. Written by AI, merged without human scrutiny, and caught only after the automated scanner ran.

That isn't a story about AI writing bad code. Humans write bad code too. It's a story about the evaporation of a social contract.

The safety model for software has always assumed a human backstop. Code review and QA were inconsistent, sure, but the social agreement held: a person will look at this and own the call. Bugs in reviewed code are failures. Bugs in unreviewed code are just weather.

In that same natural language reports session, a senior staff engineer put his finger on the gap: "I've seen nothing in writing. I have not seen a map of dependencies." He was talking about system architecture, but the sentence applied just as well to accountability. When an AI-assisted service lands in production without a formal team handoff, when the E2E test is too expensive to run, and when the PR is too large for a human to read line by line, who owns the 3am alert?

## Scaling taste instead of skipping review

The engineers who say human line-by-line review doesn't scale to AI output volumes aren't being reckless. They're doing the maths. You cannot double code volume with AI and expect the same manual PR review habits to hold the line.

But "nobody will review the code" is the wrong conclusion. If the bottleneck is that human reviewers get fatigued checking mechanical conventions while missing structural risks, then the review layer has to evolve the same way the coding layer did.

A few weeks after those meetings, one of my teams built the answer from the bottom up. Instead of waiting for a top-down governance policy or giving up on code review, they built an AI code review agent grounded in their own codebase. They mined roughly 2,000 of the team's historical pull requests and review threads to extract the patterns, architectural boundaries, and failure modes our own senior engineers actually care about. Then they wired it into a self-updating findings checklist that evolves as the team rejects noisy suggestions or uncovers new classes of bugs.

That changed the conversation immediately. A generic off-the-shelf bot nags you about style rules you don't care about. A reviewer trained on two thousand of your own team's arguments knows how your services talk to each other, where your test suite lies, and which shortcuts burned you last quarter.

It doesn't replace the human in the loop. It clears the brush so the human reviewer can spend their attention on the part a model still cannot own: whether the dependencies make sense, whether the failure mode is acceptable, and who is accountable when it ships.

The open-book exam still belongs to the engineer. We just needed a better way to grade it.
