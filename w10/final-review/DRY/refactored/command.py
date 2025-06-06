def handle_command(command):
    actions = {
        "START": "Starting the process...",
        "STOP": "Stopping the process...",
        "PAUSE": "Pausing the process...",
    }
    return actions.get(command, "Unknown command")


command = "START"
print(handle_command(command))
