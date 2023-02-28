"""This is a test module for demonstration purpose. This part of the module
   is called the 'module docstring' and can be used to add a description of
   the module.
"""

DEFAULT_USER = "Alice"


def greeting(name=""):
    """Prints a greeting addressed to the person specified
    person passed as name argument.

    name:
        name of the person to greet.
    """
    if name:
        print("Hello,", name)
    else:
        print("Hello, stranger.")
