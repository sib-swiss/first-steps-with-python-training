# Import the csv module.
import csv

# Create empty lists to store the strain, region and country data.
strain = []
region = []
country = []

# Open the input file in read mode, and read through it.
with open("data/genbank.sars-cov2.metadata.csv", "r") as f:

    # Load the file handle as a "DictReader" object. This can then
    # be looped over, and each line in the file (except the header)
    # is returned as a dictionary of {field_1: value, field_2: value, ...}
    reader = csv.DictReader(f , delimiter=';')

    for row in reader:
        strain.append(row['strain'])
        region.append(row['region'])
        country.append(row['country'])

# Let's print the length of our 3 lists:
print(len(strain), "strains")
print(len(region), "regions")
print(len(country), "countries")

# And the first 3 entries of each list:
print("strains   :", strain[:3])
print("regions   :", region[:3])
print("countries :", country[:3])



# Alternative solution, using only python built-in functions (no csv library)
# ***************************************************************************
strain = []
region = []
country = []

input_path = "data/genbank.sars-cov2.metadata.csv"
with open(input_path, mode="r") as f:

    # Read the header line to skip it: we do not want to store that data.
    l = f.readline()

    # loop through all lines in the file:
    for l in f:
        # Remove the '\n' at the end of the line with "strip()", and
        # split the line according to the ';' character
        sl = l.strip().split(";")

        strain.append(sl[0])
        region.append(sl[1])
        country.append(sl[2])

# Let's print our 3 lists:
print(len(strain), "strains")
print(len(region), "regions")
print(len(country), "countries")

# the first 3 entries of each lists:
print("strains   :", strain[:3])
print("regions   :", region[:3])
print("countries :", country[:3])
