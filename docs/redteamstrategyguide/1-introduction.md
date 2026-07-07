# 1. Introduction

_Why I wrote the Red Team Strategy Guide (RTSG) and what "impact" really means._

<!-- prettier-ignore -->
!!! tip "Takeaways"
    - RTSG focuses on maximizing business impact from red team operations (i.e. influencing security improvements)
    - RTSG offers tips and advice on how to run a red team program effectively, as opposed to detailing how to technically execute red team operations
    - RTSG is built on 16+ years of security experience, ~5 years of it red teaming

---

## Why I'm Writing the RTSG

Red teaming in large organizations is ambiguous work. Unlike an engineering team shipping features or closing tickets, a red team's output is a set of findings and recommendations. Some argue that the success of a red team ultimately depends on whether other teams act on our findings, while others claim that our value lies in the unbiased delivery of adversarial perspective, regardless of how the receiving end takes it. They're both right, and both are worth pursuing, but knowing when to lean on each matters &mdash; more on this in [2. The Purpose of Internal Red Teams](2-purpose.md). Without a deep understanding of our red team purpose and how we fit into the overall strategy of a large security organization, it's easy to mistake activity (operations run, reports written, vulnerabilities found) for actual outcomes.

Over my 16+ years of security experience, I've been exposed to thousands of statements, blogs, presentations, and pitches about security work and projects. They often talk about what was built or found, but with little mention of the resulting impact. This focus on technical detail and the "what we did" is understandably more common in less-experienced Individual Contributors (ICs), as it typically coincides with their role expectations &mdash; they're usually the doers. The pattern isn't limited to early-career ICs, though; I've seen plenty of mid-career and even senior leaders struggle with the concept of impact as well.

Over the last five years of red teaming, I've identified several key areas that have consistently helped me lead successful red team operations. In this guide, I distill my experience and lessons learned into several sections to help other red teams and security teams maximize their business impact. Because individual circumstances and needs vary, rather than trying to precisely replicate my actions or stories, I'd encourage you to adapt the principles and processes to fit your unique needs. The bulk of this guide is written for red teams, but many of the concepts apply to other security functions as well, since we all typically share the same overarching objectives of maintaining and improving security &mdash; we just do it in different ways.

## Defining Impact

There are lots of different reasons why companies implement various security functions. Each function should have a purpose, and their various security initiatives should deliver value in unique ways, such as achieving compliance, enabling sales, or hunting adversaries. These outcomes can all be impactful, so long as they align with the security function's purpose and goals.

When I refer to "impact" throughout this guide, such as in "delivering impactful work", I'm typically referring to _actually improving security_, or _clearly and strongly influencing security improvements_. Most red teams, for example, don't actively engineer solutions or patch vulnerabilities, but their outputs directly inform and influence security investments and improvements. Therefore, their business impact falls into the influencing category.

Other teams, however, may play a more active role in literally making changes to code and systems to harden the perimeter or add defense-in-depth controls, both of which directly improve security by reducing risk. Both are legitimate approaches, though influential security teams like red teams are insufficient on their own, as there is generally no improvement unless it is made by another team &mdash; again, a topic I'll cover more in [2. The Purpose of Internal Red Teams](2-purpose.md).

### Edge Cases

There are a couple of edge cases where security work can still be impactful, despite security improvements not actually being the primary objectives. I'll briefly offer some thoughts on these, but will mostly refrain from comment throughout the rest of the guide.

The first case I'll touch on is _supportive security work_. While it can be impactful, there should be very clear, concrete evidence to support its value. For example, if it is necessary to enable or facilitate other legitimate security improvements, or if it significantly contributes to security improvements, then it could be useful. Unfortunately, I've seen a lot of security work inappropriately justified under the guise of being "supportive", when there is little or weak evidence that it actually made a significant difference. When there is clear and strong evidence that the supportive work is leading to security improvements, then it does fall within my definition of impact.

Another large pillar of security work that is not in scope for my guide is compliance. Generally speaking, if a company wants to improve their security, they don't dive into compliance as a solution. While compliance may establish a minimum baseline, it is not a vehicle for meaningful security improvement. For example, there have been several major breaches over the past few years, despite the companies holding compliance certifications (LastPass 2022, Okta 2023, Change Healthcare 2024). Compliance is a point-in-time goal to satisfy legal requirements and increase sales. Because the primary goal of compliance work is certification, not continuous security improvement, I don't include it in my content or comments on security work aimed at improving security.

### Technical Impact vs Business Impact

It's important to make a clear distinction between "technical impact" and "business impact". Unfortunately, I often see security folks fixated on the technical results of their work and not the actual impact of it. Below are a few examples of how a team may attempt to classify their technical output as impactful. In certain scenarios, these results may indeed align with strategic objectives, but for our examples, we'll weigh the technical results vs. outcomes from a different perspective.

- In a recent penetration test, we compromised the administrative console and obtained read access to all customer directories.
- Last quarter, we integrated 20 new secret detection signatures, increasing our coverage by 50%, and total detections by 5%.
- During our last incident, we used AI agents to analyze 100+ data sources to assist us in our investigation, saving 4 hours of human work, landing us 10% under the Average Time to Close for our incident.

While these "wins" may appear impressive, additional context could severely erode much of the perceived success:

- The product platform is EOL, 90% of the users have already completed migration to the newer systems, and the customer directories are empty or only contain public, default product install data.
- The new detections are for niche API keys only found in legacy repositories, typically no longer running in production services. They do not represent credentials that have been abused in recent incidents or that would typically lead to severe consequences.
- While AI may have saved the Incident Response team time, they were still ultimately unable to identify the adversary's point of entry or what was actually stolen. These results indicate a significant gap in the team's ability to perform their baseline responsibilities, that of containing, mitigating, and recovering from incidents.

The above examples show how apparent success may not actually lead to business impact. These are sometimes referred to as "vanity metrics", where surface-level data points may look impressive but offer no real insight into the true business performance or success. These metrics can often crumble under the pressure of a little skeptical questioning.

Now, if the original scenarios were approached with a business impact-focused mindset, the results may have been much more meaningful:

- Four out of six of our latest pentests have surfaced authentication-related vulnerabilities, each stemming from a misconfigured authentication plugin. We've documented the common misconfigurations on the internal platform page and are scheduling presentations across major engineering orgs to share our findings and recommendations to prevent recurrence. We've also shared custom semgrep rules with our source code scanning team to identify misconfigurations in source code to help eliminate other vulnerabilities that we are unable to manually assess.
- Last quarter, we collaborated with the Threat Intel Team and the Red Team to identify the top 5 secrets that are most-commonly exploited, and we've implemented hard blocks to prevent those patterns from being pushed into our code bases. We also ticketed all current findings of these secrets, 75% of which have already been removed from source code and rotated. Additionally, we followed up with the Incident Response Team yesterday who reported that incidents have dropped by 5%, and then 10%, over the last two months. Their data confirms that there are significantly fewer incidents originating from these aforementioned secrets types.
- During our last incident, we used our new AI agent to investigate and identify logging gaps on the compromised machine. After it identified several logs that could help with adversary attribution, it then provided configuration recommendations to us that we've successfully tested with the engineering team. We're in the process of rolling these updates out to all applicable endpoints so that we can better identify and track adversaries in our networks during future incidents.

In the last examples provided, the actions and reports move away from shiny technical output metrics and draw closer to how the results actually improved security. I also made a point to showcase the scale of the effects of the projects, something we'll revisit when discussing how to scale outcomes at the end of an operation in [5. Operating Intentionally](5-operating.md).

## What's Ahead

I love to quote the Cheshire Cat, from Lewis Carroll's _Alice's Adventures in Wonderland_. When Alice asks which way to go, the cat responds, "That depends a good deal on where you want to get to." Without a clear purpose, a red team's efforts become a scattered, shotgun spray, relying on hope that something lands. However, when we do understand our purpose and where we want to be, we can target specific outcomes with the precision of a sniper.

That's why the rest of this guide follows a typical operational sequence of a red team, starting with purpose. [2. The Purpose of Internal Red Teams](2-purpose.md) comes first because it clarifies what counts as impact for your red team. From there, [3. Marketing & Promoting Red Team Services](3-marketing.md) and [4. Scoping & Planning Operations](4-scoping.md) determine what work gets done and why. [5. Operating Intentionally](5-operating.md) governs how it gets executed, and [6. Reporting & Influencing Change](6-reporting.md) and [7. Measuring Success](7-measuring.md) close the loop by translating results into influence and proving whether that influence actually moved the needle. Each section adds specific benefits to the overall impact of red team deliverables, and we'll explore each throughout the guide.

[Next: 2. The Purpose of Internal Red Teams →](2-purpose.md){ .md-button }
