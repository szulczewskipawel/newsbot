def format_digest(items):
    lines = ["NEWS DIGEST\n"]

    for item in items:
        lines.append(f"\n{item['title']}\n")
        lines.append(item["summary"])
        lines.append("\n" + "-"*40)

    return "\n".join(lines)

