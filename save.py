import json
import os

def save_data(command_history, conversation_progress):
    command_history_str = {str(user): list(set(commands)) for user, commands in command_history.items()}
    data = {
        "command_history": command_history_str,
        "conversation_progress": conversation_progress
    }

    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "data.json")

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def load_data():
    try:
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, "data.json")

        if os.path.getsize(file_path) > 0:
            with open(file_path, "r") as file:
                data = json.load(file)
                print("Loaded :", data)
            return data["command_history"], data["conversation_progress"]
        else:
            return {}, {}
    except FileNotFoundError:
        return {}, {}
