---
date: 2025-08-14
categories:
  - Red Teaming
  - Career
tags:
  - red-team
  - career
  - offsec
  - adversarial-mindset
---

# Transitioning From OffSec to Red Teaming

Over the years, I've seen four common challenges that can hold back offensive security professionals who want to move into red teaming:

- grasping the red teaming philosophy
- adopting an adversarial mindset
- understanding red team operations
- gaining hands-on experience

![Transitioning From OffSec to Red Teaming](2025-08-14-transitioning-from-offsec-to-red-teaming.header.jpg)

<!-- more -->

I had to work through these myself when transitioning from other offensive-security-related roles to a red team, and I often find myself covering these topics when I mentor others. In this blog, I'll skip over fundamental hacking skills and focus on each of the above areas and provide some basic guidance and recommendations on how to overcome them. I'll keep this blog brief and perhaps expand on the specific challenges in later blogs.

<!-- prettier-ignore -->
!!! note "Note"
    This blog is primarily focused on internal red teaming, not external consulting, though many points still apply.

## Red Teaming Philosophy

A red teamer needs to understand the history of red teaming, as it helps them understand their own role and purpose better. This knowledge can aid several areas of red team work, like project scoping, decision making during operations, reporting, evangelizing red teaming, and thought leadership. I've listened to dozens of books on various aspects of red teaming, and these are the best in my opinion for understanding why we red team, and conceptually or intellectually how:

- [Red Team: How to Succeed by Thinking Like the Enemy](https://www.audible.com/pd/Red-Team-Audiobook/B0178BAZZI), by Micah Zenko
- [Red Teaming: How Your Business Can Conquer the Competition by Challenging Everything](https://www.audible.com/pd/Red-Teaming-Audiobook/B06XDV323J), by Bryce G. Hoffman

Understanding the origin of red teaming and its uses throughout history helps us better understand why we're using it and how we can utilize it better within our industry as internal red teams.

## The Adversary Mindset

Adopting the adversary mindset is a big hurdle for a lot of security folks who are accustomed to celebrating vulnerability discovery. While vulnerabilities are often within scope of a red team operation or campaign, they're usually not the focus — that's what penetration testing and bug bounty are for. Red teams, on the other hand, simulate or emulate what real threat actors are likely to do, and report on the true susceptibility to said threat. We're kind of like actors — we assume the role and mindset of a real bad guy and play it out. Let that sink in really deep.

There are tons of resources out there that teach or inspire the criminal mind, but the below are a bunch that I have found helpful:

- [The Art of War](https://www.audible.com/pd/The-Art-of-War-Audiobook/B00URXOQ1E), by Sun Tzu, teaches how to be competitive and victorious and how to use an attacker strategy
- [We Are Anonymous: Inside the Hacker World of LulzSec, Anonymous, and the Global Cyber Insurgency](https://www.audible.com/pd/We-Are-Anonymous-Audiobook/B0085ESX34), by Parmy Olson, teaches about adversary groups, how they function, their intentions, their background, and their motives
- [The Lazarus Heist](https://www.audible.com/pd/The-Lazarus-Heist-Audiobook/B09V9D3RQH), by Geoff White, teaches about nation state capabilities and objectives and how they impact major businesses
- [Leaked Conti group chats in English](https://raw.githubusercontent.com/TheParmak/conti-leaks-englished/master/rocket-chat/deepl/rocketchat_deepl_translated.txt), provided by Github user TheParmak, shows the internal chats, tooling, TTPs, and minds of a real criminal group who was active around 2022 — they operate just a like a business
- Yearly threat reports by major providers, [Palo Alto Unit 42](https://www.paloaltonetworks.com/engage/unit42-2025-global-incident-response-report), [Mandiant](https://services.google.com/fh/files/misc/m-trends-2025-en.pdf), [FireEye (now Trellix)](https://www.trellix.com/advanced-research-center/threat-reports/april-2025/), [CrowdStrike](https://go.crowdstrike.com/rs/281-OBQ-266/images/CrowdStrikeGlobalThreatReport2025.pdf), etc, can provide valuable insight into what current adversaries are targeting and how

If you want to simulate or emulate real adversary actions, then you have to study them and think like them. Realism is one of the strongest aspects of our narratives when reporting red team results. Because of that, we must be well-versed in the adversary, and intentional and thoughtful in all our actions.

## Red Team Operations

Penetration tests are similar to red team operations or campaigns in the fact that they both often start with a scoping call to determine target, objectives, and resource investments (duration, participants, etc). Red teaming objectives though are usually very different. Penetration testing usually focuses on discovering as many vulnerabilities as possible within a strict timeframe and in a non-prod environment. Red team operations however are often conducted without advanced notice, in production environments, and are often guided by a particular end-objective like "can you obtain X", or "would adversary group Y be able to do Z". That often means the approved scope of what's allowed is much larger than that of a penetration test, because let's face it, adversaries generally don't have restricted scopes, so to get an accurate measurement, red teams often have wide scopes too.

That's also where operational capabilities of a red team differ dramatically from a penetration test or bug bounty hunter. There is a lot of support work that goes into planning, and running, and reporting a red team operation, such as:

- adversary intel: current trends and likely threats guide the purpose and intent of the operation
- aligning with business goals and building the company where it stands: don't steamroll the blue team. measure where they currently lie, then help stretch them
- technical capabilities: adversary infrastructure, technical TTPs and tooling, research
- operational capabilities: passive/active recon, weaponization, delivery, execution, lateral, persistence, exfiltration, etc
- reporting: building a report or presentation, identifying key stakeholders, coordinating and delivering meetings, building and delivering recommendations
- building blue: measuring key aspects, like detection rate, detection time, response time, etc
- follow up recommendations and trainings: in addition to informing and recommending, it does also help to aid in some root cause analysis and improvement initiatives (running trainings on misses, fine-comb post-mortem with technical teams, influencing leadership on what changes would have prevented the red team's success, etc)

Here are several great resources at how to run red team operations — both the working op or campaign, and red team business operations in general:

- [Red Team Development and Operations](https://www.audible.com/pd/Red-Team-Development-and-Operations-Audiobook/B0F22XLDXH), by Joe Vest and James Tubberville
- [GitLab Red Team docs](https://handbook.gitlab.com/handbook/security/security-operations/red-team/), by Chris Moberly at GitLab
- [Red Team Infrastructure Wiki](https://github.com/bluscreenofjeff/Red-Team-Infrastructure-Wiki), by Github user bluscreenofjeff

## Gaining Red Team Experience

Being able to speak to all these things in an interview is great, but experience often speaks stronger than words. Here is a list of good ways to get experience in and around red teaming, while not being "on" a red team:

- collaborating in purple team exercises
- sharing/discussing adversary intel
- offering detection recommendations alongside vulnerability reports
- helping the red team with research and development (exploit dev, tooling, infrastructure, etc)
- expanding and proving the impact of vulnerabilities (to an extent — don't go beyond authorized limits and don't cause business impact etc)
- explaining how vulnerabilities are relevant to today's threat landscape
- reviewing red team work (offer to review and provide feedback to presentations, research, strategy, etc)
- building open source red team tooling like C2s or attack labs

## Outro

From personal experience transitioning onto a red team, and from years of mentoring aspiring red teamers, the above four areas are the biggest challenges I've seen and heard. The references and recommendations I've provided are what I typically offer to help overcome others these challenges and transition from offsec roles into red teaming.

Best of luck!
