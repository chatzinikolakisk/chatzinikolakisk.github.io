---
layout: post
title: "Define the End State and Shut Up"
date: 2026-05-04 10:00:00 +0000
categories: work
---

Someone gave my team an ultimatum on a PHP version upgrade. "Either today or Monday." A deadline that was less of a deadline and more of a threat. I heard about it a week later, in a retro. Nobody had asked me what to do. Nobody had escalated. Nobody had panicked.

I sat there listening to them reconstruct the story and felt something I'm still processing: pride, yes, but also a strange kind of vertigo. My team had used a principle I'd been teaching them for months, applied it under real pressure, and I hadn't been in the room.

## The hundred-page document

It started about a month earlier, in a meeting about engineering standards.

We'd been handed a comprehensive document. Seven sections. Dozens of pages. Coding conventions, architecture principles, review processes, deployment practices. It was meant to be the thing that unified our engineering teams across multiple products.

I read it and my first reaction was: this is a textbook pretending to be a standard.

The content wasn't wrong. Most of it was thoughtful. The problem was that nobody could tell me which parts were actual requirements and which parts were one person's preferred way of working. A junior engineer reading this document would have no idea what was mandatory and what was aspirational. (A senior engineer, honestly, wouldn't finish it.)

I told the group: "If this is a hundred, we need something at twenty."

What followed was a conversation about how to define standards that people would actually follow. The position I kept coming back to was almost embarrassingly simple: define the end state, shut up about the path.

Tell teams what must be true. Maybe ten things. Non-negotiable, short enough that everyone reads them, strict enough that nobody escapes them. Not "good test coverage." Something like: every production change has a rollback path. Every service has a named on-call owner. Every bug fix references the bug. Things you can hold up against an artifact and check, yes or no.

Don't tell them how to get there. The maturity tiers, the migration plans, the per-team baseline assessments, the enforcement timelines: in this context they were substituting for trust. If you have to design a compliance system to make people follow your standard, the problem is probably not the people.

The litmus test I keep coming back to is what a stranger would extract from the artifact. Take a document, a process, a decision. Imagine a senior engineer arriving in three months who wasn't in any of the conversations. What do they get from the written thing? If the answer is "nothing clean," you've defined the path, not the end state.

## What it looks like when it travels

A few weeks after the standards meeting, a different team was handed the PHP8 ultimatum I opened this post with.

Today or Monday. Take it or leave it. The kind of pressure that, six months earlier, would have arrived in my inbox as an escalation before lunch. This time it didn't. The team's most experienced engineer chose Monday on the call to buy thinking time, then brought it back to the team. They mapped the actual work, identified the risk windows, drafted a counter-proposal, and went back with it as a group. They didn't argue against the upgrade. They argued against the date. They won.

I learned about it in a retro a week later. Not because they wanted credit. Because someone was reflecting on what they'd done well.

Define the end state (we'll upgrade PHP, we're not refusing). Let the team figure out the path (here's the date, here's why, here's the plan).

The way they did it was not how I would have done it. Mine would have been more political. Mine would have been more diplomatic. Mine would have been worse, actually. They went straighter at the problem because they didn't have the political muscle memory I do. The fact that their way wasn't my way is the feature, not the bug.

## The part that made me uncomfortable

Here's what nobody tells you about "define the end state and let teams move freely": you have to actually let them move freely.

That sounds obvious. It isn't.

When the team came back from that PHP8 conversation with their counter-proposal, my first instinct (which I'm not proud of, but I'm being honest) was to wonder whether they'd pushed back the right way. Whether the tone was correct. Whether the timing was optimal.

And then I caught myself. The whole point of defining the end state is that you release control over the method. You don't get to specify the destination and then backseat-drive the journey. If the team arrived at the right outcome, using their judgment, in their own way, you don't get to have an opinion about the choreography.

This is where the principle stops being an intellectual exercise and becomes a test of character. Do you actually trust the people you manage? Not in the abstract "I believe in my team" way. In the concrete "they handled it without me and I don't get to second-guess how" way.

I've been managing engineers for years. I'm still working on this.

## Where it breaks

The same week one team was pushing back on external pressure with confidence and autonomy, a different team, the one with the newest leadership, was still figuring out the basics. In a retro, an intern said something that stopped the room: "I look at us and I don't feel like we're a team. Everyone works on different things. People feel like strangers."

That took guts to say. And it was true. This was a team where the end state had been defined (ship integrations, hit OKRs, build capability) but the path hadn't been walked yet. You can't tell a team to move freely when they haven't figured out how to move together.

"Define the end state" assumes a baseline. People know each other well enough to collaborate, trust each other enough to disagree, and have enough shared context to make independent decisions that don't contradict each other. For one of my teams, that baseline was rock solid. For another, it was still being built.

The temptation, when the philosophy doesn't work immediately, is to add process. Build tiers. Create checklists. Impose timelines. The same reflexes I'd rejected in that hundred-page document, suddenly attractive again now that the discomfort is mine.

But the answer isn't more process. It's patience. The intern who named the identity gap did something more valuable than any migration plan: he made the problem visible. Now the team can work on it. In their own way. At their own pace.

Define the end state. Even when the end state is "become a team."

## The thing I keep relearning

"I look at us and I don't feel like we're a team."

I keep coming back to that sentence. Not because it's elegant. Because it's the one moment all week where the path got named honestly, and the only person who could have named it was the one standing on it.

That's the end state, actually. Not pushing back on ultimatums. Not winning the timeline. The end state is a team that tells you the truth about itself, before you get to.

I'm still learning to shut up about the path long enough to hear it.
