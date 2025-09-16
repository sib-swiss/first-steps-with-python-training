# *****************************************************************************
# Micro Exercise 1
# ****************
# Create a variable named `word` and set its value to "shrubbery".
# Write an `if... else` block that prints a text indicating whether
# the word is a long (> 5 chars) or a short word.

word = "shrubbery"

if len(word) > 5:
    print("This is a long word")
else:
    print("This is a short word")


# Same as above, but using the ternary operator.
print("This is a", "long" if len(word) > 5 else "short", "word")
print(f'This is a {"long" if len(word) > 5 else "short"} word')
# *****************************************************************************


# *****************************************************************************
# Micro Exercise 2
# ****************
# Set the value of a and/or b so that the expression becomes `False`.
#  -> change "a" or "l" so that "a" is no longer in "l".
#  -> change "b" or "l" so that "b" is no longer in "l".
# Note: the precedence of operations means that the the expression is
#       evaluated as if it was: (not a in l) or (a > 0 and not b in l)

a = 7
b = 22
l = [7, 125, 48, 52, 2, 22, 1]

if a not in l or (a > 0 and b not in l):
    print("Success")
else:
    print("This is all false...")

# *****************************************************************************


# *****************************************************************************
# Micro Exercise 3
# ****************
# 1. Use a while loop to create a list containing the multiples of 13 that
#    are under 100.
# 2. Then use a for loop to go though this list and print its elements.

multiples = []
x = 0
while x < 100:
    multiples.append(x)
    x += 13

for x in multiples:
    print(x)


# In real life, we would probably use "range()" for this task:
multiples = list(range(0, 101, 13))

# Less efficient alternative.
multiples = []
x = 0
while x < 100:
    if x % 13 == 0:
        multiples.append(x)
    x += 1

# *****************************************************************************
