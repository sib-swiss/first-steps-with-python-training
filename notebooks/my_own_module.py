DEFAULT_USER = "Alice"


def greeting(name=""):
    """Prints a greeting addressed to the person specified
    person passed as name argument.

    name
        name of the person to greet.
    """
    if name:
        print("Hello,", name)
    else:
        print("Hello, stranger.")
