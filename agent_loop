# calculator_agent.py

for iteration in range(1, 4):
    print(f"\n--- Iteration {iteration} ---")

    # OBSERVE
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    print(f"Observe: {num1} {operator} {num2}")

    # DECIDE
    if operator in ["+", "-", "*", "/"]:
        decision = "Valid operation"
    else:
        decision = "Invalid operation"

    print("Decide:", decision)

    # ACT
    if decision == "Valid operation":
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2 if num2 != 0 else "Cannot divide by zero"

        print("Act: Result =", result)
    else:
        print("Act: Invalid operator")