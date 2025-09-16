# Exercise 5.2

strains = []
regions = []
countries = []

input_path = "data/genbank.sars-cov2.metadata.csv"
with open(input_path, mode="r") as f:
    # Read the header line without doing anything with it just to skip it.
    f.readline()

    # Loop through all lines in the file:
    for line in f:
        # Remove the '\n' at the end of the line with "strip()", and
        # split the line according to the ';' character
        strain, region, country = line.strip().split(";")

        # Add the strain, region and country values to their respective
        # lists.
        strains.append(strain)
        regions.append(region)
        countries.append(country)

# Let's print our 3 lists:
print(len(strains), "strains")
print(len(regions), "regions")
print(len(countries), "countries")

# Print the first 3 entries of each lists:
print("strains   :", strains[:3])
print("regions   :", regions[:3])
print("countries :", countries[:3])


# Alternative solution, using the pandas external module
# ******************************************************
# (a sneak peak of day 3 modules)
import pandas as pd

df = pd.read_csv("data/genbank.sars-cov2.metadata.csv", sep=";")
strains = list(df.strain)
regions = list(df.region)
countries = list(df.country)

# Let's print our 3 lists:
print(len(strains), "strains")
print(len(regions), "regions")
print(len(countries), "countries")

# Print the first 3 entries of each lists:
print("strains   :", strains[:3])
print("regions   :", regions[:3])
print("countries :", countries[:3])
