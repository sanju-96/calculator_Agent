log = []

max_iterations = 10
done = False
status = "failure"

for i in range(max_iterations):
    step = i + 1

    # Observe
    log.append(f"Step {step}: Observe")

    # Decide
    log.append(f"Step {step}: Decide")

    # Act
    log.append(f"Step {step}: Act")

    # Success condition
    if step == 3:
        done = True
        status = "success"
        log.append("Success condition reached")
        break

if not done:
    log.append("Maximum iterations exceeded")

return log