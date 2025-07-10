# *****************************************************************************
# Micro Exercise 1 - reading a file with a for loop
# *************************************************
# Read the content of "data/titanic_head.csv" and print it. Make sure
# no white space is printed between lines.

input_file = "data/titanic_head.csv"
with open(input_file, mode="r") as f:
    for line in f:
        print(line.strip())

# *****************************************************************************


# *****************************************************************************
# Micro Exercise 2 - copy a file's content
# ****************************************
input_path = "shopping_list.txt"
output_path = "shopping_list_copy.txt"

with open(input_path, mode="r") as in_file, open(output_path, mode="w") as out_file:
    for line in in_file:
        line = line.strip()
        print(line)
        print(line, file=out_file)

# *****************************************************************************
