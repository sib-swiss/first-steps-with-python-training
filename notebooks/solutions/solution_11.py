# Exercise 1.1

my_string = "0123456789abcdef"

# The third value passed to the slicing operator (in our example the number 2)
# is the step/increment between each selected index in the sequence.
# In this case, every 2nd letter is kept.
print(my_string[0:10:2])

# Setting a custom step value also allows the following neat trick to reverse
# a string: have steps of -1.
print(my_string[::-1])
