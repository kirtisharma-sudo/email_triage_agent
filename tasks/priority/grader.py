def grade(action, ground_truth):
    if action["priority"] == ground_truth["priority"]:
        return 0.8
    elif action["priority"] in ["medium", "high"]:
        return 0.5
    return 0.2
