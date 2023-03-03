# Exercise 4.2

import os    # Import the os module into the global namespace.


def count_files(dir_name):
    """Counts files present in the input directory.
    Only files are counted, directories are ignored.
    """
    
    # Initialize file counter.
    file_count = 0

    # Loop through all files and directories present in the input directory.
    for f in os.listdir(path=dir_name):

        # Get the absolute path of the file/directory.
        full_path = os.path.join(dir_name, f)

        # Verify the path corresponds to a file, not a directory.
        if os.path.isfile(full_path):
            file_count += 1

    return file_count


# Count the number of files in the parent directory of the current working
# directory.
parent_dir = os.path.dirname(os.getcwd())
print("File count in [", parent_dir, "]: ", count_files(parent_dir), sep="")


# Alternative version of the function using a list generator comprehension.
def count_files_2(input_dir):
    return sum(
        (1 for x in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, x)))
    )
