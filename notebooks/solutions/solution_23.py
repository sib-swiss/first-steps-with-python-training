# Notes:
# There are multiple ways in which a reverse complement function can be
# written, and we provide you with 2 different options here.
#
# The first implementation takes a bit longer to design and write, however it
# may be easier to understand for someone who does not know the methods of
# `str` in Python.
# Also, the first implementation may be faster than the second implementation
# because it iterates over the nucleotides of `seq` only once, whereas the
# second function does it twice (in each call of the `count` method). This is
# however mitigated by the fact that native python methods and function are
# often quite efficient, and it is not easy to outperform them.


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


# Let's test our 2 implementations:
my_seq = "ATAGAGCGATCGATCCCTAGCTA"
gc1 = get_GC_percent(my_seq)
gc2 = get_GC_percent_2(my_seq)

if gc1 != gc2:
    print("ERROR! The 2 functions returned different results:", gc1, gc2, sep="\n")
else:
    print("The 2 functions returned the same result.\nGC% of the sequence:", gc1)


