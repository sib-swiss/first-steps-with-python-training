
seq = "GTGCCCCTCGAGAGGAGGGCGCGCGCCGCGCGCTCGACGCGATCGGCGCTCAGCGAGCGAGCTCCTCGAAGCGATCCGCGCGCGCT"
pattern = "CTCGA"
print(seq.find("CTCGA"))

# Limitation:
# find() only returns the 1st occurence of the motif...
# To find other occurrences of "CTCGA", we can use the optionnal argument
# "start" of the "find()"" method and pass the index of the last found
# motif + 1:
print(seq.find("CTCGA", 7))
print(seq.find("CTCGA", 33))
print(seq.find("CTCGA", 65))  # "find()" returns -1 when no match is found.


# Alternatives using loops
# ************************
# Of course, it would be nicer to automate this:
# Here is a sneak peak at how to do this using loops, which we'll see in
# the next lesson.

# Instantiate a list where we will store the motif positions, and get the
# postion of the first match.
positions = []
pos = seq.find("CTCGA")

# This is a loop that will run as long as new matches are found...
while pos != -1:
    positions.append(pos)  # Add motif position to result list.
    pos = seq.find("CTCGA", pos + 1)  # Attempt to find another motif.

print(positions)


# Note: starting with python 3.8, the "wallrus" opperator ":=" can be used
# to write the code is a more condensed fashion.
#
# The := operator allows to assign a value to a variable (here "pos"), and
# evalute an expression at the same time.
pos = -1
positions = []
while (pos := seq.find("CTCGA", pos + 1)) != -1:
    positions.append(pos)
print(positions)
