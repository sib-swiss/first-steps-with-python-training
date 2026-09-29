# Exercise 3.4

# 1. Write loop that implements the Collatz conjecture
# ****************************************************

# Set the initial value of the sequence.
x = 13
# Create a list to store the sequence of values.
collatz_values = [x]

# Run the Collatz conjecture: it stops when the value becomes 1.
while x > 1:
    # Compute the next value in the Collatz sequence.
    if x % 2 == 0:
        x = x // 2
    else:
        x = 3 * x + 1

    # Add the new value to list.
    collatz_values.append(x)


print(collatz_values)


# 2. Introduce a "safety exit" in the loop
# ****************************************
# The "safety exit" is implemented in the form of a "break" instruction,
# which is triggered when the sequence reaches a length > 1'000'000.

max_iterations = 1_000_000
x = 13
collatz_values = [x]

# Run the Collatz conjecture: it stops when the value becomes 1.
while x > 1:
    # Compute the next value in the Collatz sequence.
    if x % 2 == 0:
        x = x // 2
    else:
        x = 3 * x + 1

    # Add the new value to list.
    collatz_values.append(x)

    # Safety check: if the iterations does not converge after
    # "max_iterations", the loop exits here.
    if len(collatz_values) > max_iterations:
        print(
            "Stopping loop: could not reach the end of the sequence "
            f"after {max_iterations} iterations."
        )
        break

print(collatz_values)
