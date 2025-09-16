# Exercise 7.2

import pandas as pd

# 1. Read input files as data frames.
df_hosp = pd.read_csv("data/switzerland_covid19_hospitalized.csv")
df_demo = pd.read_csv("data/switzerland_demographics.csv")


# 2. Update the index of both DataFrames.
df_hosp.index = df_hosp["Date"]
df_demo.index = df_demo["Canton"]
df_demo.head()
df_hosp.head()


# 3. Subset the number of hospitalized person data frame.
# Keep only columns "AG" -> "CH" (i.e. the first 27 columns).
df_hosp = df_hosp.loc[:, "AG":"CH"]
df_hosp.head()


# 4. Extract population count per Canton
pop_by_canton = df_demo.loc[df_hosp.columns, "Population"]

# Note: as long as the index of the Series by which we divide (step 5 below)
# is matching the columns of the DataFrame, the order of the elements in
# Series does not matter. Therefore we can also simply do:
#
# pop_by_canton = df_demo["Population"]


# 5. Compute hospitalized people relative to population size
# Convert the number of hospitalized people from raw count to
# number per 10'000 inhabitants.
df_hosp /= pop_by_canton / 10000
df_hosp.head()


# 6. For each canton, date at which the hospitalization rate was maximal.
# one liner answer:
df_hosp.idxmax(axis=0)


# Additional tasks
# ****************
# Create new data frame with max hospitalized people and date.
df_max_hosp = pd.DataFrame({"MaxHosp": df_hosp.max(), "Date": df_hosp.idxmax(axis=0)})

df_max_hosp.sort_values("Date", ascending=True)
df_max_hosp.sort_values("MaxHosp", ascending=False)
