def divide_if_even(n):
    """Takes a number and divides it by 2 if it is even.
    If the number is odd, it is returned unchanged.
    """

    # To test if a number is even, we check whether the remainder of its
    # integer division by 2 is equal 0.
    if n % 2 == 0:
        n = n / 2  # Divide number by 2

    return int(n)


# Now let's test our function for all integer below ten:
for n in range(10):
    print(n, "->", divide_if_even(n))



# Bonus: shorter way of writing the function.
def divide_if_even(x):
    return int(x/2) if x % 2 == 0 else x
