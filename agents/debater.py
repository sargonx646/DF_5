import time

def simulate_debate(personas, chat_log, rounds=3):
    for _ in range(rounds):
        for persona in personas:
            message = f"As {persona['name']}, I believe we must consider {persona['goals'][0].lower()}."
            chat_log.append({"agent": persona["name"], "message": message})
            time.sleep(0.3)
    return chat_log