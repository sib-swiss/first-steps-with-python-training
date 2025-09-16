# Exercise 5.1

# Notes:
# To read a file with python in a Jupyter Notebook, we must specify its
# location relatively to our notebook. Since the file is located in a the
# "data" subdirectory, must add "data/" to the input file name.

input_file = "data/Homo_sapiens.GRCh38.99.MT.gtf"
output_file = "Homo_sapiens.GRCh38.99.MT.head.gtf"

with open(input_file, "r") as in_file, open(output_file, "w") as out_file:
    for i in range(10):
        print(in_file.readline(), file=out_file, end="")
        # Note: we add the optional end="" argument to the "print()" function
        # to avoid printing an additional "\n" character (newline) printed,
        # since that would cause line skips (because each line already ends
        # with a `\n` character read when read from the file).
        # Alternatively we could have used `strip()` on the lines read from
        # the input file: print(in_file.readline().strip(), file=out_file)

# Verify that the file we created above is correct by reading it.
# It should contain 10 lines.
file_content = []
with open(output_file, mode="r") as f:
    for line in f:
        file_content.append(line)

print("The file has", len(file_content), "lines")
for line in file_content:
    print(line)


# Note: in practice, reading a file line-by-line just to store its content
# in a list does not make much sense. It's simpler to use readlines() in that
# case, since we are anyway loading the whole file in memory.
with open(output_file, mode="r") as f:
    file_content = f.readlines()

print("The file has", len(file_content), "lines")
for line in file_content:
    print(line)
