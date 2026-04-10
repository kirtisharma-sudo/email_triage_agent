from environment import EmailEnv
from inference import policy

def run():
    env = EmailEnv()
    s = env.reset()
    a = policy(s)
    _, r, _, _ = env.step(a)
    print({"reward": r})

if __name__ == "__main__":
    run()
