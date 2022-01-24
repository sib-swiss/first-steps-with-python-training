
my_string = "0123456789abcdef"

# The 2 is the step/increment between each selected index in the sequence.
# In this case, every 2nd letter is kept.
print(my_string[0:10:2])

# This allows the following neat trick to reverse a string: have steps of -1
print(my_string[::-1])
