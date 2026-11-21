# 3. Marketing & Promoting Red Team Services

_How to build awareness, demand, and trust for internal red teaming._

<p class="rtsg-meta">📅 Published November 20, 2026 &nbsp;·&nbsp; 🕒 {{READTIME}} min read</p>

<!-- prettier-ignore -->
!!! tip "Takeaways"
    - Internal marketing helps teams understand what red teaming is, why it exists, and how it can help them.
    - Educating others on the red team's purpose leads to higher-quality requests that better fit your work.
    - Greater awareness creates organic demand, giving red teams more opportunities from which to select high-impact work.
    - Trust and positive relationships improve collaboration during operations and receptivity to recommendations afterward.
    - Successful operations are some of the best marketing; make meaningful outcomes visible across the organization.

---

## Why Market an Internal Red Team?

At first glance, marketing an internal red team may sound unnecessary. Shouldn't we just focus on running operations? Operations are the core of our work, but as we covered in [2. The Purpose of Internal Red Teams](2-purpose.md), our ultimate goal is to influence security improvements. That becomes much harder if teams don't understand what we do, how we can help them, or why they should trust us.

Marketing helps us achieve this goal in three ways: it builds awareness, creates demand, and establishes trust.

### Awareness

Red teams that operate without organizational input risk exposing weaknesses without understanding the company's priorities or ability to address them. Their measurements may be accurate, but if they don't account for that context, they rarely lead to improvements. On the flip side, red teams that only test what the organization asks for risk inheriting its biases and blind spots.

Building awareness opens the door to conversations that help us find that sweet spot between the two. As we spread awareness about the red team's mission, other teams learn what we offer and how we can help each other. We also learn about their concerns, capabilities, and priorities so that we can design testing that stretches the organization and leads to improvements.

A few examples of collaborating with other teams:

- Threat Intelligence teams can tell us which adversaries are relevant to the company and how they've been operating lately.
- Engineering teams can tell us what they want to protect and where they want to validate their defenses.
- Security Architecture teams can point us to potentially risky workflows in critical platforms and help champion resulting improvements.

From our side, we can show defenders how an adversary would actually move through their environment, give engineers the backing to get security work prioritized, and give leaders evidence of where their security investments fall short against a motivated adversary.

### Demand

As engineers, security teams, and leaders understand the value we provide, they're more likely to recognize where adversarial testing could help them. This creates organic demand, giving us more opportunities to choose from. We're not trying to build the biggest backlog we can &mdash; we just want enough requests to pick the highest-impact work.

Marketing also affects the kinds of requests we get. Red teams can easily get pulled into vulnerability discovery or backfilling other teams' capacity. If people only know us as the team that finds vulnerabilities, they'll keep asking us to find vulnerabilities. When we present or write about our work, we should be clear about what the red team is actually for: measuring how well the company can prevent, detect, and respond to realistic adversary activity. When people understand that, they're more likely to ask us how their defenses would hold up against an attack, not just whether we can find vulnerabilities.

### Trust

Adversarial testing can make people uncomfortable. Red teams intentionally find weaknesses in systems other teams build, operate, or defend. If someone's first interaction with the red team is an operation that exposes a major problem they're responsible for, it's easy for them to see us as auditors or the "security police." People who see us that way tend to get defensive and are less willing to collaborate.

Building relationships before an operation starts helps establish trust before we need it. Teams should know the adversary role is temporary: we simulate an adversary during testing, but remain partners in improving security throughout. When teams know we're there to help them improve, not to embarrass them or point fingers, they're more likely to accept red teaming and even ask for it. They're also more likely to tell us what actually worries them and to take our recommendations seriously.

The red team's goal is to influence improvements, and that's hard to do if people don't understand or trust us. Marketing helps others understand what we do and want to work with us, which leads to better-informed operations, findings that get acted on, and improvements that last.

The rest of this section covers how to do that: finding the right audiences, showing the value of our work, and turning interest into opportunities.

## Find Your Audience

Internal red teams are uncommon &mdash; most people won't know what we do unless we tell them. Use the channels the organization already has, such as internal conferences, engineering all-hands, security forums, leadership meetings, newsletters, Slack or Teams channels, and operation readouts, to explain what the red team does and where it has helped.

Different audiences care about different things. Engineers may want to understand how an adversary would steal their crown jewels. Security teams may want to know where their defenses are weakest. Leaders may care more about systemic risk, organizational resilience, and whether security investments are working as intended. The focus of the message can change based on the audience, but our purpose should be clear and consistent.

Be specific about when someone should reach out. Useful starting points include:

- Major platform changes that alter how the organization prevents, detects, or responds to attacks
- Uncertainty about whether defenses would stop a relevant adversary
- Concerns about a sensitive attack path

Explain what a team can expect from an operation and how it differs from requesting a penetration test. They don't need to arrive with a fully scoped request.

Some of the best opportunities come from small interactions. An engineer who attends a red team presentation may later volunteer architecture context for an operation. A defender may propose a purple team exercise to test logging coverage they're unsure of.

## Show the Value

Successful operations are some of our best marketing, but only if people hear about them. Tell short, compelling stories about unexpected attack paths, what they revealed about the organization's defenses, and what improved afterward. The story should lead people to consider whether something similar could happen in their area. Then explain how the red team can help them find out.

As discussed in [1. Introduction](1-introduction.md), technical results aren't the same as business impact. "We compromised 300 hosts" may get attention, but it doesn't explain why anyone should care. A more useful story might be: "Testing exposed a systemic credential issue affecting multiple environments. The responsible teams used those findings to deploy a control that closed that attack path across the company."

In each story, be specific about what changed. For example, an adversary technique that went undetected now produces an actionable alert, default credentials no longer ship in products, or new logging lets incident responders see lateral movement they previously missed. Distinguish improvements that have been implemented from those that are still recommendations. Don't claim a control works until it's been validated, and don't attach a hypothetical "dollars avoided" figure without defensible evidence.

Share these stories through presentations, internal writeups, and operation readouts, with enough context for other teams to recognize where the lessons apply. Agree with leadership or stakeholders on what can be shared and with whom. Sanitize sensitive details, give credit to the teams that made the improvements, and avoid turning a security gap into a public embarrassment.

We don't have to be the only ones telling the story, either. An engineer or security leader explaining how a red team operation helped their team improve can be more persuasive than the red team promoting itself. Joint readouts and partners sharing their experiences at all-hands give others a concrete example of what working with the red team looks like.

<!-- prettier-ignore -->
!!! quote "Story Time: Letting Leaders Tell Our Story"
    At our company-wide 2026 Cybersecurity Awareness Month event, one of the themes was the evolving role of AI in both cyberattacks and defense. I gave the red team's perspective on how adversaries are using AI and where it's heading. I closed with a few asks: assume adversaries are already inside, and think like an adversary about which parts of your systems need the most protection.

    Before the event, the director speaking after me reached out to ask for red team metrics to include in their talk. On stage, they used those metrics to support their own message.

    When leaders see red team data as useful, they ask for it and use it in their own messages, which often carries more weight than the red team could alone.

## From Awareness to Opportunities

Make it easy to take the next step. Every presentation or writeup should point to a clear way to contact the team, whether that's a shared channel, an intake form, or a team email. Capture those conversations in a shared intake queue so useful opportunities aren't lost in individual inboxes, while restricting sensitive details that could tip off the teams being tested. Make it clear that submitting a request doesn't guarantee we'll take it on.

The number of requests doesn't measure our impact. The red team should keep identifying its own work and form its own view of what matters most. We use requests to help find the best work, not as a list to complete.

That's where marketing hands off to [4. Scoping & Planning Operations](4-scoping.md): deciding which opportunities are most likely to lead to improvements and turning them into operations with clear objectives.

---

[←&nbsp;2. The Purpose of Internal Red Teams](2-purpose.md){ .md-button } [4. Scoping & Planning Operations&nbsp;→](4-scoping.md){ .md-button }
{ .rtsg-nav }
