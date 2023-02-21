# Imagine a population starting with 1000 individuals.
# Each generation the population is multiplied by 1.5. 

## note for the rest of the correction :
##  here I allow the population to be float numbers, 
##   but alternatively one could constrain it to be integers only

#  1. Simulate a few generation. How large is the population after 3 generations?
pop = 1000
growth_factor = 1.5
print("generation 0 - population:",pop)
pop *= growth_factor # 1 generation : the population is multiplied by the growth factor
print("generation 1 - population:",pop)
pop *= growth_factor # 1 generation : the population is multiplied by the growth factor
print("generation 2 - population:",pop)
pop *= growth_factor # 1 generation : the population is multiplied by the growth factor
print("generation 3 - population:",pop)

print('***')
#  2. Use a while loop to simulate the population until it reaches 10 000 individuals or more. How many generation did it take?

## initialization
pop = 1000
growth_factor = 1.5
generation = 0

## while the population is under 10 000, we continue to grow it
while pop < 10000 :
    pop *= growth_factor
    generation += 1
    print("generation",generation,"- population:",pop)
print("it took",generation,"generations to reach 10000 (actual population is",pop,')')

print('***')
#  3. How does the above change if the population starts at 100 individuals? 

## we just have to change the initialization
pop = 100
growth_factor = 1.5
generation = 0

## while the population is under 10 000, we continue to grow it
while pop < 10000 :
    pop *= growth_factor
    generation += 1
    print("generation",generation,"- population:",pop)
print("it took",generation,"generations to reach 10000 (actual population is",pop,')')

