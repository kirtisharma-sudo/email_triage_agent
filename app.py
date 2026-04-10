from environment import EmailEnv
from inference import policy

def run():
    env = EmailEnv()
    state = env.reset()
    action = policy(state)
    _, reward, _, _ = env.step(action)

    print("STATE:", state)
    print("ACTION:", action)
    print("REWARD:", reward)

if __name__ == "__main__":
    run()
