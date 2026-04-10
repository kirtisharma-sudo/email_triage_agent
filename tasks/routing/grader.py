def grade(action, ground_truth):
    score = 0

    if action["priority"] == ground_truth["priority"]:
        score += 0.5

    if action["department"] == ground_truth["department"]:
        score += 0.5

    return min(max(score, 0.01), 0.99)
