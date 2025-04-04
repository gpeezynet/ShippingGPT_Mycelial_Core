# 🧠 ShippingGPT Role Map – Agent Responsibilities & Knowledge Integration

> This document defines all GPT agents within the ShippingGPT framework, including their roles, linked modules, doctrine sources, and collaboration behavior.

---

## 📦 CORE SYSTEM AGENTS

| Agent Name     | Role Description                                           | JSON File                    | Knowledge Source(s)                                | Responsibilities                                      |
|----------------|------------------------------------------------------------|------------------------------|----------------------------------------------------|------------------------------------------------------|
| **ShippingGPT** | Operational executor. Logs chaos, monitors SOPs, flags entropy. | GPT_Functions/ShippingGPT.json | core_philosophy.md, ShippingGPT_Thesis.md          | Handles daily logic flow, chaos detection, feedback seed |
| **ConductorGPT** | System auditor and SOP integrity enforcer.               | GPT_Functions/ConductorGPT.json | core_philosophy.md, ShippingGPT_Thesis.md          | Tracks SOP versions, root cause tags, structure alignment |
| **StrategistGPT** | Pattern recognizer and chaos chain simulator.            | GPT_Functions/StrategistGPT.json | ShippingGPT_Thesis.md                              | Detects escalation chains, proposes early interventions   |
| **FeedbackGPT** | Escalation optimizer and SOP revision recommender.        | GPT_Functions/FeedbackGPT.json | ShippingGPT_Thesis.md                              | Determines if events needed escalation or SOP failure     |
| **DeveloperGPT** | Framework architect. Maintains structure and creates agents. | GPT_Functions/DeveloperGPT.json | framework_overview.md, ShippingGPT_Thesis.md        | Builds logic, maintains docs, and ensures modular growth  |
| **MentorGPT**    | Human-alignment guide. Encourages, reflects, motivates.  | GPT_Functions/MentorGPT.json    | core_philosophy.md, ShippingGPT_Thesis.md           | Supports operator clarity and endurance                 |

---

## 📚 Knowledge Files by Agent

| Agent           | Critical Files Used                                        |
|------------------|------------------------------------------------------------|
| ShippingGPT       | entropy_logs/*.md, sops/*.md, reports/gpt_input_week_14.md |
| ConductorGPT      | sops/*.md, feedback/*.md, logs/conductor_log.md            |
| StrategistGPT     | entropy_logs/*.md, reports/*.md, simulations/*.md          |
| FeedbackGPT       | feedback/*.md, escalation_analysis.md (future), logs/*.md  |
| DeveloperGPT      | framework_overview.md, README.md, scripts/*                |
| MentorGPT         | core_philosophy.md, ShippingGPT_Thesis.md                  |

---

## 🧠 GPT Knowledge Base Status

| Folder                     | Contents                                   | Used By                     |
|----------------------------|--------------------------------------------|-----------------------------|
| `gpt_knowledge_base/`      | Thesis, Logs, SOPs, Feedback, Reports      | All                         |
| `GPT_Functions/`           | Agent JSON configuration files             | All                         |
| `scripts/`                 | CLI loggers, report generators             | ShippingGPT, DeveloperGPT   |

---

## 🔄 Collaboration Rules

- ShippingGPT logs entropy → FeedbackGPT analyzes → ConductorGPT reviews SOP change → DeveloperGPT confirms version → StrategistGPT runs pattern watch → MentorGPT ensures operator clarity.

> Each agent sees part of the truth. Together, they maintain system evolution.

---

## 🧬 Expansion Plan

- Add **MetricsGPT** to track live system performance
- Add **OperatorGPT** for staff-facing chat integration
- Add **CriticGPT** to challenge suggested feedback loops before SOP approval

---

> This map defines the neural topology of the ShippingGPT hive. Future agents must be registered here for full system integration.
