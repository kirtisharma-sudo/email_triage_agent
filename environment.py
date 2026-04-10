import os
import json
import random


class EmailEnv:
    def __init__(self, data_path="data/emails.json"):
        # -----------------------------
        # SAFE PATH HANDLING (IMPORTANT)
        # -----------------------------
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        DATA_PATH = os.path.join(BASE_DIR, data_path)

        with open(DATA_PATH, "r", encoding="utf-8") as f:
            self.dataset = json.load(f)

        self.current = None

    # -----------------------------
    # RESET ENVIRONMENT
    # -----------------------------
    def reset(self):
        self.current = random.choice(self.dataset)
        return self._get_state()

    # -----------------------------
    # GET STATE
    # -----------------------------
    def _get_state(self):
        return {
            "email_text": self.current.get("email_text", ""),
            "sender": self.current.get("sender", ""),
            "history": []
        }

    # -----------------------------
    # STEP FUNCTION (MAIN LOGIC)
    # -----------------------------
    def step(self, action):
        gt = self.current

        reward = self._compute_reward(action, gt)

        # HARD SAFETY CLAMP (MANDATORY for hackathon)
        reward = float(max(0.01, min(0.99, reward)))

        done = True

        return self._get_state(), reward, done, {}

    # -----------------------------
    # REWARD FUNCTION
    # -----------------------------
    def _compute_reward(self, action, gt):
        score = 0.0

        # priority match
        if action.get("priority") == gt.get("priority"):
            score += 0.3

        # department match
        if action.get("department") == gt.get("department"):
            score += 0.3

        # response similarity (simple overlap-based)
        pred = (action.get("response") or "").lower()
        true = (gt.get("response") or "").lower()

        pred_words = set(pred.split())
        true_words = set(true.split())

        if len(true_words) > 0:
            overlap = len(pred_words & true_words)
            similarity = overlap / len(true_words)
        else:
            similarity = 0.0

        score += 0.4 * similarity

        return score
