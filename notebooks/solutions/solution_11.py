# Exercise 1.2

# 1. 

# The problem is that "a" is an "int" and "b" is a "str".
#  -> solution: we have to convert "b" to a number type (int or float)
#     in order for the division to work.
a = 12
b = "36"
division = int(b) / a
print(division)

# 2. what if `b = "36.2"`

# Note that if we use "int(b)", then the code will fail if "b" is set to
# a fractional value. Using float(b) makes the code more resistant to
# different user inputs as it will convert both inputs with and without
# fractional values.
a = 12
b = "36.2"
division = float(b) / a
print(division)

# 3. what if `a = "12"`

a = "12"
b = "36"
division = int(b) / int(a)
print(division)
