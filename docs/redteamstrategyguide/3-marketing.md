# 3. Marketing & Promoting Red Team Services

_How to build awareness, trust, and demand for internal red teaming._

<p class="rtsg-meta">📅 Published August 19, 2026 &nbsp;·&nbsp; 🕒 {{READTIME}} min read</p>

<!-- prettier-ignore -->
!!! tip "Takeaways"
    - Internal marketing helps teams understand what red teaming is, why it exists, and how it can help them.
    - Greater awareness creates organic demand, giving red teams more opportunities from which to select high-impact work.
    - Trust and positive relationships improve collaboration during operations and receptivity to recommendations afterward.
    - Successful operations are some of the best marketing; make meaningful outcomes visible across the organization.
    - A healthy inbound pipeline should be tracked and intentionally prioritized rather than handled ad hoc.

---

## Why Market an Internal Red Team?

At first glance, marketing an internal red team may sound unnecessary. The team already exists, leadership already funds it, and red teamers are perfectly capable of identifying systems they want to test on their own. Plus, red teams are supposed to maintain an independent adversarial perspective, right? Shouldn't we decide for ourselves what to test? Yes, absolutely, but there are also good reasons to source work from others. Threat Intelligence teams can provide insight into relevant adversaries and emerging behaviors. Engineering teams can tell you where their most valuable data lives, painting the bullseye before you even draw your bow. Security architecture teams can point you toward platforms ripe for change and help drive recommendations afterward.

All these examples show how information and collaboration from other teams can positively influence and support your own red team work. But effective collaboration starts with understanding what each team does and how they can help one another. That's the first reason to market red teaming: awareness creates opportunities for collaboration. As we create awareness around what we offer, engineers, security teams, and leaders come to understand the value we provide and are then more likely to recognize situations where adversarial testing could help them. As awareness and understanding increase, they begin to translate into demand for red teaming services. That demand creates a backlog of potential operations from which the red team can select. A team with a healthy backlog can compare opportunities and prioritize the work most likely to produce meaningful measurements and improvements. But the goal is not simply to build the largest backlog possible. The goal is to create enough demand that the team can be selective.

But marketing isn't just about teaching others what red teaming is. It's also about building and fostering trusting relationships that pave the way to effective collaboration. How others perceive the red team heavily influences their willingness to collaborate. Adversarial testing can make people uncomfortable. Red teams intentionally find weaknesses in systems other teams built, operate, or defend. If the first interaction someone has with the red team occurs when an operation exposes a significant problem, it is easy for the team to be perceived as an auditor, an enforcement function, or the "security police." That perception can make people guarded, defensive, and less willing to collaborate.

Building relationships before an operation begins changes that dynamic. When people understand that the red team's purpose is to measure security effectiveness and help influence improvements &mdash; not embarrass teams or point fingers &mdash; red teaming becomes easier to accept and seek out. Then, as operations are scoped and conducted, and findings are delivered, teams are more likely to have candid conversations about what threats are most important and view findings as useful information rather than criticism.

As discussed earlier in this guide, the red team's ultimate goal is to influence improvements, and that's really hard to do if people don't understand or like you. Overall, marketing and promoting red team services builds awareness, demand, and trust, giving the red team better opportunities to test and a better chance of turning those measurements into meaningful change.

## Build Awareness Before You Need It

This is your "get your face out there" section.
The basic principle:
People can't request a service they don't understand.
Explain:
what the red team does
why the organization has one
what kinds of problems it can help evaluate
what makes red teaming different from pentesting/AppSec/etc.
examples of when another team should contact you
Your Section 2 distinction between red teaming and vulnerability-discovery functions gives you a perfect foundation for this.

### Find Your Audience

Possible channels:

- Internal security conferences
- Engineering conferences
- Organization or company all-hands
- Leadership forums
- Security Slack/Teams channels
- Internal security newsletters or quarterly updates
- Engineering/security community meetings
- Readouts from completed operations

It's important to meet people where they are, rather than expecting them to discover a red team wiki page on their own.

### Make It Interesting

This is where your presentation note belongs.
Don't give a 40-slide explanation of ATT&CK.
Show:
a compelling attack story
an unexpected attack path
a surprising defensive gap
a meaningful improvement produced afterward
Your goal is curiosity:
"Could something like that happen to us?"
Then explain how the red team can help answer that question.

## Publish Your Wins

This should probably be a substantial section.
Your principle could be:
Successful operations create demand for future operations—but only if people hear about them.
Share appropriately sanitized examples of:
previously unknown risks uncovered
attack paths demonstrated
defensive weaknesses exposed
improvements triggered by testing
systemic problems identified across multiple teams
But keep it aligned with Section 1: don't market technical activity as impact.
Instead of:
"We compromised 300 hosts."
prefer:
"Testing exposed a systemic credential issue affecting multiple environments, leading to a company-wide control that prevented recurrence."
That directly reinforces your earlier distinction between technical output and actual business impact.

### Make Outcomes Tangible

Your before/after idea fits really well:
Before
adversary technique went undetected
privileged credentials were broadly exposed
incident escalation took hours
After
telemetry added
credentials eliminated/rotated
control deployed broadly
response process improved
I'd be somewhat careful with "dollars avoided." Use it when you actually have defensible numbers, but don't encourage security teams to fabricate hypothetical breach-cost figures just because executives like dollar signs.

## Let Your Customers Promote You

I really like this idea and would give it its own short section.
Your strongest advocates aren't red teamers saying:
"Red teaming is awesome."
They're engineers or security leaders saying:
"We worked with the Red Team, learned something important, and it helped us improve."
Discuss:
satisfied partners sharing experiences at all-hands
joint operation readouts
partner quotes in internal newsletters
leaders recommending red-team engagement to peer organizations
I would emphasize organic advocacy rather than soliciting testimonials.
Something like:
Good work creates advocates. Give those advocates opportunities to tell the story.

## Turn Awareness Into Collaboration

This is where I'd put several of your remaining ideas.
Marketing shouldn't merely cause teams to throw scopes over the wall.
The best outcome is often:
"We have something important we'd like to test. Can we work together?"
Examples:
Engineers acting as trusted insiders during assumed-compromise exercises
Blue teams collaborating on purple-team activities
Product teams providing architecture/context that enables deeper testing
Defenders sharing goals when collaborative testing is appropriate
Interested employees observing portions of an operation or helping with appropriately bounded activities
The important argument isn't necessarily that collaboration makes attacks technically easier.
It's that relationships create better conditions for organizational learning and improvement.
You can connect this directly to the Section 2 line:
"During testing, the red team is an adversary. After testing, it's a partner."
You could even echo that here.

## Manage Inbound Demand

Once marketing works, you have another problem:
people start asking for things.
That's a good problem—as long as you manage it deliberately.
Create a Single Intake Queue
Track requests somewhere structured, e.g. Jira:
requesting organization
proposed target
desired outcome
business/security rationale
timing constraints
stakeholders
initial red-team assessment
priority/status
The point isn't Jira specifically.
The point is creating visibility into demand so the team can triage instead of reacting to whoever asks loudest.

### Decide What Should Be Visible

I like your public/private distinction, but I'd make it a short note:
Some requests can exist in a broadly visible backlog when knowledge of the eventual assessment doesn't materially affect the measurement.
Others should remain restricted when advance awareness could cause defenders or system owners to prepare and invalidate the measurement.
That's a nice strategic nuance.

### Prioritize, Don't Just Schedule

This is the bridge into Section 4.
A long queue isn't a mandate to execute everything.
It gives the red team options.
Then you can evaluate requests based on things like:
alignment with red-team purpose
potential organizational impact
realistic adversary relevance
strategic importance
opportunity to measure important defenses
uniqueness of what the red team can provide
And then say something like:
The goal isn't to work through the backlog. The goal is to use the backlog to identify the best work.
That might actually be one of the central lines of the chapter.

## Demand as a Signal

I'd finish the substantive content with your idea about demand indicating program health, but make it nuanced.
You don't want:
Requests = success.
That conflicts somewhat with your disdain for vanity metrics.
Instead:
Demand is a useful signal, not a measure of impact.
A mature red team may generate plenty of strategically important operations itself. So there isn't some ideal ratio of internally sourced vs externally requested operations.
But if nobody ever requests red-team services, that's worth investigating.
Possible reasons:
employees don't understand what the team does
they don't understand when to engage it
the red team hasn't demonstrated useful outcomes
previous engagements were difficult or unpleasant
the team has a reputation for policing rather than helping
the organization's structure simply doesn't encourage inbound engagement
I'd preserve your slightly provocative wording here because it fits your writing voice:
If nobody ever asks your red team for help, either they don't understand what you do, they don't see value in the results, or you're not very pleasant to work with.
Maybe soften "probably" to "it may be worth asking whether..." in the actual chapter.

## Before You Start Marketing

I wouldn't make ROE/leadership support a full opening section. It distracts from your argument.
Make it a Note box somewhere early:
Prerequisite: This chapter assumes the red team already has organizational authorization, established Rules of Engagement, and leadership support for conducting adversarial testing. Marketing services without clear authority and operational expectations creates problems that awareness alone can't solve.
Short and done.

## From Demand to Decisions

Then a very short closing section that transitions into Section 4:
Marketing has created:
awareness
trust
relationships
inbound demand
a pipeline of potential operations
But capacity is finite.
Now the question becomes which opportunities deserve the red team's time.

---

[← 2. The Purpose of Internal Red Teams](2-purpose.md){ .md-button } &nbsp; [4. Scoping & Planning Operations →](4-scoping.md){ .md-button }
