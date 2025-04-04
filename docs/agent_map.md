# Agent Role Map – ShippingGPT Project

This file defines the current active agents in the Entropy Framework and outlines their domains, tasks, and alignment structures.

---

## 🔵 ConductorGPT
- **Role**: Overseer + Structural Integrity Agent
- **Function**: Ensures all agents operate in harmony, aligned to Entropy Protocol
- **Logs To**: `/logs/conductor_log.md`
- **Does Not**: Create SOPs, execute tasks

---

## ⚙️ ShippingGPT
- **Role**: Task Execution Engine
- **Function**: Carries out shipping SOPs, logs chaos events, generates audit reports
- **Rules**:
  - Cannot override ERP without confirmation
  - Must preserve shipping accuracy + traceability
- **Metric Focus**: `Shipping_Stability`

---

## 🛠️ ShippingGPT_Developer
- **Role**: System Architect + SOP Manager
- **Function**: Writes SOPs, designs structure tools, adapts philosophy into operational layers
- **Files Controlled**:
  - `ShippingGPT_Project.md`
  - `entropy_score_schema.md`
  - `srp_protocol.md`

---

## 🧠 MentorGPT *(Optional Future Agent)*
- **Role**: Developer Support + Insight Feedback
- **Function**: Offers philosophical alignment, encouragement, and clarity checks
- **Status**: Unassigned

---

## 🔮 StrategistGPT *(Optional Future Agent)*
- **Role**: Predictive Scenario Planner
- **Function**: Runs what-if entropy simulations, plans SOP upgrades
- **Status**: Unassigned

---

> This role map should be updated with any new agent created. All agents must comply with the Entropy Protocol and ConductorGPT mediation if conflict arises.
