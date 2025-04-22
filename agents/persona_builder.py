import random

def build_personas(stakeholders):
    tones = ["analytical", "pragmatic", "emotional", "strategic"]
    biases = ["risk averse", "pro-growth", "compliance-focused", "cost-cutter"]
    return [{
        "name": role,
        "goals": [f"Advance the interest of {role}"],
        "biases": [random.choice(biases)],
        "tone": random.choice(tones)
    } for role in stakeholders]