# In this solution, we provide 2 different ways to write a function
# that creates the reverse complement of a sequence.


def reverse_complement(seq):
    """Returns the reverse complement of a sequence given as argument.

    This is the implementation using a dictionary to lookup nucleotide
    complements.
    """
    nucleotide_complements = {"A": "T", "T": "A", "C": "G", "G": "C"}

    # Create an empty string variable that will be used to store the
    # function's output.
    reversed_complement = ""

    # Loop through all nucleotides in the sequence in reverse sequence.
    # In this way, we won't need to reverse the sequence later.
    for nucleotide in seq[::-1]:
        # Find the complement of the current nucleotide.
        reversed_complement += nucleotide_complements[nucleotide]

    # Return the reverse complement.
    return reversed_complement


def reverse_complement_2(seq):
    """Returns the reverse complement of a sequence given as argument.

    This is the implementation using if/else lookup nucleotide complements.
    """
    # Create an empty string variable that will be used to store the
    # function's output.
    complement = ""
    # Loop through all nucleotides in the sequence...
    for nucleotide in seq:
        if nucleotide == "A":
            complement += "T"
        elif nucleotide == "T":
            complement += "A"
        elif nucleotide == "G":
            complement += "C"
        elif nucleotide == "C":
            complement += "G"
        else:
            # In case the nucleotide is not A, T, G, or C -> error!
            print("Unknown nucleotide :", nucleotide)
            print("Abort!")
            return None

    # Reverse the complement.
    return complement[::-1]


# Let's test our functions:
input_seq = "ATAGAGCGATCGATCCCTAGCTA"
revcomp_seq = reverse_complement(input_seq)
revcomp_seq_2 = reverse_complement_2(input_seq)
print("original              :", input_seq)
print("reverse complemented  :", revcomp_seq)
print("reverse complemented 2:", revcomp_seq_2)

# Check against output of the online tool:
online_result = "TAGCTAGGGATCGATCGCTCTAT"
print("Is 'reverse_complement' result correct?", revcomp_seq == online_result)
print("Is 'reverse_complement_2' result correct?", revcomp_seq_2 == online_result)


# Bonus: shorter way of writing the function.
def reverse_complement_3(seq):
    nucleotide_complements = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(nucleotide_complements[n] for n in seq[::-1])


# Bonus: benchmarking of the 3 functions.
#        Uncomment the code below to run (it takes a little while to run).
# Warning: %timeit is an iPython "magic" functions that benchmarks a function.
#          This will only run a Jupyter notebook, not in a regular python shell.

# test_sequence = "ATAGAGCGATCGATCCCTAG" * 10000
# print("Benchmarking reverse_complement ...")
# %timeit reverse_complement(test_sequence)
# print("Benchmarking reverse_complement_2 ...")
# %timeit reverse_complement_2(test_sequence)
# print("Benchmarking reverse_complement_3 ...")
# %timeit reverse_complement_3(test_sequence)
