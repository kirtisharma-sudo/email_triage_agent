import random
import json

class EmailEnv:
    def __init__(self, data_path="data/emails.json"):
        with open(data_path, "r") as f:
            self.dataset = json.load(f)
        self.current = None

    def reset(self):
        self.current = random.choice(self.dataset)
        return self._get_state()

    def _get_state(self):
        return {
            "email_text": self.current["email_text"],
            "sender": self.current["sender"],
            "history": []
        }

    def step(self, action):
        gt = self.current

        reward = self._compute_reward(action, gt)

    # SAFETY CLAMP (MANDATORY for hackathon)
        reward = float(max(0.01, min(0.99, reward)))

        return self._get_state(), reward, True, {}

    def _compute_reward(self, action, gt):
        score = 0.0

        if action.get("priority") == gt["priority"]:
            score += 0.3

        if action.get("department") == gt["department"]:
            score += 0.3

        pred = (action.get("response") or "").lower()
        true = gt["response"].lower()

        overlap = len(set(pred.split()) & set(true.split()))
        sim = overlap / max(len(true.split()), 1)

        score += 0.4 * sim

        return score

    def _text_similarity(self, a, b):
        a, b = a.lower(), b.lower()
        overlap = len(set(a.split()) & set(b.split()))
        return overlap / max(len(b.split()), 1)
