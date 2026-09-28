# Exercise 2.2

# Store the sequence as a string variable.
dna_seq = "ATGCCATTAGCGAGATCGATCGAT"


# Since "seq" is a string, we look at "help(str)" to search for methods of str
# objects. We can see that there is a "replace()" method that allows replacing
# characters within a string.
rna_seq = dna_seq.replace("T", "U")
print("Original sequence   :", dna_seq)
print("Transcribed sequence:", rna_seq)


# Alternative using the "split()" and "join()" method: the sequence is first
# split on the letter "T", and then joined on the letter "U". This effectively
# replaces all "T" by "U", but is somewhat more cumbersome to read.
print("U".join(dna_seq.split("T")))
