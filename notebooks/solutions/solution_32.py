strain = []
region = []
country = []

input_path = "data/genbank.sars-cov2.metadata.csv"
with open(input_path, mode="r") as f:

    # Read the header line to skip it: we do not want to store that data.
    l = f.readline()

    # Loop through all lines in the file:
    for l in f:
        # Remove the '\n' at the end of the line with "strip()", and
        # split the line according to the ';' character
        sl = l.strip().split(";")

        # Add the strain, region and country values to their respective
        # lists.
        strain.append(sl[0])
        region.append(sl[1])
        country.append(sl[2])

# Let's print our 3 lists:
print(len(strain), "strains")
print(len(region), "regions")
print(len(country), "countries")

# Print the first 3 entries of each lists:
print("strains   :", strain[:3])
print("regions   :", region[:3])
print("countries :", country[:3])



# Alternative solution, using the pandas external module (a sneak peak of day 3 modules)
# **************************************************************************************
import pandas as pd
df = pd.read_csv( "data/genbank.sars-cov2.metadata.csv" , sep=";" )
strain  = list( df.strain )
region  = list( df.region )
country = list( df.country )

# Let's print our 3 lists:
print(len(strain), "strains")
print(len(region), "regions")
print(len(country), "countries")

# Print the first 3 entries of each lists:
print("strains   :", strain[:3])
print("regions   :", region[:3])
print("countries :", country[:3])
