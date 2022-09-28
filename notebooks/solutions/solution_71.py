with open("SARS-CoV-2_acc.txt") as in_file:
    accessions = in_file.read().splitlines()

# * How many accessions are there?
# * What is the first accession?
# * What is the last accession?
print("There are {} accessions".format(len(accessions)))
print("First accession is:", accessions[0])
print("Last accession is:", accessions[-1])

