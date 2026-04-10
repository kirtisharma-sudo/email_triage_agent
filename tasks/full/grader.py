def similarity(a, b):
    a, b = a.lower(), b.lower()
    overlap = len(set(a.split()) & set(b.split()))
    return overlap / max(len(b.split()), 1)

def grade(action, ground_truth):
    score = 0

    if action["priority"] == ground_truth["priority"]:
        score += 0.3

    if action["department"] == ground_truth["department"]:
        score += 0.3

    score += 0.4 * similarity(
        action.get("response", ""),
        ground_truth["response"]
    )

    return min(max(score, 0.01), 0.99)
