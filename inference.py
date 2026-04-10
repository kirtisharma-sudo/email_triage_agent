from environment import EmailEnv

def policy(state):
    text = state["email_text"].lower()

    if "refund" in text or "immediately" in text:
        priority = "high"
        dept = "support"
    elif "price" in text:
        priority = "medium"
        dept = "sales"
    elif "crash" in text:
        priority = "high"
        dept = "tech"
    else:
        priority = "low"
        dept = "support"

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
