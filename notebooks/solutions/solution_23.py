# Notes:
# There are multiple ways in which a reverse complement function can be
# written, and we provide you with 2 different options here.
#
# The first implementation takes a bit longer to design and write, however it
# may be easier to understand for someone who does not know the methods of
# "str" in Python.
# Also, the first implementation may be faster than the second implementation
# because it iterates over the nucleotides of `seq` only once, whereas the
# second function does it twice (in each call of the `count` method). This is
# however mitigated by the fact that native python methods and function are
# often quite efficient, and it is not easy to outperform them.
# Note: upon benchmarking both solutions, it turns-out that the second one,
#       which uses the build-in ".count()" method is faster.

# First implementation, using a for loop.
def get_GC_percent(seq):
    """Computes the percentage of GC nucleotides in a sequence"""

    # Initialize a variable that we will use to count the number of G and C.
    GC_count = 0
    for nucleotide in seq:
        # If the nucleotide is a G or C, increment the counter of GC.
        if nucleotide in "GC":
            GC_count += 1

    seq_length = len(seq)
    return GC_count / seq_length * 100.0


# Second implementation, using the "count()" methods of str.
def get_GC_percent_2(seq):
    """Computes the percentage of GC nucleotides in a sequence"""

    GC_count = seq.count("G") + seq.count("C")
    return GC_count / len(seq) * 100


# Let's test our implementations against known values:
test_sequences = {
    "AAAATTTT": 0,
    "AATTGGCC": 50,
    "AATTAAAC": 12.5,
    "GGGGGGGC": 100
}
for seq, expected_value in test_sequences.items():
    actual_value = get_GC_percent(seq)
    if actual_value == expected_value:
        print(seq, "produced a correct result:", actual_value)
    else:
        print("ERROR: unexpected value for", seq, ": ", actual_value, "[expected:", expected_value,"]")



# Bonus: benchmarking of the 2 implementations.
#        Uncomment the code below to run (it takes a little while to run).
# Warning: %timeit is an iPython "magic" functions that benchmarks a function.
#          This will only run a Jupyter notebook, not in a regular python shell.

# test_seq = "ATAGAGCGATCGATCCCTAGCTA" * 1000
# %timeit get_GC_percent(test_seq)
# %timeit get_GC_percent_2(test_seq)
