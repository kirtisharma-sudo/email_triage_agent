---
title: Email Triage OpenEnv
emoji: 📧
colorFrom: blue
colorTo: green
sdk: docker
app_file: app.py
pinned: false
---
# Email Triage OpenEnv

## Problem
Automating enterprise email triage using RL environments.

## Tasks
1. Priority classification
2. Routing
3. Full triage pipeline

## State
- email_text
- sender

## Action
- priority
- department
- response

## Reward
Weighted scoring across:
- classification
- routing
- response similarity

## Real-world relevance
This environment simulates enterprise email triage workflows used in customer support automation.

## Complexity
- Multi-step reasoning
- Noisy input
- Multi-objective reward

## Run
```bash
python inference.py
