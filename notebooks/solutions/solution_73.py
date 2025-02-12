### 7.3

# **1.** Create a new record by **slicing** the previous record using the
# coordinates of the 'S' gene.
# How many features does this 'S' gene record have?


s_gene = rec[21549:25371]
print("'S' gene record has", len(s_gene.features), "features")

#**2.** Translate the 'S' gene (transcript in this case, as this is an RNA
# virus) into a new variable called `s_protein`.
# Which translation table should we use (a little biology)? 
# Does the protein sequence contain a stop?
# If so, try to translate without a stop character.
# How many amino acids does this protein have?

s_protein = s_gene.translate(to_stop=True)
print("S protein has", len(s_protein), "amino acids")

