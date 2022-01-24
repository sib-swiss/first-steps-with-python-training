
# 1. Create a dictionary with the classification of the Python genus
# ******************************************************************
pythons = {
    "Class": "Reptilia",
    "Order": "Squamata",
    "Family": "Pythonidae",
    "Genus": "Python"
}


# 2. Add an entry for species
# ***************************
# Since we are asked to add 2 or more species, we must use some type of
# container object: e.g. a list or a tuple.
pythons["Species"] = ["molurus", "regius", "bivittatus"]


# 3. Print the lists of keys and values as two separate lists
# ***********************************************************
print("List of keys  :", list(pythons.keys()))
print("List of values:", list(pythons.values()))
