
# This solution relies on the method .isdigit() of str which returns "True"
# if all characters in a string are digits.

def split_numbers_and_words(line):
    """takes a string mixing letters and digits and transform it into a list
    of the words (groups of letters) and numbers (group of digits) of the string.
    """
    split_line = []  # This will store the return value: the splitted input line.

    # Handle the special case of an empty input string.
    # Note that "not line" is simply a shortcut for "len(line) == 0"
    if not line:
        return split_line

    # stores whether the previous character was a digit.
    previous_is_digit = line[0].isdigit()
    current_group = ""  # Store the word or number we are currently reading.

    for c in line:
        current_is_digit = c.isdigit()  # Is the current character a digit?

        # Ihe current character has the same status than the previous
        # character: -> the word or number grows.
        if current_is_digit == previous_is_digit:
            current_group += c

        # If the current character does not have the same status than the
        # previous character: -> indicates the end of a word or number.
        else:
            # If the group we just completed is a number, convert it to int.
            if previous_is_digit:
                current_group = int(current_group)

            # Add the newly detected word or number to the list of results.
            split_line.append(current_group)

            # Now we start a new word with the current character.
            current_group = c
            previous_is_digit = current_is_digit

    # Now, the last thing we need to do is to add the last group to our
    # output list.
    if previous_is_digit:
        # If we are building a number, convert it to an integer
        current_group = int(current_group)
    split_line.append(current_group)

    return split_line


test_string = "Nobody0expects42the2048Spanish1492Inquisition!"
print(test_string, "\n\t->", split_numbers_and_words(test_string))
