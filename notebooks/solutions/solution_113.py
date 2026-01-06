# Exercise 7.3

import pandas as pd

# 1. Center each column: subtract their mean from their values.
df = pd.read_csv("data/mouse_heart_gene_expression.tsv", sep="\t")
column_means = df.mean()
print(column_means)

df -= column_means
df.head()


# 2. select genes whose expression is above the column-wise average
# Here we can take advantage from the fact that we have already removed
# the column averages, so we are interested in positive values.
mask = (
    (df["Heart_WT_1"] > 0)
    & (df["Heart_WT_2"] > 0)
    & (df["Heart_WT_3"] > 0)
    & (df["Heart_WT_4"] > 0)
)
df[mask].head()


# If we hadn't done the subtraction, here's how we could do it:
df = pd.read_csv("data/mouse_heart_gene_expression.tsv", sep="\t")
column_means = df.mean()
mask = (
    (df["Heart_WT_1"] > column_means["Heart_WT_1"])
    & (df["Heart_WT_2"] > column_means["Heart_WT_2"])
    & (df["Heart_WT_3"] > column_means["Heart_WT_3"])
    & (df["Heart_WT_4"] > column_means["Heart_WT_4"])
)
df[mask].head()
