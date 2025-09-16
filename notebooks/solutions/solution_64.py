# Exercise 6.4

# 1. What does is_part_of_set do?
# *******************************
from exercise_44_module import is_part_of_set

# help(is_part_of_set)
# "is_part_of_set()" returns True if its argument is a prime number
# and False otherwise.

for n in range(10):
    print(n, "->", is_part_of_set(n))


# 2 and 3. Use is_part_of_set to get all primes numbers between 2 and 50000
# *************************************************************************
from exercise_44_module import is_part_of_set
from time import time

primes = []

# Get the current time, so we can compute elapsed time at the end.
t0 = time()
for i in range(50000):
    if is_part_of_set(i):
        primes.append(i)

time_first_algo = time() - t0
print("it took", time_first_algo, "seconds")
print("found", len(primes), "prime numbers")


# Optional: devise a more time efficient way of getting the prime numbers
# ***********************************************************************
#
# Principle: rather than testing each number separately, we test the whole
# set of numbers at once by going over all number and "eliminating" all
# multiples of that number.
from time import time

t0 = time()

# Phase1 : initialization
upperLimit = 50000

# Create a list that contains True for all numbers we want to test.
# During the algorithm we will set all non-prime numbers to False.
arePrime = [True] * (upperLimit + 1)
arePrime[0] = False  # 0 is not prime
arePrime[1] = False  # 1 is not prime


# Phase2 : go through all numbers
primes2 = []

for i in range(2, upperLimit + 1):  # for each candidate number

    # only do something if that number has not been set as a non-prime before
    if arePrime[i]:
        primes2.append(i)

        # then we want to set all multiples of that number as non-prime
        mult = 2 * i

        # all multiples until the upper limit is reached
        while mult <= upperLimit:
            arePrime[mult] = False  # set the multiple to non-prime
            mult += i  # nest multiple

time_second_algo = time() - t0

print("it took", time() - t0, "seconds")
print("speedup compared to first algorithm:", time_first_algo / time_second_algo)
print("found", len(primes2), "prime numbers")
print("is this list the same as with the first algorithm ?", primes == primes2)
