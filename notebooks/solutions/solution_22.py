# Exercise 2.2

# 1. Store our favorite quote as a string variable
# ************************************************
quote = "Regarde-moi, mon cher, et dis moi quelle espérance pourrait bien me laisser cette protubérance!"
quote = "Are you suggesting coconuts migrate ?"

# 2. Replace all spaces by '@' characters in the quote
# ****************************************************
# Since "quote" is a string, we look at "help(str)" to search for methods
# of str objects. We can see that there is a "replace()" method that allows
# replacing characters within a string.
modified_quote = quote.replace(" ", "@")
print(quote)
print(modified_quote)


# Alternative using the "split()" and "join()" method: we split the quote
# on whitespaces (removing all spaces), and then concatenate the words
# back using "@", essentially replacing white spaces with "@".
# Note that this will also e.g. replace "\t" and "\n", since they are
# white spaces, unless we explicitly pass " " to split().
print("@".join(quote.split()))
print("@".join(quote.split(" ")))  # Avoids replacing "\t" or "\n"
