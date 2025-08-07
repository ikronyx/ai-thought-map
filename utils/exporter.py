import json

def export_json(sentences, labels):
    data = {}
    for s, l in zip(sentences, labels):
        data.setdefault(str(l), []).append(s)
    return json.dumps(data, indent=2)

def export_markdown(sentences, labels):
    output = ""
    clusters = {}
    for s, l in zip(sentences, labels):
        clusters.setdefault(l, []).append(s)

    for label, group in clusters.items():
        output += f"## Cluster {label}\\n"
        for idea in group:
            output += f"- {idea}\\n"
        output += "\\n"
    return output
