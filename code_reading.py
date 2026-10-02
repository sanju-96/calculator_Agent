state = {
    "done": False,
    "steps": 0,
    "status": None
}

max_steps = 2

for i in range(max_steps):
    state["steps"] += 1

    print(f"Step {state['steps']}")

    # Observe
    print("Observe: Checking current state")

    # Decide
    print("Decide: Choosing next action")

    # Act
    print("Act: Performing action")

    # Success condition
    if state["steps"] == 2:
        state["done"] = True
        state["status"] = "success"

print("\nFinal State:")
print(state)