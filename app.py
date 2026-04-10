from environment import EmailEnv
from inference import policy

def run_demo():
    env = EmailEnv()
    state = env.reset()
    action = policy(state)
    _, reward, _, _ = env.step(action)

    return {
        "state": state,
        "action": action,
        "reward": reward
    }

if __name__ == "__main__":
    print(run_demo())
