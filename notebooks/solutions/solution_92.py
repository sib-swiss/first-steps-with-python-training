# Exercise 9.2

# In this exercise, we will find the 'gene' and 'CDS' features for the spike
# protein. The spike protein (S protein) is a large type I trans-membrane
# protein, which is highly glycosylated.
# Spike proteins assemble into trimers on the virion surface to form the
# distinctive "corona", or crown-like appearance. The gene is usually called
# the **S** gene and the protein product is called **surface glycoprotein**.

# 1. First, write a function, which accepts a single argument, a record,
# which has to be of `SeqRecord` type.
# This function should loop over all features of this record and return a
# `list` of features whose `.type` is either **'gene' or 'CDS'**. You will
# use this function in all other questions of **7.2**!


def get_gene_cds_features(rec):
    result = []
    for feature in rec.features:
        if feature.type in ["CDS", "gene"]:
            result.append(feature)
    return result


# Using this function, print the **keys** of the qualifiers for all 'gene'
# and 'CDS' features.
# What is the single **key** that can be found in all qualifiers?
# *Hint:* Qualifiers are a special kind of dictionary called OrderedDict.
# Their keys can be accessed by the `.keys()` method.

for feature in get_gene_cds_features(rec):
    print("{}: {}".format(feature.type, list(feature.qualifiers.keys())))

# 2.  Now, using the same function, print the `'gene'` qualifier for all.
# Can you spot the 'S' gene?

for feature in get_gene_cds_features(rec):
    print("{}: {}".format(feature.type, feature.qualifiers["gene"]))


# 3. Using the `'gene'` qualifier from the previous exercise,
# print the `location` of all 'gene' and 'CDS' features for the 'S' gene.

# *Attention, the value of the `'gene'` qualifier is a `list`*


for feature in get_gene_cds_features(rec):
    if feature.qualifiers["gene"][0] == "S":
        print("{}: {}".format(feature.type, feature.location))
