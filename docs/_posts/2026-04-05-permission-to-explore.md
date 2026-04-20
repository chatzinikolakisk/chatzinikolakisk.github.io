---
layout: post
title: "Permission to Explore"
date: 2026-04-05 10:00:00 +0000
categories: work
---

One of my engineers apologized this week. Not for shipping a bug, not for breaking production. They apologized for writing code.

Exploratory code. A draft PR, the kind of thing you push to a branch because you're playing with an idea, testing whether a new abstraction might clean things up. Not merged, not even intended for review yet. A senior colleague from another team saw it and escalated: where's the ADR? Why wasn't this discussed? When I said the interaction felt demotivating, the response was two words: "your problem." The incident passed. The lesson my team took from it hasn't.

## When process becomes control

Engineering governance exists for good reasons. ADRs, architecture reviews, technical standards: these are tools for alignment. They protect teams from costly surprises and give everyone a voice in decisions that affect them.

But governance can be picked up by anyone for any purpose. And when a senior person uses process language to shut down a junior team's exploration, something breaks. Not the code. The team.

Here's the pattern I keep seeing: the same people who make architectural decisions unilaterally (framework choices, ORM adoption, infrastructure changes) become governance enthusiasts when someone else's team tries something small. The ADR process, meant to be a tool for collaboration, becomes a gate. And gates have gatekeepers.

The question isn't whether process matters. It does. The question is: who gets to explore without a permission slip, and who gets cross-examined for writing draft code?

## Constraints, not methods

Here's the philosophy I keep coming back to, the one I try (and sometimes fail) to live by: be tight on the what, silent on the how.

Define the end state. Be crystal clear about what needs to be true when the work is done. Quality standards, security requirements, performance targets, customer commitments: these are non-negotiable. Write them down. Make them specific.

Then shut up about the path.

I gave this feedback just this week on an engineering standards document. Seven documents covering every aspect of how to write code. My response: make it one. A short, strict spec of what must be true. Rules, not methods. Then let teams figure out how to get there in their own way, on their own terms.

This isn't soft management. Constraints are hard. "Every API endpoint must have contract tests" is harder to live up to than "follow these 14 coding guidelines." Constraints expose gaps ruthlessly. Methods let you hide behind compliance.

But constraints also create space. Space for draft PRs and exploratory code and half-baked abstractions that might turn into something brilliant or might get quietly deleted. Space for the kind of messy, creative engineering work that actually moves things forward.

Governance that prescribes the method instead of the constraint isn't alignment. It's control.

## What I want to build

I manage three engineering teams. My main goal is helping each team stand on their own feet: engineering capability, management maturity, the confidence to make decisions without looking upstairs first.

That goal lives and dies in moments like the one that started this post. When a team takes initiative and gets treated like they've committed a governance violation, they learn something. Not the lesson you intended. The real lesson: don't try new things unless you've pre-cleared them with someone more senior. Play it safe.

Safe teams don't build anything interesting.

I don't have the high ground here. I've been territorial about code I felt ownership over. I've shut down conversations I should have stayed in. You don't get to this level without having been, occasionally, the problem.

But knowing that doesn't change what I'm building toward. The next time one of my teams pushes a draft PR with a half-formed idea, I want them to feel like they did something brave, not something that requires an apology.

Define the constraints. Make them clear and hard. Then get out of the way. That's the job.
