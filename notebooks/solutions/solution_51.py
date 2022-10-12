
# 1. Create a pandas DataFrame
# ****************************
import pandas as pd

# Option 1: create data frame and assign index in a two steps.
data = {
    "row_position": range(100),
    "index": range(1, 101),
    "random_text": "hello from pandas",
}
df = pd.DataFrame(data)
df.index = df["index"]

# Note: alternatively, we can also use the "set_index()" method.
#  -> use "drop = False" to keep the column used as index.
#     By default drop = True.
#  -> use "inplace = True" to modify the original DataFrame, otherwise
#     a new DataFrame is returned.
df.set_index("index", drop=False, inplace=True)


# Option 2: create data frame and assign index in a single command.
# Note that with this option, the index is does not get an associated label.
df = pd.DataFrame(data, index=range(1, 101))

# Print the first and last 5 rows.
print(df.head())  # print first 5 rows.
print(df.tail())  # print last 5 rows.
df  # Displaying the DataFrame object will show the 5 first and last rows.


# 2. Create a selection of the first 7 rows
# *****************************************
print("\nFirst 7 rows:\n", df.loc[1:7, ["row_position", "index"]])
print("\nFirst 7 rows:\n", df.iloc[0:7, 0:2])


# 3. Add a new "reverse_index" column
# ***********************************
df["reverse_index"] = 100 - df["row_position"]
df

# 4. Delete the "index" column
# ****************************
df.drop("index", axis=1, inplace=True)
# Alternative: del df["index"]

# 5. Select row numbers multiple of 11
# ************************************
df.loc[df.index % 11 == 0, df.columns[0:2]]
