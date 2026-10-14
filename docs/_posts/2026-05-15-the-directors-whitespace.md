---
layout: post
title: "The Director's Whitespace"
date: 2026-05-15 10:00:00 +0000
categories: work
---

At 12:18 on a Tuesday afternoon, I was pair-reviewing production code with one of my engineers. Walking through event-driven architecture, validators, service handlers, exception catching. Real engineering. Not rubber-stamping a PR; actually reading code, questioning design decisions, suggesting alternatives, catching a catch-throwable that should have been a catch-specific-exception.

My calendar that day had a gap. An hour between a planning session and a 1:1. That's when my engineer happened to be online and the code happened to be ready, so that's when we sat down together.

This is not what the advice books mean by "staying technical." The advice books imagine maker days. Blocked-out Fridays. Quarterly hackathons. Something on the calendar with a label.

This was an hour I could have spent on Slack, or catching up on emails, or pre-reading for the next meeting. Instead I spent it reading validators with a mid-level engineer. And that choice, more than any blocked-out maker day, is what I want to write about.

## The CI migration nobody noticed

Two weeks before the pair review, I merged a CI migration for one of our products. Moved the PHP pipeline from self-hosted cloud runners to managed CI runners. Two PRs, nothing glamorous. The kind of infrastructure work that makes everything slightly cheaper and slightly faster and that nobody ever celebrates.

I'd been poking at it between meetings. Not during a blocked-out maker day. Not during a dedicated sprint. Between meetings. The way you check your phone while waiting for coffee, except instead of scrolling feeds, I was debugging why our static analysis check had been silently broken in CI for months.

That's the part that stuck with me. A static analysis tool the team relied on to catch code quality issues had been passing every build. Green checkmarks across the board. Except it wasn't actually running. The CI configuration was invoking it, getting a non-failing exit code from a misconfigured step, and moving on. Every PR that had passed "code quality checks" for the last several weeks had passed a check that wasn't checking anything.

I found it because I was in there doing plumbing. Nobody else was going to find it because nobody else had a reason to be in the CI configuration. The team had working pipelines. The dashboards were green. The problem was invisible to everyone who wasn't elbow-deep in YAML.

This is the argument for directors staying technical that nobody makes. Not "you need to stay sharp" or "you should understand what your teams build." Those are true but abstract. The concrete argument is: infrastructure has dark corners that only get illuminated when someone with enough context wanders through them for reasons unrelated to the original problem. And if the only people wandering through are the people who built it, you'll only find the problems they already know about.

## What the pair review was actually for

The review wasn't scheduled. A mid-level engineer on one of my teams had just shipped a significant feature: an automation framework with event-driven scheduling, domain-driven service isolation, and a validator abstraction layer. He'd been working on it for weeks. The code was already merged.

I didn't need to review it. It was done. Shipped. Working. But I wanted to understand it, and I wanted him to walk me through his thinking. Partly because the architecture was going to be the foundation for future work across the team. Partly because I'm nosy about code.

We spent an hour. I asked him why he'd used catch-throwable with an instanceof check instead of just catching the specific exception. I pointed out that his test classes were extending the database test case when half of them were pure unit tests, inflating the test suite's runtime and memory footprint. I asked him to explain the relationship between the scheduling service's dispatched event and the execution listener, because the connection wasn't traceable within a single repository.

He pushed back on some of it. Defended his choices. Explained constraints I hadn't considered. This is what pair review looks like when both people are actually engaged. Not "looks good, approved." Not "here are seventeen comments about naming conventions." Two engineers reading code together, disagreeing about exception handling.

Near the end, I told him something I'd been thinking about for a while. "My collaboration with you will have succeeded if, whenever you next update your CV, you have more to write."

He said: "Only this way will we learn and get better."

That exchange happened because I was in the code with him. Not managing him. Not coaching him in an abstract 1:1 about career development. Reviewing actual validators and actual service handlers and having actual technical disagreements. The CV conversation grew naturally out of a discussion about cyclomatic complexity and value objects, not from a performance review template.

## The gap that isn't a gap

Directors say they want to stay technical. Most don't. The honest version of why is that the calendar fills up, and the remaining time feels too fragmented for real work. You can't write a feature in the twenty minutes between a retro and a stakeholder call. So you stop trying, and "staying technical" becomes reading Hacker News and having opinions about architecture you haven't shipped in years.

What I've found, mostly by accident, is that the fragmented time isn't useless. It's just suited to different work. CI migrations. Config fixes. Dependency updates. Static analysis tuning. The kind of infrastructure improvement that takes thirty minutes of focused attention, can be interrupted without losing state, and compounds invisibly over weeks.

It's not glamorous. You're not going to write a blog post about upgrading a CI runner configuration. (Well.) But it is real engineering. You're reading real code, making real decisions, catching real problems. And the side effect is that you stay calibrated. When you're in an architecture review and someone proposes a service mesh, you know what a service mesh actually costs because you were in the deployment pipeline last week. When a team says "our CI takes forty minutes," you know whether that's fixable because you just fixed it somewhere else.

The prerequisite, and this is the uncomfortable part, is teams that can run without you. The pair review happened because I had a gap. I had a gap because nothing was on fire. Nothing was on fire because the team didn't need me to put out fires anymore. The infrastructure tinkering is a side effect of team maturity.

Every post I've written this year returns to this: help your teams stand on their own feet. What I hadn't realised until recently is that "their own feet" has a corollary for the manager. When they stand, you get to kneel. Get your hands dirty again. Not because the team needs it, but because you need it.

## The part most directors won't do

Most directors with a free hour wouldn't spend it pair-reviewing already-merged code with a mid-level engineer. They'd clear Slack. They'd answer the email backlog. They'd prep for the next meeting. They'd justify the choice by saying the meeting prep is higher-leverage, that the engineer doesn't need their time, that the code is already shipped so what's the point.

All of which is defensible. None of which is wrong, exactly. But the cumulative effect, over months and years, is a director who has not read a line of production code since they took the role.

The problem isn't time. The problem is that the instinct to be available, to clear inboxes, to prep for the next meeting, will eat every free hour you have. The maker-day fantasy assumes that if you blocked out a Friday you'd write code. You wouldn't. You'd spend the Friday catching up on the things you didn't do during the week, because that's what the instinct does. It reaches for the things that feel like work without requiring you to be vulnerable.

Sitting next to a mid-level engineer and asking him to explain his architecture is vulnerable. He might explain something you don't understand. You might suggest something naive. The conversation might surface that you're rustier than you'd like to admit. None of that happens when you're answering email.

The cracks in the calendar are not the problem. The instinct about what to do with them is.

## What I'm actually arguing for

Not maker days. Not "technical Fridays." Not any scheduled thing that becomes another calendar block to protect and eventually lose.

What I'm arguing for is permission. Permission to treat the cracks as legitimate work time. Permission to merge a PR between meetings without feeling like you're skiving. Permission to spend an hour on already-shipped code with an engineer who doesn't need you, and to count it as real contribution, not a guilty pleasure.

And, more importantly, the recognition that the cracks only exist when your teams don't need you. The technical work is both the reward for good management and the evidence of it. If your calendar is so full that you can't find fifteen minutes for a CI fix, the question isn't "how do I block out a maker day." The question is "why does every meeting need me in it."

I know the answer in my case. Not all of them do. I just haven't finished letting go.

## The CV test

That engineer I reviewed code with? He's now leading the architecture for his team's next major integration. The validator patterns we argued about have become the team's standard approach. The value object conversation is showing up in other engineers' PRs without anyone mandating it.

I didn't teach him those things. I taught him to care about those things, which is different. The teaching happened over months of 1:1s, pair reviews, technical arguments, and, yes, one afternoon where we disagreed about exception handling.

"My collaboration with you will have succeeded if, whenever you next update your CV, you have more to write."

Most managers measure success by what shipped. Features delivered, deadlines met, OKRs hit. And those matter. But there's a different yardstick that hits closer to why I do this job. If your direct report's resume looks the same after a year under your management, you built a product but not a person.

The implied trade-off is real. Sometimes the fastest path to shipping isn't the one that grows your people. The pair review wasn't efficient. It was an hour spent on code that was already merged and working. The CI migration could have been delegated. The static analysis fix could have been a ticket.

But the engineer who walks me through his architecture is different, afterward, from the engineer who submits it for async review. And the team whose director is in the codebase is different from the team whose director is in the org chart.

The director's whitespace is small. It lives in the cracks between meetings, in the hours that other directors would spend clearing Slack. It's not enough, and I'm working on making it bigger.

But it's real engineering. And it's where the teaching happens.
