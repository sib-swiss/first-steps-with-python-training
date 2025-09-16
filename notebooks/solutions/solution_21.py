# Exercise 2.1

seq = "GTGCCCCTCGAGAGGAGGGCGCGCGCCGCGCGCTCGACGCGATCGGCGCTCAGCGAGCGAGCTCCTCGAAGCGATCCGCGCGCGCT"
pattern = "CTCGA"
print(seq.find(pattern))

# Limitation:
# find() only returns the 1st occurrence of the motif...
# To find other occurrences of "CTCGA", we can use the optional argument
# "start" of the "find()" method and pass the index of the last found
# motif + 1:
print(seq.find(pattern, 7))
print(seq.find(pattern, 33))
print(seq.find(pattern, 65))  # "find()" returns -1 when no match is found.


# Alternatives using loops
# ************************
# Of course, it would be nicer to automate this:
# Here is a sneak peak at how to do this using loops, which we'll see in
# the next Notebook.

# Instantiate a list where we will store the motif positions, and get the
# position of the first match.
positions = []
pos = seq.find(pattern)

# This is a loop that will run as long as new matches are found...
while pos != -1:
    positions.append(pos)  # Add motif position to result list.
    pos = seq.find(pattern, pos + 1)  # Attempt to find another motif.

print(positions)


# Note: starting with python 3.8, the "walrus" operator ":=" can be used
# to write the code is a more condensed fashion.
#
# The := operator allows to assign a value to a variable (here "pos"), and
# evaluate an expression at the same time.
pos = -1
positions = []
while (pos := seq.find(pattern, pos + 1)) != -1:
    positions.append(pos)
print(positions)


# Alternative using regexp.
# A more efficient approach would be to use the external module "re" that
# provides regular-expression matching.
import re

pattern = "CTCGA"
print(
    "The number of occurrences of the pattern in seq is:", len(re.findall(pattern, seq))
)

print("The start positions of the pattern in seq is:")
for match in re.finditer(pattern, seq):
    print(match.start())
