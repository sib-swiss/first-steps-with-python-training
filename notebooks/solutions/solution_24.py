
quote = (
    "Brave Sir Robin ran away. Bravely ran away away. "
    "When danger reared it's ugly head, he bravely turned his tail and fled. "
    "Brave Sir Robin turned about and gallantly he chickened out..."
)

letter_count = {}  # Instantiate an empty dictionnary.
for letter in quote:

    # Test whether the current letter is already present in the dictionnary.
    if not letter in letter_count:
        # If not, initialize its count value to 0.
        letter_count[letter] = 0

    # Increment the number of times the letter has been seen in the quote.
    letter_count[letter] += 1


# Let's now print the results:
for letter in letter_count.keys():  # for each key in the dictionnary
    print("'", letter, "' is present ", letter_count[letter], " times", sep="")


# Bonus: iterating over key value pairs in a dictionary can be elegantly
# achieved using a dictionary's "items()" method:
for letter, count in letter_count.items():
    print("'", letter, "' is present ", count, " times", sep="")


# Alternative implementation, using the "count()" method of str
# *************************************************************
letter_count = {}       # Instantiate an empty dictionnary.
for letter in quote:
    if not letter in letter_count:
        letter_count[letter] = quote.count(letter)

for letter, count in letter_count.items():
    print(letter, "->", count)


# Bonus: one liner, using set() and dictionary comprehension
# **********************************************************
# Note: set(quote) creates a "list" of unique characters in "quote".
for letter, count in {x: quote.count(x) for x in set(quote)}.items():
    print(letter, "->", count)

# To count only letters and ignore upper/lower case:
for letter, count in {x:quote.count(x) for x in sorted(set(quote.lower())) if x.isalpha()}.items():
    print(letter, "->", count)
