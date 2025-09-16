# Exercise 3.4

# 1. Write a function that returns the length of the Collatz sequence of n
# ************************************************************************


# Let's code 2 functions: one that gives the next number in the sequence,
# and one that creates the sequence until it reaches 1.
def next_collatz(n):
    """Divide by 2 if n is even, otherwise multiply by 3 and add 1."""
    if n % 2 == 0:
        r = n / 2
    else:
        r = 3 * n + 1
    return r


def collatz_sequence_length(n):
    """Returns the length of the Collatz sequence of n."""
    seq_length = 1  # Counter for sequence length.
    while n > 1:  # while loop testing for the stopping condition.
        n = next_collatz(n)  # Compute the next number in the sequence.
        # print(n)           # For debugging purposes.
        seq_length += 1

    return seq_length


# Let's test our function with the number 13.
n = 13
print("Collatz sequence length for value", n, "is:", collatz_sequence_length(n))


# Bonus:
# Simple "if... else..." constructs can often be condensed to a single line with
# the "value A if condition else value B" structure.
def next_collatz_2(n):
    return n / 2 if n % 2 == 0 else 3 * n + 1


# 2. Introduce a "max_iter" argument for cases where the conjuncture is false
# ***************************************************************************
# Here is an example of how we can introduce a new optional "max_iter"
# argument to stop the function if it doesn't converge to 1 quickly enough.
def collatz_sequence_length(n, max_iter=500):
    """Returns the length of the Collatz sequence of n.

    If the sequence length exceeds the maximum number of allowed iterations,
    "max_iter", the function returns None.
    """
    seq_length = 1  # Counter for sequence length.
    while n > 1:  # while loop testing for the stopping condition.
        n = next_collatz(n)  # Compute the next number in the sequence.
        seq_length += 1

        # If the sequence length exceeds the maximum number of allowed
        # iterations, we return None.
        if seq_length > max_iter:
            print(
                "Error: sequence did not converge after",
                max_iter,
                "iterations.\nPlease increase 'max_iter' value",
            )
            return None

    return seq_length


n = 101
print(
    "Collatz sequence length for value", n, "is:", collatz_sequence_length(n, 20), "\n"
)


# One more solution where we additionally implement a check to see whether
# a number in the sequence was already encountered, which would
# indicate that we are stuck in an infinite sequence...
def collatz_sequence_length(n, max_iter=500):
    """Returns the length of the collatz sequence of n.

    If the sequence length exceeds the maximum number of allowed iterations,
    "max_iter", the function returns None.
    """

    # Now we keep track of all values in the sequence (instead of just the
    # count).
    collatz_seq = [n]
    while n > 1:
        n = next_collatz(n)
        # Check that the new number in the sequence in not already found in
        # the sequence. This would indicate that the sequence is infinite...
        # (well, so far no one was able to find a number that would not
        # converge to 1!)
        if n in collatz_seq:
            print(
                "Infinite sequence detected: the sequence is an infinite"
                "repetition of: ",
                ", ".join(collatz_seq),
            )
            return None

        collatz_seq.append(n)
        if len(collatz_seq) > max_iter:
            print("Error: only", max_iter, "iterations supported...")
            return None

    return len(collatz_seq)


# Let's test a bunch of numbers.
for n in range(30):
    print("Collatz sequence length for value", n, "is:", collatz_sequence_length(n))
