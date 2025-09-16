# *****************************************************************************
# Micro Exercise 1
# ****************
# Write a function named print_to_screen().


def print_to_screen(string_to_print, reverse=False):
    if reverse:
        string_to_print = string_to_print[::-1]

    print(string_to_print)


# Shorter version using ternary operator.
def print_to_screen_2(string_to_print, reverse=False):
    print(string_to_print[::-1] if reverse else string_to_print)


print_to_screen("Are you suggesting coconuts migrate?")
print_to_screen("!nuf si nohtyp", reverse=True)

# *****************************************************************************


# *****************************************************************************
# Micro Exercise 5
# ****************
# Write a function that takes a number and returns its square.


def square(x):
    """Returns the square value of a number."""
    squared_value = x**2
    return squared_value


# Shorter version.
def square_2(x):
    """Returns the square value of a number."""
    return x**2


# Compute the square value of all numbers from 0 to 10.
for y in range(11):
    print(square(y))
# *****************************************************************************
