with open("SARS-CoV-2_acc.txt") as infile:
    accessions = infile.read().splitlines()

# How many accessions are there? What is the first accession? What is the last accession?
print("There are {} accessions".format(len(accessions)))
print("First accession is:", accessions[0])
print("Last accession is:", accessions[-1])

