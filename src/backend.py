import os
import json

SESSION_FILE = "sessions.json"

def save_session(session_data):
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, 'r') as file:
            data = json.load(file)
    else:
        data = []

    data.append(session_data)

    with open(SESSION_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def load_sessions():
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, 'r') as file:
            return json.load(file)
    else:
        return []

