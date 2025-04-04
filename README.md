# 🧠 ShippingGPT – Entropy-Aware Operations Framework

**ShippingGPT** is a memory-based, entropy-aware operational intelligence system.  
It tracks, analyzes, and evolves warehouse SOPs based on chaos events, aiming to reduce disorder and increase stability through self-correcting feedback loops.

> "Entropy is not failure—it's signal. We measure it, learn from it, and adapt."

---

## 🚧 What This Is

ShippingGPT is **not just a bot or a program**. It's a modular intelligence framework that includes:

- 📦 Real-time event logging via MongoDB
- 🧾 Adaptive SOP versioning based on live feedback
- 📊 Weekly entropy trend reports
- 🤖 GPT integration for SOP analysis and simulation
- 📁 Human-readable logs, markdown reports, and structured GPT input

---

## 🧩 Core Modules

| Module              | Purpose                                       |
|---------------------|-----------------------------------------------|
| `ShippingGPT`        | Executes SOPs, tracks entropy                |
| `ConductorGPT`       | Oversees SOP conflicts + memory tracking     |
| `StrategistGPT`      | Runs entropy simulations + scenario planning |
| `WarehouseGPT`       | Answers warehouse-specific logic + flow      |
| `DeveloperGPT`       | Maintains structural integrity + evolution   |

---

## 📦 Folder Overview

```bash
.
├── config/               # MongoDB connection + config
├── scripts/              # CLI loggers, reporters, GPT input generator
├── docs/                 # System dashboard + role map
├── entropy_logs/         # Daily raw chaos logs
├── feedback/             # SOP revision suggestions from entropy
├── sops/                 # Versioned SOPs (packing, picking, etc.)
├── reports/              # Weekly summaries + GPT inputs
├── logs/                 # System-level logs (philosophy, ConductorGPT)
├── standards/            # Immutable operating standards
├── ShippingGPT/          # Core intelligence logic + stability metrics
├── GPT_Functions/        # Agent role JSONs for GPT integration
└── .env.example          # Environment variable template
