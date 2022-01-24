
import time

# To see what the "sleep()" function does, we print its help:
# Reading the help we learn that "time.sleep()" will pause
# code execution for 3 seconds.
print(help(time.sleep))


# Example usage:
for x in range(5):
    print("pausing code execution for 3 seconds...")
    time.sleep(3)

