---
layout: post
title: "Permission to Explore"
date: 2026-04-05 10:00:00 +0000
categories: work
---

One of my engineers apologised this week. Not for shipping a bug, not for breaking production, not for missing a deadline. They apologised for writing code.

Exploratory code. A draft PR. The kind of thing you push to a branch because you're playing with an idea, testing whether a new abstraction might clean things up. Not merged. Not even intended for review yet. Just thinking out loud, in code.

A senior colleague from another team saw it and decided it needed governance. Where's the ADR? Why wasn't this discussed? Who approved this approach?

Let me be clear: there was no ADR because there was no decision. There was an experiment. A draft. A conversation that hadn't happened yet because the idea wasn't fully formed.

But suddenly we were in a meeting about it. And when I said, "honestly, this doesn't make me feel motivated," the response was: "your problem."

## When process protects the powerful

I've been thinking about that moment all week.

Engineering governance exists for good reasons. ADRs, architecture reviews, technical standards: these are tools for alignment. They protect teams from costly surprises, keep codebases coherent, and give everyone a voice in decisions that affect them.

But like any tool, governance can be picked up by anyone for any purpose. And when a senior person uses process language to shut down a junior team's exploration, something breaks. Not the code. The team.

Here's the pattern I keep seeing: the same people who make architectural decisions unilaterally (framework choices, ORM adoption, infrastructure changes) suddenly become governance enthusiasts when someone else's team tries something small. The ADR process, meant to be a tool for collaboration, becomes a gate. And gates have gatekeepers.

The question isn't whether process matters. It does. The question is: who gets to explore without a permission slip, and who gets cross-examined in a public channel for writing draft code?

## The thing about initiative

I manage three engineering teams. My main goal, the one I actually care about, is helping each team stand on their own feet. Engineering capability, management maturity, the confidence to make decisions without looking upstairs first.

That goal lives and dies in moments like this one.

When a team takes initiative and gets treated like they've committed a governance violation, they learn something. Not the lesson you intended ("follow the process"). The real lesson: don't try new things unless you've pre-cleared them with someone more senior. Don't push exploratory code. Don't think out loud in a PR description. Play it safe.

And safe teams don't build anything interesting.

I watched my engineer apologise for unfinished work in a draft PR, and I thought: this is the exact opposite of what I'm trying to build. I want teams that experiment, that push messy ideas, that argue about abstractions before they're polished. I want the kind of creative friction that only happens when people feel safe enough to be wrong.

What I got instead was a team in defensive posture, explaining themselves for the crime of having an idea.

## "Your problem"

The dismissal stung more than the process debate.

I've been an engineering leader long enough to know that not every emotional response is valid, and not every frustration deserves accommodation. Sometimes you're wrong, and someone telling you so isn't an attack. It's a gift.

But there's a difference between disagreeing with someone's approach and dismissing their experience of the interaction. "This doesn't motivate me" is information. It's a signal about how your process, your tone, your approach is landing with the people who have to live inside it. Responding with "your problem" doesn't resolve the disagreement. It just ends the conversation.

And when conversations end like that, they don't really end. They go underground. They become the thing you talk about in DMs, in 1:1s, in the car on the way home. They become the reason someone stops raising concerns in meetings, because what's the point?

I don't have the high ground here, by the way. I've been the person who dismissed someone's concern because I was sure I was right. I've shut down conversations I should have stayed in. You don't get to this level without having been, occasionally, the problem.

But knowing that doesn't make it easier to watch your team absorb the hit.

## Constraints, not methods

Here's the philosophy I keep coming back to, the one I try (and sometimes fail) to live by: be tight on the what, silent on the how.

Define the end state. Be crystal clear about what needs to be true when the work is done. Quality standards, security requirements, performance targets, customer commitments: these are non-negotiable. Write them down. Make them specific.

Then shut up about the path.

I gave this feedback just this week on an engineering standards document someone was drafting. Seven documents covering every aspect of how to write code. My response: make it one. A short, strict spec of what must be true. Rules, not methods. And then let teams figure out how to get there in their own way, on their own terms.

This isn't soft management. Constraints are hard. "Every API endpoint must have contract tests" is harder to live up to than "follow these 14 coding guidelines." Constraints expose gaps ruthlessly. Methods let you hide behind compliance.

But constraints also create space. Space for teams to experiment. Space for draft PRs and exploratory code and half-baked abstractions that might turn into something brilliant or might get quietly deleted. Space for the kind of messy, creative engineering work that actually moves things forward.

Governance that prescribes the method instead of the constraint isn't alignment. It's control.

## The messy middle

I'm writing this on a Sunday morning, a few days after the incident, and I still don't have it fully sorted.

Part of me knows the senior colleague had a point. Communication matters. If you're going to introduce a new pattern, even experimentally, a heads-up in Slack costs nothing. The PR description could have been clearer about intent. My team could have been more proactive about signalling "this is exploratory, not a proposal."

Part of me thinks I'm being too generous. When the response to "I feel demotivated" is "your problem," you're not dealing with a process gap. You're dealing with a power dynamic. And no amount of better PR descriptions fixes that.

And honestly? Another part of me wonders if I'd have reacted differently had the roles been reversed. If someone on another team pushed a draft PR that touched code I felt ownership over, would I have been curious or territorial? I'd like to think curious. But I've been territorial before. Most of us have.

What I do know is this: the next time one of my teams pushes a draft PR with a half-formed idea, I want them to feel like they did something brave, not something that requires an apology.

If that means I need to fight a few more battles upstream, so be it. Building teams that take initiative is messy work. You're not just coaching the team. You're negotiating the environment they work in. And sometimes the environment pushes back.

The best thing I can do right now is keep showing up. Keep pair-programming with my engineers, keep pushing for constraints over methods, keep making space for the exploratory work that nobody asks for but everyone benefits from.

And maybe, next time someone says "your problem," have a better answer ready than stunned silence.
