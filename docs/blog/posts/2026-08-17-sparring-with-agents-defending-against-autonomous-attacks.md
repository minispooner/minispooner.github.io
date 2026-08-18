---
date: 2026-08-17
categories:
  - AI Agents
  - Red Teaming
  - Blue Team
  - Metrics
tags:
  - ai
  - agents
  - red-team
  - blue-team
  - metrics
  - detection
---

# Sparring with Agents: Defending Against Autonomous Attacks

I recently built an autonomous attack system and deployed it against several live production systems. After successfully reaching post-exploitation impact, I considered what would have stopped it, and I came up with several metrics that organizations can track to measure and improve their defensibility specifically against autonomous attackers. In this post, I'll introduce three metrics and several ways to influence them.

_These attack agents are tightly guardrailed and closely monitored. I plan to share more about the system in another post._

<figure markdown="span">
  ![Combating Autonomous Attacks](2026-08-17-sparring-with-agents-defending-against-autonomous-attacks.header.png)
</figure>

<!-- more -->

WIP...

<!--
## What Sets Autonomous Attacks Apart

Modern AI agents can operate at a speed and scale humans can't match. This makes them particularly dangerous in cyber attacks because they can find and exploit weaknesses faster than humanly possible. It's helpful to set aside our traditional security mindset and instead consider how AI agents actually reason and act during an attack.

## What Would Have Made Attacking Harder

After each significant step forward in my red team operations, I ask myself _what would have stopped me or made this harder?_ The answer to this is often what I present as security recommendations during my readouts. After evaluating my own autonomous attacks, I came up with several concepts that would have made my autonomous attacks harder:

- Slowing my agents down
- Confusing my agents
- Increasing the cost of my agents

Translating these into organizational metrics that can guide and track improvements in defensibility, I came up with these three metrics:

- **Time to Success** — time between first action and completion of objective
- **Total Commands** — number of actions or commands the agent executed
- **Total Cost** — tokens consumed (or dollars spent) by the agent

Each are closely correlated, but can also be independent of each other. I'll expand on each below.

### Time to Success

Defenders want this number as high as possible. Every extra second the attack takes is extra time to detect and respond before the objective is reached.

I'm still working on testing these theories, but here are several ways we may be able to slow down autonomous attacks:

- Confuse the agent with misleading or complex content. Think of this as a form of social engineering against the agent to slow it down. This could be accomplished via indirect prompt injections, such as planting files to misdirect the agent or cause misinterpretation of the system architecture.
- Overload the agent's context window with large datasets. Hosting numerous, or large text files could cause agents to stray from their original system prompt (prompt drift). If the agent's system uses context compaction, this can also cause it to lose track of earlier findings or state, forcing it to re-discover or re-verify things it already knew, burning time and tokens.
- Plant invalid or canary tokens to cause the agents to waste time and resources. As the agent attempts to validate fake credentials, it can get bogged down in network calls, generate more telemetry, increase its token counts, and trigger canary detections.

### Total Commands

Increasing the total commands required to reach an objective also drives up Time to Success and Total Cost, since more steps generally means more time and tokens. But an increase in total commands also means an increase in telemetry. Every command is a chance for something to log, alert, or leave a trace. 200 steps instead of 20 to reach the same objective means 10x more opportunities for a detection to fire.

Here are a few potential ways to accomplish this:

- Increase your filesystem footprint. Creating a larger folder structure hierarchy with nested subfolders and file references can cause the agent to traverse more directories and filepaths.
- Obfuscate file paths. Similar to confusing the agent, this can impact agents' abilities to use file paths to reason about context and attack paths.

### Total Cost

Currently, the best performing models are paid frontier models. Although free, open-weight alternatives are close behind, frontier models excel at long-horizon, multi-step reasoning that autonomous attacks require. If defenders can prepare their environment sufficiently so that attackers must pay for the most-powerful models, they can increase the cost of attacks and thereby decrease the pool size of potential attackers. Instead of "any attacker with a laptop", it'd be narrowed down to attackers who can fund their efforts.

Assuming the adversary uses a paid model, some ways to increase token consumption include:

- Host numerous, or large files to consume tokens.
- Inject distracting, but plausible data into READMEs or files to inflate agent reasoning.

## Moving the Numbers

After establishing baseline measurements and giving teams time to implement recommendations, we can repeat the same autonomous attacks with the click of a button and see the difference in outcomes. These two result sets are highly valuable to red teams and security organizations, as they literally detail and measure improvements to security &mdash; or lack thereof.

The ideas laid out in this blog are still in their infancy, so empirical testing is necessary to evaluate their effectiveness. Furthermore, additional consideration is needed regarding the potential impact of these countermeasures on legitimate workflows. The practical implementation of these examples may not be feasible in real-world scenarios. For instance, confusing file paths and misleading READMEs could just as easily degrade onboarding or other processes as it could attacking agents.

## Takeaways

- Increasing Time to Success gives defenders more time to detect and respond.
- Increasing Total Commands required for the agent to reach its objectives means more telemetry and more chances to catch it.
- Increasing Total Cost decreases the pool size of potential adversaries to only those who can afford it.

Moving any of these three metrics upward is a measurable defensive improvement worth celebrating.

## Closing & Next Steps

Conducting adversarial tests and obtaining measurements of current defenses is only the first part of the equation. Ultimately, those measurements should be used to inform and influence positive security change. Next, I plan to test these theories to identify which measures actually make it harder for autonomous attacks to succeed. Every round of sparring &mdash; testing, measuring, adjusting &mdash; should leave the defense a little better than last time.
 -->
