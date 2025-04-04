import os
import datetime
from config.mongo import get_entropy_collection

# --- Config
DAYS_BACK = 7
OUTPUT_FILE = "reports/gpt_input_week_{}.md".format(datetime.date.today().isocalendar()[1])

# --- Query DB
def get_entropy_events(days=7):
    collection = get_entropy_collection()
    since = datetime.datetime.utcnow() - datetime.timedelta(days=days)
    return list(collection.find({"timestamp": {"$gte": since}}))

# --- Format Markdown
def format_markdown(events):
    by_type = {}
    unresolved = 0
    lines = [
        f"# GPT Entropy Log Summary – Past {DAYS_BACK} Days",
        "",
        f"Total Events: {len(events)}",
        f"Date Range: {DAYS_BACK} days ending {datetime.date.today()}",
        ""
    ]

    for e in events:
        event_type = e.get("event_type", "unknown")
        by_type[event_type] = by_type.get(event_type, 0) + 1
        if e.get("resolution_status") != "resolved":
            unresolved += 1

    lines.append(f"Unresolved Events: {unresolved}")
    lines.append("")
    lines.append("## 🔥 Event Breakdown by Type:")
    for k, v in by_type.items():
        lines.append(f"- {k}: {v}")

    lines.append("\n---\n")
    lines.append("## 📄 Event Details\n")
    for e in events:
        lines.append(f"### • {e.get('event_type', 'unknown')} @ {e.get('location', 'unknown')}")
        lines.append(f"- Operator: {e.get('operator_id', 'unknown')}")
        lines.append(f"- Status: {e.get('resolution_status')}")
        lines.append(f"- Time: {e.get('timestamp').strftime('%Y-%m-%d %H:%M:%S UTC')}")
        lines.append(f"- Notes: {e.get('notes', '')}")
        lines.append(f"- Root Cause: {e.get('root_cause_tag', 'N/A')}")
        lines.append("")

    return "\n".join(lines)

# --- Save to .md file
def write_to_markdown(content, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Report written to: {path}")

if __name__ == "__main__":
    events = get_entropy_events(DAYS_BACK)
    markdown = format_markdown(events)
    write_to_markdown(markdown, OUTPUT_FILE)
