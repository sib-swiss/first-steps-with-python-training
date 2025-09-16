import pandas as pd

# *****************************************************************************
# Micro Exercise 1 - create a DataFrame and Series
# ************************************************
# Create a new DataFrame named "df_test":
size_data = {
    "Name": ["Alice", "Bob", "Jim", "Zoe"],
    "Height": [163, 180, 172, 173],
    "Weight": [58, 97, 63, 60],
}
df_size = pd.DataFrame(size_data)

# Create a Series named age:
age = pd.Series([33, 25, 31])

# Print DataFrame and Series info:
print("DataFrame row count:", df_size.shape[0])
print("DataFrame column count:", df_size.shape[1])
print("Series length:", len(age))
print("Series values:\n", age, sep="")
df_size


# Bonus: create a dictionary with "zip()"
name_values = ["Alice", "Bob", "Jim", "Zoe"]
height_values = [163, 180, 172, 173]
weight_values = [58, 97, 63, 60]
col_names = ["Name", "Height", "Weight"]
dict(zip(col_names, [name_values, height_values, weight_values]))
# *****************************************************************************


# *****************************************************************************
# Micro Exercise 2 - read and write data frames
# *********************************************
# Read the titanic.csv file from disk and save it to a variable named titanic_df.
titanic_df = pd.read_csv("data/titanic.csv")

# Create a new DataFrame that only contains the first 10 rows. Save it as a
# tab-delimited .txt file.
titanic_df_head = titanic_df.head(10)
titanic_df_head.to_csv("data/titanic_head.txt", sep="\t")

# Same as above but in a single line.
titanic_df.head(10).to_csv("data/titanic_head.txt", sep="\t")
# *****************************************************************************


# *****************************************************************************
# Micro Exercise 3 - editing a DataFrame
# **************************************
# Add an entry to the DataFrame for "Tim".
df_size.loc[df_size.shape[0]] = ["Tim", 191, 95]
df_size

# Add a "BMI" (Body Mass Index) column.
df_size["BMI"] = df_size["Weight"] / (df_size["Height"] / 100) ** 2
df_size
# *****************************************************************************


# *****************************************************************************
# Micro Exercise 4 - DataFrame selection
# **************************************
# Select passengers from the Barber family.
df.loc[df["Last_name"] == "Barber",]

# Select passenger that are either american, or older than 30 years.
mask = (df["Nationality"] == "USA") | (df["Age"] > 30)
df.loc[mask,]

# Select british passengers that are either women or men traveling 1st class.
mask = (df["Nationality"] == "UK") & (
    (df["Gender"] == "female") | ((df["Gender"] == "male") & (df["Pclass"] == 1))
)
df.loc[mask,]

# *****************************************************************************


# *****************************************************************************
# Micro Exercise 5 - summary statistics
# *************************************
# Which proportion of women and men survived the tragedy:
print("Survival rate among women:", df.loc[df["Sex"] == "female", "Survived"].mean())
print("Survival rate among men  :", df.loc[df["Sex"] == "male", "Survived"].mean())

for gender in ("male", "female"):
    survival_rate = df.loc[df["Sex"] == gender, "Survived"].mean()
    print(f"Survival rate in {gender}: {round(survival_rate, 2)}")

# Alternative:
for gender in ("male", "female"):
    subset = df.loc[df["Sex"] == gender]
    print(
        f"Survival rate in {gender}:",
        round(subset["Survived"].sum() / subset.shape[0], 2),
    )

# More alternatives...
df.loc[df["Sex"] == "male", "Survived"].sum() / (df["Sex"] == "male").sum()
df.loc[df["Sex"] == "male", "Survived"].sum() / df.loc[df["Sex"] == "male",].shape[0]
# *****************************************************************************


# *****************************************************************************
# Micro Exercise 6 [Additional Theory] - applying custom functions
# ****************************************************************
# Write your own implementation of the mean() function, then apply it to
# the "Age" and "Fare" columns

# Implementation using a function that skips NaN values:
import math


def calculate_mean(seq):
    total = 0
    count = 0
    for x in seq:
        if not math.isnan(x):
            total += x
            count += 1
    return total / count


print(df.loc[:, ["Age", "Fare"]].apply(calculate_mean))
print(df.loc[:, ["Age", "Fare"]].mean())


# Alternative implementation using statistics.mean()
import math
import statistics


def calculate_mean_2(seq):
    return statistics.mean([x for x in seq if not math.isnan(x)])


print(df.loc[:, ["Age", "Fare"]].apply(calculate_mean_2))


# Implementation using a function that does not support NaN, but
# where NaN values are dropped from the DataFrame before the function
# is applied.
def calculate_mean_3(seq):
    total = 0
    for x in seq:
        total += x
    return total / len(seq)


print(df.dropna().loc[:, ["Age", "Fare"]].apply(calculate_mean_3), "\n")
print(df.dropna().loc[:, ["Age", "Fare"]].mean(), "\n")
# *****************************************************************************


# *****************************************************************************
# Micro Exercise 7: grouping data by factor.


def age_category(x):
    age_classes = {"child": 12, "teenager": 17, "adult": 64, "senior": 200}
    for label, threshold in age_classes.items():
        if x <= threshold:
            return label


# Make a copy of the "df" DataFrame.
dfc = df.copy()

# Add a new column "Age_category".
dfc["Age_category"] = df["Age"].map(age_category)
# or
dfc["Age_category"] = df["Age"].apply(age_category)

# Compute survival rates by gender, age category and passenger class.
dfc.groupby(["Sex", "Age_category", "Pclass"]).mean()

# *****************************************************************************


# *****************************************************************************
# Micro Exercise X (was part of Additional Theory section)
# ****************
df = pd.read_csv("data/titanic_no_header.csv", header=None)
df.head()

# Make the first column the index of the DataFrame
df.index = df[0]
df.drop(0, axis=1, inplace=True)  # alternative: del df[0]
df.index.name = None
df.head()

# Alternatively, the "set_index()" method can be used to set the index and
# delete the first column in a single column.
df.set_index(0, drop=True, inplace=True)
df.index.name = None

# Change column names:
df.columns = ("Name", "Sex", "Age", "Pclass", "Survived", "Family", "Fare", "Embarked")
df.head()

# *****************************************************************************
