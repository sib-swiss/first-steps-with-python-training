# ******************************************************************************
# Micro Exercise 1
# ****************
a = 10
42 + "a"
# Trying to run: 42 + "a"
#  -> TypeError: unsupported operand type(s) for +: 'int' and 'str'

42 + a
"42" + "a"  # Correct syntax, but probably not what was intended.
# ******************************************************************************


# ******************************************************************************
# Micro Exercise 2
# ****************
# Convert "a" to an integer:

a = "42"
a = int(a)
print("type of 'a' after conversion:", type(a), ", a = ", a)

# If the string represents a fractional number, then int(a) will not work.
# To make it work, we must first convert to float, then to int.
a = "42.0"

a = int(float(a))
print("type of 'a' after conversion:", type(a), ", a = ", a)

# ******************************************************************************


# *****************************************************************************
# Micro Exercise 3
# ****************
# The exercise itself is basic, but it's a good opportunity to show why it is
# important to use variables in code:

# Start with everything hardcoded...
print("The product of 348 and 157.2 is:", 348 * 157.2)
print("Is this > than 230 squared [", 230**2, "]?: ", (348 * 157.2) > (230**2), sep="")

# Then change to variables...
a = 348
b = 157.2
c = 230
product_ab = a * b
squared_c = c**2
print("The product of", a, "and", b, "is:", product_ab)
print("Is this > than 230 squared [", squared_c, "]?: ", product_ab > squared_c, sep="")

# *****************************************************************************

# *****************************************************************************
# Micro Exercise 4
# ****************
# Extract the last 3 letters from name using slicing.
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
# Micro Exercise 5
# ****************
# Concatenate and slice lists.
l1 = [0, 1, 2, 3]
l1 = list((0, 1, 2, 3))
l1 = list(range(4))
print(l1)

l1.extend([4, 5])
# l1 += [4, 5]
print(l1)


print("The fourth element is:", l1[3])
print("The fourth element is:", l1[-3])

# This prints "None" because the ".append()" method returns None, and print
# prints whatever object the evaluated expression returns.
print(l1.append("something"))

# The .remove() method deletes the first element that matches the specified
# value (here 5) from the list.
l = [6, 5, 5, 4, 3, 2, 1]
l.remove(5)
print(l)
l = [6, 5, 5, 4, 3, 2, 1]
l.pop(5)
print(l)
# *****************************************************************************
