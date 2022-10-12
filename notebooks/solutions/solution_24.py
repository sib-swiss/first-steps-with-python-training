
quote = (
    "Brave Sir Robin ran away. Bravely ran away away. "
    "When danger reared it's ugly head, he bravely turned his tail and fled. "
    "Brave Sir Robin turned about and gallantly he chickened out..."
)

# Instantiate an empty dictionary.
letter_counts = {}

# Loop through the quote, one character at a time.
for char in quote:

    # Test whether the current character is already present in the dictionary.
    if not char in letter_counts:
        # If not, initialize its count value to 0.
        letter_counts[char] = 0

    # Increment the number of times the letter has been seen in the quote.
    letter_counts[char] += 1


# Let's now print the results by looping over each key in the dictionary.
# We additionally sort the output in alphabetical order.
for letter in sorted(letter_counts):
    print(letter, letter_counts[letter], sep=" -> ")


# Bonus: iterating over key value pairs in a dictionary can be elegantly
# achieved using a dictionary's "items()" method:
for letter, count in letter_counts.items():
    print("'", letter, "' is present ", count, " times", sep="")


# Implementation to keep only letters and ignore upper/lower cases
# ****************************************************************
letter_counts = {}
for char in quote.lower():

    # If the current character is not alphabetical (a letter), we
    # go straight to the next using the "continue" keyword.
    if not char.isalpha():
        continue

    # Test whether the current letter is already present in the dictionary.
    if not char in letter_counts:
        # If not, initialize its count value to 0.
        letter_counts[char] = 0

    # Increment the number of times the letter has been seen in the quote.
    letter_counts[char] += 1



# Alternative implementation, using the "count()" method of str
# *************************************************************
letter_counts = {}
for char in quote.lower():
    if char.isalpha() and char not in letter_counts:
        letter_counts[char] = quote.lower().count(char)

for letter in sorted(letter_counts):
    print(letter, letter_counts[letter], sep=" -> ")


# Bonus: one liner, using set() and dictionary comprehension
# **********************************************************
# Note: set(quote) creates a "list" of unique characters in "quote".
letter_counts = {x: quote.count(x) for x in set(quote)}

# Same as above, but counting only letters, ignoring upper/lower case
# differences, and in addition sorting the output alphabetically:
letter_counts = {x:quote.lower().count(x) for x in sorted(set(quote.lower())) if x.isalpha()}
for letter in sorted(letter_counts):
    print(letter, letter_counts[letter], sep=" -> ")
