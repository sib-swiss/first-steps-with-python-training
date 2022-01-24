### 7.2

# **1.** For this and the following exercises we will work only with the **first accession**.
# Retrieve the sequence record for the first accesssion from Genbank using `Bio.Entrez`. Keep this record as a new variable.

from Bio import Entrez
from Bio import SeqIO

Entrez.email = "A.N.example@institute.ch"
handle = Entrez.efetch(db="nucleotide", id=accessions[0], rettype="gb", retmode="text")
rec = SeqIO.read(handle, "genbank")
handle.close()


# What is the `id`, `name` and `description` of this record?

print("ID={}\nName={}\nDescription={}".format(
    rec.id, rec.name, rec.description)
)

# Confirm that the ID of this record matches the first accession in the accessions text file. 
# Based on these information, can you guess in which country this isolate was identified?

print("Accession IDs do match:", rec.id == accessions[0])
print("Country of origin could be", rec.description.split("/")[2])


# **2.** How many entries are there in the `annotations` of this record?

print("There are", len(rec.annotations), "annotations associated with this record")

# Print the 'taxonomy' and the 'references' of this record. What is the title of the publication this sequence was published?

print(rec.annotations["taxonomy"])
print(rec.annotations["references"])
print()
print("Method of submission:", rec.annotations["references"][0].title)


# **3.** How many entries are there in the `features` of this record? Print the first feature.

print("There are", len(rec.features), "features")
print(rec.features[0])

# This is a 'source' feature and usually there is a single 'source' feature for a record. 
# It holds like the 'annotations' very useful information about the source of this record. 
# Can you confirm the country of origin?

print("The place of origin for this isolate is", rec.features[0].qualifiers["country"][0])

# How many different possible values are there for the `type` of these features and what are they?

# Using a list
feature_types = []
for feature in rec.features:
    if feature.type not in feature_types:
        feature_types.append(feature.type)
print("There are {} different values for feature types".format(len(feature_types)))
print(feature_types)

# Optional - alternative using set
feature_types_set = set([feature.type for feature in rec.features])
print("There are {} different values for feature types".format(len(feature_types_set)))
print(feature_types_set)

# Can you spot the differences between the list and set versions?
# Sets are very useful counters to hold unique members
# Try help(set)


# How many 'gene's does this viral genome have, according to the features? 
# How many 'CDS's are defined in the features? Are the number of genes and CDSs same?
# *Hint*, dictionaries can be used to count multiple things within a single loop.

counter = {'CDS': 0, 'gene': 0}
for feature in rec.features:
    if feature.type in counter:
        counter[feature.type] += 1
print(counter)



