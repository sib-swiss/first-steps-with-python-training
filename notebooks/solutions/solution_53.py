# Exercise 5.3

# In the code below, we will not presume that the features are ordered by
# chromosome and position, and therefore we will read through the entire file.
#
# However, if that assumption can be made, then it could be good way to
# terminate the reading early, and save some execution time if the input file
# is very big (e.g. the gtf file of the full human genome is ~2 GB).

to_report = []
input_path = "data/Homo_sapiens.GRCh38.99.MT.gtf"

with open(input_path, "r") as in_file:
    for line in in_file:
        # The file is tab delimited: we split by tab.
        split_line = line.split("\t")

        # The 1st column of the file contains the chromosome info.
        # The 3rd column contains the feature info.
        chromosome = split_line[0]
        feature = split_line[2]

        # The 4th and 5th columns contain the start and end coordinates
        # of the features (e.g. genes).
        # Note that we since the elements returned by .split() are strings,
        # we must convert start/end to int().
        start = int(split_line[3])
        end = int(split_line[4])

        # The 7th column contains the strand info: + = forward; - = reverse.
        is_forward_strand = split_line[6] == "+"

        if (
            chromosome == "MT"
            and feature == "gene"
            and is_forward_strand
            and start > 7500
            and end < 10000
        ):
            to_report.append(line)

for line in to_report:
    print(line, end="")


# Alternative solution that uses "iterable unpacking".
input_path = "data/Homo_sapiens.GRCh38.99.MT.gtf"

with open(input_path, mode="r") as f:
    for line in f:
        chromosome, _, feature, start, end, _, strand = line.strip().split("\t")[:7]

        if (
            chromosome == "MT"
            and feature == "gene"
            and strand == "+"
            and int(start) > 7500
            and int(end) < 10000
        ):
            print(line)
