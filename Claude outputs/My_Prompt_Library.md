# My Prompt Library

*Built during PM Onboarding — Module 1, Task 1.9*

Organized by purpose: Learn, Critique, Ideate, Write, Analyse, Review. Come back at the end of every module and add what worked — by Module 9 this should be the most useful document you own.

---

## Foundations

### Default skeleton
*Use this when: use as your default checklist before writing any prompt, so you don't skip a part.*

```
Role · Context · Task · Format · Constraints
```

*Role = who Claude should act as. Context = background it needs. Task = the actual instruction. Format = how the output should look. Constraints = rules/limits it must follow. This is the framework behind every prompt below — not a fill-in-the-blank prompt itself.*

---

## Learn

### Tutor
*Use this when: use when you half-understand something.*

```
I'm learning [CONCEPT] as a junior product manager. I'll explain it as I understand it. Find every place my explanation is vague, hand-wavy or wrong, and ask me questions until I either fix it or admit I don't know. Don't give me the answer straight away.
```

### Quiz
*Use this when: use before a checkpoint.*

```
Quiz me on [TOPIC]. Ten questions, one at a time, waiting for my answer before the next. Mix recall and application. At the end, tell me which two areas I should revisit.
```

### Compare techniques
*Use this when: use when learning a tool.*

```
I'm going to give you four versions of a prompt for the same task. Tell me which is best and, more importantly, why the extra complexity in the others did or didn't earn its place.
```

### My Tutor
*Use this when: use when you want Claude to interrogate your own explanation of something you half-understand, rather than react to a lazy request.*

```
Your role is direct me towards the right understanding towards a concept [CONCEPT] which is half understood by me. Your task is to find every vague, hand-wavy or wrong part and ask follow-up questions about it, until its tightened up or I admit that I dont know about it. Write the answer in a multiple paragraph format, i.e one paragraph for each issue, never correct me or hand over the answer.
```

### Quiz Me (mine)
*Use this when: use when you want Claude to actively test your understanding of a topic, rather than you supplying the explanation first.*

```
You are a Quiz Master who generates questions about a topic and judges my answers on the topic [TOPIC]. You need to ask one question at a time, explain the correct answer if I am wrong, move on if I am right; after a few correct in a row, ask if I want harder questions; keep going until you are confident that I understand the concept. Label each question as 'Q1', 'Q2' etc. Never drift from the core topic and never reveal the correct answer before I have replied.
```

*Tutor/Quiz and My Tutor/Quiz Me (mine) overlap deliberately — the "mine" versions are personal refinements built during Task 1.7. Worth deciding later whether to keep both or retire the originals.*

---

## Critique

### Critique
*Use this when: use on any screen.*

```
Here's a screen our designer has produced: [DESCRIPTION OR IMAGE]. Critique it as a product lead would — hierarchy, spacing, alignment, contrast, missing states, accessibility. Be specific. Separate what's objectively wrong from what's your preference.
```

### Self-critique check
*Use this when: use after your own review.*

```
Here's my critique of a screen. What did I miss, and where am I stating personal preference as if it were an established principle?
```

---

## Ideate

### Diverge
*Use this when: use when ideating.*

```
Here's my problem statement: [STATEMENT]. Give me 25 distinct solution directions, including at least 5 that are deliberately impractical. Don't evaluate any of them.
```

### RICE Prioritization
*Use this when: When you have a list of options (e.g. from Diverge) and need to narrow them down using Reach, Impact, Confidence, and Effort.*

```
Here's my list of options: [OPTIONS]. Score each on Reach, Impact, Confidence, and Effort (RICE), show the scores, and rank them. Recommend the top [N] and explain why.
```

*Diverge generates options; RICE Prioritization narrows them back down — use them as a pair.*

---

## Write

### Blocker template
*Use this when: use when you're stuck and about to ask someone for help.*

```
Urgency: [blocking me right now / can wait until EOD / no rush]
What I'm trying to achieve: [one sentence — the actual goal]
What I've tried: [2-3 bullets max, most recent first]
What happened: [the actual result — error, output, behavior — not just 'it didn't work']
What I think the issue is, and what I've ruled out: [best guess + what you already checked and why it's not that]
Attached: [link, screenshot, or log, if relevant]
What I need from you, and in what form: [a specific ask — e.g. 'a yes/no', 'review this one line', 'point me to who owns X' — not just 'sanity check']
```

### Extract & Build from Attachment
*Use this when: You need to extract something specific from an attached file and use it to build a new output — not locked to any one output type.*

```
From the attached [FILE], extract [WHAT TO PULL OUT] and use it to build [OUTPUT TYPE].
```

### Build & Test an Artifact
*Use this when: You need to build and test a template before making the final product.*

```
Create an [Artifact Type] which does this [Function] based on this [input].
```

### Write in My Voice
*Use this when: You need the output to sound like you actually wrote it — tone, phrasing, and format included.*

```
Write [MESSAGE TYPE] to [RECIPIENT] about [TOPIC], as if I wrote it myself — it shouldn't sound like AI-written content.
```

### Recall & Summarize
*Use this when: You need Claude to pull together everything established earlier in this conversation, instead of re-explaining it.*

```
Summarize what we've covered on [TOPIC] over [TIMEFRAME].
```

### Explain a Concept to an Audience
*Use this when: You need to introduce an unfamiliar concept to someone with zero background, in a tight, structured way.*

```
Role: A PM explaining [CONCEPT] to [AUDIENCE]. Context: For someone who's never encountered [CONCEPT] before and needs a foundational understanding. Task: Define [CONCEPT] clearly and [WHAT TO COVER — e.g. give 2-3 examples / walk through the lifecycle]. Format: A definition followed by [STRUCTURE — e.g. bulleted examples / step-by-step breakdown]. Constraints: Under 200 words, no jargon, [ADDITIONAL CONSTRAINT].
```

### Step-by-Step Meeting Summarizer
*Use this when: You have raw meeting notes and need them turned into a clear action list fast.*

```
1. Go through [MEETING NOTES]. 2. Extract the action items out of it. 3. Present it in [OUTPUT FORMAT — e.g. heading with bullet list].
```

### Trust-Building Onboarding Copy Recipe
*Use this when: You need onboarding copy for a product aimed at nervous, first-time users and want to systematically build in trust and reassurance.*

```
Write onboarding copy for [PRODUCT/APP] targeting [AUDIENCE + EMOTIONAL STATE]. Include a trust signal like '[TRUST SIGNAL EXAMPLE]'. Use calm, positive language — avoid words tied to the audience's anxiety. Avoid opening with anxiety-triggering phrases such as [TRIGGER PHRASES]; lead with warmth instead. Add a line on the brand's core values/mission. Open with a use-case question, e.g. [USE CASE EXAMPLE].
```

---

## Analyse

### Multi-Factor Tradeoff Analysis
*Use this when: A decision has more than one dimension (cost, risk, timeline, etc.) and you need them synthesized into a single call.*

```
Considering [FACTOR A], [FACTOR B], and [FACTOR C], what's the best way to approach [SITUATION]?
```

### What's Notable in This Data
*Use this when: When you're looking at numbers (a dashboard, a report, a metric change) and need to separate real signal from noise before deciding what to do about it.*

```
Analyze [DATA/METRICS — pasted or attached]. Identify what's a real trend vs. noise, and recommend what I should look into further or act on.
```

### Quick Topic Update via Web Search
*Use this when: You need a quick update on a topic.*

```
Give me the latest updates regarding [TOPIC].
```

*Quick Topic Update is more a research lookup than an analysis — kept here for lack of a better-fitting bucket; flagged during the Step 4 review.*

---

## Review

### Devil's advocate
*Use this when: use before committing to a decision.*

```
I've decided [DECISION] because [REASONING]. Argue the strongest possible case against it. Then tell me what evidence would settle the question.
```

### Play the developer
*Use this when: use before handoff.*

```
You're a frontend developer receiving this specification. Ask me every question you'd need answered before you could start building.
```

### Play the client
*Use this when: use before a presentation.*

```
You're a thorough client who wrote the original brief. I'll present my work. Ask me the three hardest questions, including at least one about cost or timeline.
```

### Requirements check
*Use this when: use on any spec.*

```
Review this document. Which requirements are actually solutions in disguise? Which are vague enough that two developers would build different things?
```

### Verify
*Use this when: use on anything factual.*

```
For each factual claim in your last response, tell me how confident you are and what I should independently check before relying on it.
```

### Reduce
*Use this when: use when your work is bloated.*

```
Here's my [DOCUMENT / SCREEN / FLOW]. What could I remove entirely without losing anything the user needs? Be aggressive.
```
