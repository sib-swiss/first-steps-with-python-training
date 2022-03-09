
# 1. What does "mysterious_function()" do?
# ****************************************
# "mysterious_function()" takes a number "n" and multiplies it by the result
# of "mysterious_function(n-1)", unless "n" is lower or equal to 1 in which
# case it returns 1.
#
# Let's see what happens with n = 4:
#   mysterious_function(4)  ->  4 * mysterious_function(3)
#   mysterious_function(4)  ->  4 * 3 * mysterious_function(2)
#   mysterious_function(4)  ->  4 * 3 * 2 * mysterious_function(1)
#   mysterious_function(4)  ->  4 * 3 * 2 * 1
#   mysterious_function(4)  ->  24
#
# So, "mysterious_function" computes the product of all positive integers
# lower or equal to "n". In other words, it computes a factorial !
# (see https://en.wikipedia.org/wiki/Factorial)

# Having a function calling itself is called a recursion.
# It is a method commonly used when the solution to a problem can be defined
# using solution(s) to smaller instance(s) of the same problem.


# 2. Write a function that gives the same result, but using a "for" loop
# **********************************************************************
def factorial_using_loop(n):

    # Treating the special case where n is lower or equal to 1.
    # Note: in fact this is not really needed, since the "for" loop below
    # does not run if n <= 1, and the function thus returns 1.
    if n <= 1:
        return 1  # Note: anytime the "return" keyword is called,
                  # we exit the function immediatly.

    # Loop through numbers from 1 to n.
    # Remember that in "range()"" the end point (second argument) is excluded.
    fact = 1
    for i in range(2, int(n) + 1):
        # Increment the factorial.
        fact *= i
        # print(fact)                # Print was used while debugging.
    return fact


# Testing our function with the number 4.
print("4! =", factorial_using_loop(4))
print("4! =", factorial_using_loop(4.0))
