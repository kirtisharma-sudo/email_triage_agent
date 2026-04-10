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

## Run
```bash
python inference.py
