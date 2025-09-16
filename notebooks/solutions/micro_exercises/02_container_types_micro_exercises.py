# *****************************************************************************
# Micro Exercise 1
# ****************
# Extract the last 3 letters from your name using slicing.
name = "Alice"
name[2:5]
name[2:]

# This solution does not work on every name.
name = "Charlotte"
name[2:]

# This last solution works on every name >= 3 chars.
name = "Alice"
name[-3:]
# *****************************************************************************


# *****************************************************************************
# Micro Exercise 2
# ****************
# Concatenate and slice lists.
l = [0, 1, 2, 3]
l = list(range(4))
print(l)

l.extend([4, 5])  # Alternatively: l += [4, 5]
print(l)

# Print the fourth and last element of the list.
print("The fourth element is:", l[3])
print("The last element is:", l[-1])
# This would also work to print the last element, but is suboptimal.
print("The last element is:", len(l) - 1)

# This prints "None" because the ".append()" method returns None, and print
# prints whatever object the evaluated expression returns.
print(l.append("something"))

# The .remove() method deletes the first element that matches the specified
# value (here 5) from the list.
l = [6, 5, 5, 4, 3, 2, 1]
l.remove(5)
print(l)
l = [6, 5, 5, 4, 3, 2, 1]
l.pop(5)
print(l)
# *****************************************************************************
