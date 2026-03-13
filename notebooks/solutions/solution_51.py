# Exercise 5.1


# Define a function that copies the 10 first lines of a file to an output file.
def head_copy(input_file, output_file):
    """Writes the first 10 lines of `input_file` to a new file `output_file`."""

    with open(input_file, "r") as in_file, open(output_file, "w") as out_file:
        for i in range(10):
            print(in_file.readline(), file=out_file, end="")
            # Note: we add the optional end="" argument to the "print()" function
            # to avoid printing an additional "\n" character (newline).
            # Alternatively we could have used `.strip()` on the lines read from
            # the input file: print(in_file.readline().strip(), file=out_file)

    return None


# Notes:
# To read a file with python in a Jupyter Notebook, we must specify its
# location relatively to our notebook. Since the file is located in a the
# "data" subdirectory, we must add "data/" to the input file name.
input_file_path = "data/Homo_sapiens.GRCh38.99.MT.gtf"
output_file_path = "Homo_sapiens.GRCh38.99.MT.head.gtf"
head_copy(input_file_path, output_file_path)
