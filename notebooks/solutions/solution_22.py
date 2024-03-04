# Note for the correction:
# We here allow the population to be float numbers, but one could also
# constrain it to be integers only

# 1. Simulate a few generation. How large is the population after 3 generations?
pop = 1000
growth_factor = 1.5
print("generation 0 - population:", pop)

pop *= growth_factor  # 1st generation: population is multiplied by growth factor.
print("generation 1 - population:", pop)
pop *= growth_factor  # 2nd generation: population is multiplied by growth factor.
print("generation 2 - population:", pop)
pop *= growth_factor  # 3rd generation: population is multiplied by growth factor.
print("generation 3 - population:", pop)

# As can be seen here, duplicating code is sort of possible when we only do a
# few generation, but it quickly becomes tedious and error prone. So using a
# loop is a much better solution.
pop = 1000
growth_factor = 1.5
for generation in range(3):
    pop *= growth_factor
    print("generation", generation, "- population:", pop)


# 2. Use a while loop to simulate the population until it reaches 10'000
#    individuals or more. How many generation does it take?

# Initialization.
pop = 1000
growth_factor = 1.5
generation = 0

## While the population is under 10'000, we continue to grow it.
while pop < 10_000:
    pop *= growth_factor
    generation += 1
    print("generation", generation, "- population:", pop)

print(
    "It takes",
    generation,
    "generations to reach 10'000 or more individuals. "
    "The actual population at that point is:",
    pop,
)


#  3. How does the above change if the population starts at 100 individuals?

# All we have to do is change the initial population size to 100 in the code
# that we wrote for point 2 above.
pop = 100
