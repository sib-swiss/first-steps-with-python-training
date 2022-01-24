
# 1. Read the file, store the strain id, geographic regions, and country in
#    three different lists (strain, region, country)

strain = []
region = []
country = []

import csv 
with open("data/genbank.sars-cov2.metadata.csv", "r") as f:

    # Read the header line to skip it: we do not want to store that data.
    reader = csv.DictReader(f , delimiter=';')

    for row in reader:
        strain.append(row['strain'])
        region.append(row['region'])
        country.append(row['country'])

# Let's print our 3 lists:
print(len(strain), "strains")
print(len(region), "regions")
print(len(country), "countries")
# the first 3 entries of each lists:
print("strains   :", strain[:3])
print("regions   :", region[:3])
print("countries :", country[:3])


##
## Alternative solution, using only python simple bricks (no csv library)
##

strain = []
region = []
country = []

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

