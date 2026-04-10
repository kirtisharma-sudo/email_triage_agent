from environment import EmailEnv

def policy(state):
    text = state["email_text"].lower()

    priority = "low"
    dept = "support"

    if "refund" in text or "urgent" in text:
        priority = "high"
        dept = "support"

    elif "price" in text or "cost" in text:
        priority = "medium"
        dept = "sales"

    elif "error" in text or "crash" in text:
        priority = "high"
        dept = "tech"

    return {
        "priority": priority,
        "department": dept,
        "response": "We are looking into your request."
    }


if __name__ == "__main__":
    env = EmailEnv()
    state = env.reset()
    action = policy(state)
    _, reward, _, _ = env.step(action)

    print("State:", state)
    print("Action:", action)
    print("Reward:", reward)
