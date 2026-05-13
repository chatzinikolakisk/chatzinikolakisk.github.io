---
layout: post
title: "The Rules Nobody Wrote Down"
date: 2026-04-24 10:00:00 +0000
categories: work
---

We were in a meeting about training budgets. Five engineering leaders and someone from L&D, trying to sort out why a junior engineer got conflicting information about whether they could attend a conference. One of us said they had to wait a year before being eligible. L&D said three months. Both believed they were right.

Turns out, neither was reading from the same page. Because there was no page.

## The discovery

Our L&D lead pulled up the actual company policy and started going through it. One-year waiting period before training budget eligibility? Not company policy. Maximum three people per conference? Not company policy. Mandatory presentation after attending? Not company policy.

These were R&D-specific decisions, made at some point by someone, passed down through conversations and Slack messages and "I think the rule is..." until they felt as solid as anything in the employee handbook. One person's preferences, never documented, became institutional truth.

The room went quiet for a moment. I remember one of us saying, "This is new information for us." Which is a polite way of saying: we've been operating under rules that don't exist for years, and nobody thought to check.

## How phantom policies work

Here's how it happens. Someone senior makes a practical decision in a specific context. Maybe they had ten interns that year and the budget was tight, so they said "let's hold off on conferences for new hires." Reasonable. Context-dependent. Temporary.

But nobody writes down the context. The decision gets relayed as a rule. The rule gets relayed as policy. Within a year, managers are citing it in 1:1s as if it came from HR. Within two years, people who joined after the decision was made enforce it more rigidly than the person who made it, because they never knew it was a judgement call. They think it's a wall. The original decision-maker has probably forgotten they said it.

The training budget rules were a textbook case. We consistently spent only about 60% of the allocated training budget each year. The phantom policies were doing their job: discouraging claims that would have been perfectly valid under the actual policy. And then, because the budget was underspent, Finance cut it the following year. Underutilisation justified reduction, which justified stricter phantom controls, which justified further underutilisation. The fiction became more real over time.

Phantom policies are indistinguishable from real ones until someone checks. They carry the same authority. They shape the same behaviours. People get reprimanded for violating them. New hires get onboarded into them.

## It's not just budgets

Once I saw the pattern, I started seeing it everywhere.

A few weeks later, I was in a discussion about engineering standards. Someone had written a comprehensive standards document. Seven sections. Dozens of pages. Coding conventions, architecture principles, review processes, deployment practices.

The problem wasn't the content. The problem was that nobody could tell me which parts were actual requirements and which parts were one person's preferred way of working. The document mixed enforceable minimums with architectural philosophy with training material, all presented with the same weight. Everything looked like policy. Nothing was labelled as opinion.

So when one of my engineers, let's call them M, proposed an event-driven approach for a new integration, the document was no help. There was nothing on event-driven patterns. Nothing on broker selection. The standard was silent, and into that silence walked the phantom policies. The first review meeting questioned whether event-driven was "really our pattern." The second meeting questioned whether the proposed broker fit "our way of doing things." Three weeks in, M presented essentially the original design back to the same room, and it was approved. Same proposal. Same approver. Different week.

The only thing that had changed was that a senior architect had, between meetings two and three, said in a corridor conversation that the approach "made sense to him."

M's observation, which I haven't been able to shake: "It's not what you say, it's who says it." That's what happens when the written standard goes quiet. Authority fills the gap.

That's what phantom policies do at their worst. When the rules are unwritten, enforcement becomes personal. The same exploratory work that's celebrated when it comes from one direction triggers a governance review when it comes from another. Not because anyone is being deliberately unfair (usually). But because without a written baseline, every decision about what needs approval and what doesn't is made on vibes.

## The audit that called our bluff

Then a SOC2 auditor walked in and asked a very simple question: "Please provide evidence depicting that a documented Code Release Lifecycle is in place."

Not "do you do good work" but "can you prove it to someone who wasn't in the Slack channel when you decided how to do it." Without an artifact, the answer is no. Functionally invisible is functionally non-existent.

We have release processes. Canary deployments. CI pipelines. Rollback procedures. Teams that ship reliably. What we didn't always have was the artifact: the written thing that says "this is how we do it" in a way that someone outside the organisation could point to and verify.

The auditor asked the same question about bug resolution. We fix bugs. We don't always document that we did, or how, or against which definition of "fixed." For anyone who joins next year, or audits you this year, or tries to understand why two teams do the same job differently despite supposedly following the same standards, that gap is the whole problem.

## What I'm doing about it (slowly)

I committed to drafting ten baseline engineering items for our organisation. Not a manifesto. Not seven sections of aspirational architecture principles. Ten things. Non-negotiable. Written down. Short enough that everyone reads them, strict enough that nobody escapes them.

To make it concrete: things like "every production change has a documented rollback path," "every service has a named on-call owner," "every bug fix references the originating issue." Not "good engineering culture." Not "we value quality." Things you can hold up against an artifact and check, yes or no.

The philosophy is simple, and it's the same one I keep coming back to: define the end state, shut up about the path. Tell teams what must be true. Don't tell them how to get there. If a standard needs fifty pages of explanation to be understood, it's not a standard. It's a textbook masquerading as one.

The harder work is the cultural audit. Going through every rule we enforce and asking: is this written somewhere? If not, who decided it, and when, and does the context still apply? Most of the phantom policies I've found were reasonable when they were created. The problem was never the original decision. It was the failure to document it, revisit it, and eventually either formalise it or kill it.

I haven't finished this work. I probably won't for a while. Phantom policies are, by definition, hard to find. You don't know what you don't know until someone asks a question that exposes the gap, like a junior engineer who heard two different answers about conference eligibility, or an auditor who asked for a piece of paper we assumed existed.

## The uncomfortable bit

I have phantom policies too. Of course I do.

Somewhere in the way I manage my teams, there are preferences I've expressed once that became rules I enforce without remembering I made them up. Communication norms I set through behaviour rather than words. Expectations I hold people to that I've never articulated clearly enough to be challenged.

The question isn't whether your organisation has phantom policies. It has them. Every organisation does. The question is whether you're willing to go looking for them before something else does.

Write it down. If it's worth enforcing, it's worth documenting. And if it's not worth documenting, maybe ask yourself whether it's really worth enforcing at all.
