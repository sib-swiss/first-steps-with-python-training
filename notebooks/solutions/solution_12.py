
a = 12
b = "36"
# The problem here, is that "a" in an int(), and "b" is a str().
# -> we have to convert "b" to a number type (int or float) in order
# for the division to work.
division = int(b) / a
print(division)

# Note that if we use "int(b)", then the code will fail if the  input "b"
# is set to a fractional value. Using float(b) makes the code more
# resistant to diffent user inputs as it will convert both inputs with and
# without fractional values.
a = 12
b = "36.7"
division = float(b) / a
print(division)
