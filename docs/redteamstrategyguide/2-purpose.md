# 2. The Purpose of Internal Red Teams

_Why red teams exist, how they deliver distinct value, and how purpose guides work._

<p class="rtsg-meta">📅 Published August 19, 2026 &nbsp;·&nbsp; 🕒 {{READTIME}} min read</p>

<!-- prettier-ignore -->
!!! tip "Takeaways"
    - Red teams measure how well an org can prevent, detect, and respond &mdash; but the resulting improvements are the payoff.
    - The red team owns the measurement and recommends improvements, while other teams own the decision and the change.
    - Pentesting and bug bounty try to find and break preventative controls; red teams test whether the org could catch and stop a realistic attack.
    - The attacker mindset asks "how can I break this?" The adversary mindset asks "how do I get what I need?"
    - A clear purpose concentrates the team on the highest-impact work only it can do.

---

## The Origins of Red Teaming

I've never been a huge fan of history lessons, but better understanding the origins of red teaming can help us internalize why and how we red team today. In Micah Zenko's [_Red Team: How to Succeed By Thinking Like the Enemy_](https://www.amazon.com/Red-Team-Succeed-Thinking-Enemy/dp/1501274899), he provides a fantastic background of the roots of red teaming. He frames red teaming as a modern version of the Vatican's "devil's advocate", whose job was to argue against candidates for sainthood so the case would be tested rather than rubber-stamped. Here, the contrarian helped suppress a surge in canonization that would dilute the significance of the recognition.

Another example he gives is Israel's "Tenth Man Rule", which many claim came about in the aftermath of the 1973 Yom Kippur War. Essentially, if ten people are presented with the same information, and nine arrive at the same conclusion, it's the duty of the tenth to disagree and argue the opposition. This practice helps prevent groupthink and confirmation bias and can shed light on hidden blind spots that could otherwise be overlooked. Together with the devil's advocate, it shows how institutionalized, sanctioned skepticism has long been recognized as valuable.

The example that really popularized the term "red team", though, is the Cold War war-gaming simulations the RAND Corporation and the US ran to explore potential conflicts and Soviet decision-making. Red represented the Soviet/communist adversary, while blue represented the US and allied forces, with the red team assuming the adversarial mindset to prepare allied forces for adverse scenarios.

Fundamentally, red teaming is about challenging the status quo by adopting the adversarial perspective to uncover and prevent undesirable outcomes. However, in each of these cases, skepticism alone provided no value. It was the resulting change that was the payoff. The devil's advocate stopped bad canonizations. The tenth man broke groupthink before a decision was made. RAND's red teams changed how the US prepared for real conflict. In the context of cybersecurity, red teams follow that same purpose &mdash; we adopt the adversarial mindset to test defensive readiness, ultimately to influence positive security change. Understanding that purpose is foundational to everything we do, so that's where we'll start.

## A Red Team's Purpose

If I were to boil it all down to one sentence, the purpose of a red team is this:

<blockquote class="pull-quote" markdown>
Red teams exist to measure how effectively an organization can prevent, detect, and respond to realistic adversary activity.
</blockquote>

But as we covered in Section 1, measurement alone doesn't improve security. The ultimate goal of those measurements is to inform and influence improvements that make the organization more secure. That resulting change is where the red team delivers its impact.

That distinction between measurement and impact is important. A red team is responsible for producing accurate measurements, translating findings into recommendations, and communicating it all effectively, but it shouldn't own whether the organization implements the recommended improvements. A red team that operates well and delivers solid, well-supported recommendations has succeeded at its job, regardless of whether leadership chooses to act on their findings. That said, success isn't unconditional. If a red team's recommendations are never implemented, it may point to low-quality or poorly-targeted recommendations, but could also indicate an organization is too immature or distracted to act on them. Put simply, the red team owns the measurement and influences the response, while the teams responsible for securing the organization own the change.

Most large companies have internal cybersecurity organizations that are responsible for protecting the company's data and systems. These security programs consist of a wide range of functions, such as a Security Operations Center (SOC), Security Architecture and Engineering, and Vulnerability Management. Collectively, these teams work together to comprehensively prevent, detect, and respond to threats.

After investing significant time and resources into these security programs, leaders need validation that they can actually hold up against real threats. More than assurances from within, leaders need accurate, unbiased measurements of how effective their efforts are at protecting company and customer data. By using red teams, organizations get an independent, adversarial perspective of their defensive readiness, which in turn helps them find and fix weaknesses in their programs before a real adversary finds and exploits them.

This unique purpose of a red team is what differentiates them most from other security assessment functions. Penetration testing and bug bounty are often conflated with red teaming, but their purpose is distinctly different. Their primary responsibilities are scoped to finding vulnerabilities in preventative technical controls. For internal teams, this also tends to include participating in remediation to an extent. The question they seek to answer is _can this be broken?_ Red teams answer an entirely different question: _if a real adversary attacked us, would we prevent it, detect it, and respond in time?_ Red teams can certainly find and exploit vulnerabilities during their tests, but that's merely a means to an end, not the primary objective.

Some organizations blend these different testing responsibilities into versatile penetration testing or generic offensive security teams. While some variation in nomenclature and implementation is understandable, it's important to understand what unique value your team provides. A deep understanding of that purpose helps the team avoid functional overlap and focus its efforts where it can have the greatest impact.

<!-- prettier-ignore -->
!!! note "Note"
    One decision leaders need to make is whether to employ an internal red team or periodically hire external red team consultants. Without internal knowledge, external consultants are typically less influenced by internal assumptions, and their experience across diverse environments gives them a broader perspective. Larger consulting firms are also often able to provide technology-specific testing through consultants with advanced specialties. Internal red teams, on the other hand, can use their deep understanding of the company to focus testing where it can have the most impact without sacrificing realism. Their ongoing presence and relationships also position them well to identify process gaps, collaborate with teams, share findings across the company, and influence broader security improvements following an operation. During testing, the red team is an adversary. After testing, it's a partner.

## The Adversary Mindset

About five years ago, I transitioned from an AppSec/OffSec role to my first red team role. I'd been trying for years to get onto a red team, and I'd finally made it! At that point, I'd been finding bugs and demonstrating impact for a few years professionally, so I thought, _how hard could it be?_ I soon discovered that my _attacker mindset_ was not the same thing as an _adversary mindset_.

Generally speaking, I define the attacker mindset as an unconventional way of thinking that looks past intended use and established rules to find ways a system can be broken or abused. It asks questions like _how did the developer assume this would work?_, _what happens if I use this differently?_, and ultimately, _how can I break this?_

That mindset is foundational to offensive security, but red teaming adds another layer. The adversary mindset uses the attacker mindset in service of a larger objective. Instead of asking only _how can I break this?_, it asks _what am I trying to accomplish?_, and _what should I do next to get there?_

That shift introduces several important traits:

- Intent: Adversaries usually have a reason for attacking. They want your data, your intellectual property, your compute, your crypto wallet. They have mouths to feed, a message to spread, or an ego to satisfy.
- Stealth: Adversaries try to accomplish their mission before getting caught. In some cases, such as for nation states, avoiding attribution may also matter.
- Patience: Adversaries can be very patient, operating low-and-slow for months to avoid detection or reach an opportune moment.
- Indifference: Adversaries are ruthless. They don't care about your policies or uptime SLAs or how long it takes to patch. They want what you have, and your loss or disruption is of no concern to them.

My current boss and Director of the Red Team at Adobe, Justin Tiplitsky, frequently refers to this adversarial shift in perspective as the "evil bit". It's a different way of perceiving the target. When you put on the black hat, the thought process becomes much more strategic: _what do I need, and how can I get it?_

That distinction changes how a red team operates. A vulnerability can be technically severe and still be irrelevant to the operation. If getting root across a fleet of a thousand servers doesn't get you any closer to your objective, then from the adversary's perspective, it's useless. Conversely, one or several seemingly minor weaknesses may be extremely valuable if they provide the access, information, or leverage needed to advance the mission.

Red teams apply the adversary mindset in many ways, such as:

- Identifying, scoping, and planning operations (_see [4. Scoping & Planning Operations](4-scoping.md)_)
- Determining next actions on objectives during an operation (_see [5. Operating Intentionally](5-operating.md)_)
- Delivering detection and response recommendations (_see [6. Reporting & Influencing Change](6-reporting.md)_)
- Using the adversary's story to inform and influence (_see [6. Reporting & Influencing Change](6-reporting.md)_)

Without the adversary mindset, a red team loses much of the realism that makes its measurements valuable and begins to resemble other vulnerability discovery functions. The attacker mindset helps us find ways through defenses; the adversary mindset tells us which paths actually matter.

## Grounding Work in Purpose

With a solid understanding of your purpose, you're better equipped to navigate the ambiguity of red teaming. A clear purpose acts as a filter for deciding what work the red team should take on and what it should leave to other teams. This decision-making process can be applied both when evaluating incoming requests and when proactively identifying work.

Without a strong understanding of purpose, it's easy for a red team to take on work that may be helpful, but ultimately belongs to another team. Instead of taking ownership of another team's responsibilities, the red team can offer insight and recommendations to help improve those processes, technologies, and people. A red team is most valuable when used as intended to measure and influence the company's ability to defend itself, not to do it for them.

One example of red teams assisting in improving defensive capabilities is after an operation, red teams will often provide training and support to blue teams to help them improve their detection and response skills and processes. However, the red team should not assist with the workload of engineering new detections due to capacity limitations or other difficulties. If the team responsible for detecting adversary activity is struggling to perform, that's a finding! By exercising defensive capabilities, sharing findings, and helping teams address identified gaps, red teams can help those teams become more capable and self-reliant.

Another common example of scope creep is when a red team is asked to assist in vulnerability discovery. In some cases, such as in measuring the company's ability to find and remediate vulnerabilities, the red team could be used to gauge the effectiveness of current efforts, but care should be taken to avoid reinforcing misconceptions of purpose and responsibility. Red teams often uncover and exploit vulnerabilities during an operation, and this can lead to a misunderstanding that vulnerabilities are their primary objectives. Red teams should certainly inform the company of the technical and procedural gap, but should avoid taking on the responsibility of scaling vulnerability discovery. Those are precisely the functions they're supposed to be measuring, not driving themselves.

Through all aspects of their work, red teams should remain grounded in their mission of measuring how effectively the organization can prevent, detect, and respond to realistic adversary activity, while using those measurements to influence meaningful improvements. Remember, the red team isn't there to backfill gaps in other security teams' capacity or capabilities; it's there to test those functions, measure their effectiveness, and recommend where leadership should invest to improve them.

## From Operations to Influence

Red teaming work has two major components: technical operations and business influence. While both serve the same goal of improving the organization's security, they require largely different methods and mindsets.

During technical operations, red teamers assume the adversary mindset and simulate realistic attacks to test defenses and identify areas of weakness. To produce credible measurements, red teams seek to operate in a manner indistinguishable from real adversary activity. Doing so requires specialized infrastructure and tooling, along with a deep understanding of offensive tactics, techniques, and procedures. The results of these operations provide the evidence that justifies security investments and improvements. Technical operations are explored further in [5. Operating Intentionally](5-operating.md).

After testing has concluded, the red team shifts its efforts toward reporting its findings and recommending security improvements. It begins by reviewing operation notes and gathering evidence to show which people, processes, and technologies broke down during the attacks. This is where internal red teams hold an advantage. Through their ongoing work alongside other security teams, they develop organizational context that helps them understand how each security function is supposed to prevent, detect, and respond, which in turn helps them recognize where those functions fall short.

From there, red teams combine operational evidence, security expertise, and that organizational understanding into recommendations and work to influence the business to act on them. These recommendations might include additional training or hiring, new technology, or process changes &mdash; anything that could help the company strengthen the systems the red team just exploited. That work is explored in [6. Reporting & Influencing Change](6-reporting.md).

## Purpose First

Once purpose is defined, it should shape everything downstream &mdash; how you scope, operate, report, and measure success. Without it, you're back to the shotgun spray, hoping something lands.

---

[← 1. Introduction](1-introduction.md){ .md-button } &nbsp; [3. Marketing & Promoting Red Team Services →](3-marketing.md){ .md-button }
