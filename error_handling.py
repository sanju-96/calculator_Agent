def handle_action(action):
    valid_actions = ["add", "subtract", "multiply", "divide"]

    if action not in valid_actions:
        return {
            "status": "error",
            "error": "Invalid action",
            "action": action
        }

    return {
        "status": "success",
        "action": action
    }


# Example
result = handle_action("modulus")
print(result)