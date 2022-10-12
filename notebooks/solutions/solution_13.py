
# 1. Store our favorite quote as a string variable.
# ************************************************
my_quote = "Regarde-moi, mon cher, et dis moi quelle espérance pourrait bien me laisser cette protubérance!"


# 2. Replace all spaces by '@' characters in the quote.
# ****************************************************
# Since my_quote is a string, we look at "help(str)" to search for methods
# available for string objects. We can see that there is a "replace()"
# method that allows replacing characters within a string.
modified_quote = my_quote.replace(" ", "@")
print(my_quote)
print(modified_quote)


# Alternative using the "split" and "join" method: we split the quote on
# whitespaces (removing all spaces), and then concatenate the words back
# using "@", essentially replacing white spaces with "@".
# Note that this will also e.g. replace "\t" and "\n", since the are
# white spaces, unless we explicitly pass " " to split().
print("@".join(my_quote.split()))
print("@".join(my_quote.split(" ")))  # to avoid replacing "\t" or "\n"
