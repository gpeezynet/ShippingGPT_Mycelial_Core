# GPT Entropy Log Summary – Past 7 Days

Total Events: 3
Date Range: 7 days ending 2025-04-04

Unresolved Events: 3

## 🔥 Event Breakdown by Type:
- barcode_scan_failure\: 1
- label_generation_failure: 2

---

## 📄 Event Details

### • barcode_scan_failure\ @ "Packing Station B\
- Operator: JHUNT\
- Status: resolved\
- Time: 2025-04-05 00:30:08 UTC
- Notes: Scan failed 2x before override.\
- Root Cause: scanner_misalignment\

### • label_generation_failure @ Label Station A
- Operator: ZREED
- Status: escalated
- Time: 2025-04-05 01:00:34 UTC
- Notes: Label API call failed, then succeeded with stale manifest. Label printed with wrong carrier.
- Root Cause: api_latency

### • label_generation_failure @ Label Station A
- Operator: ZREED
- Status: escalated
- Time: 2025-04-05 01:06:05 UTC
- Notes: Label API call failed, then returned stale manifest. Label printed with wrong carrier.
- Root Cause: api_latency
