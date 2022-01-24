import matplotlib.pyplot as plt
import numpy as np   # This is only needed for the "Bonus" section at the end.
                     # Not needed for the actual exercise.


height = [150, 152, 152, 152, 152, 152, 152, 152, 155, 155, 155, 155, 155, 155, 
          155, 155, 155, 155, 157, 157, 157, 157, 157, 157, 157, 157, 160, 160, 
          160, 160, 160, 160, 160, 160, 160, 160, 160, 163, 163, 163, 163, 163, 
          163, 163, 163, 163, 163, 163, 165, 165, 165, 165, 165, 165, 165, 165, 
          168, 168, 168, 168, 168, 168, 168, 168, 168, 168, 168, 168, 168, 168, 
          170, 170, 170, 170, 170, 170, 170, 173, 173, 173, 173, 173, 173, 173, 
          173, 173, 173, 173, 175, 175, 175, 175, 175, 175, 175, 178, 178, 178, 
          178, 178, 178, 178, 180, 180, 180, 183, 183, 183, 183, 183, 183, 183, 
          183, 183, 183, 183, 183, 185, 188, 188, 191, 193]
weight = [73, 72, 45, 59, 95, 62, 54, 68, 77, 92, 83, 56, 47, 77, 63, 81, 52, 
          110, 54, 59, 61, 90, 81, 63, 63, 59, 52, 77, 50, 63, 58, 72, 63, 65, 
          69, 59, 72, 67, 59, 59, 65, 77, 61, 111, 93, 74, 68, 59, 68, 50, 77, 
          74, 65, 72, 77, 86, 61, 65, 53, 60, 67, 99, 61, 70, 97, 54, 88, 99, 
          68, 70, 56, 86, 63, 65, 72, 81, 68, 79, 70, 81, 79, 85, 99, 77, 71, 
          81, 89, 72, 106, 56, 90, 81, 87, 81, 94, 83, 77, 94, 86, 95, 77, 77, 
          92, 77, 77, 131, 97, 101, 108, 99, 90, 91, 86, 113, 126, 104, 81, 77, 
          117, 63, 68, 101]
gender = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
          2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 
          2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 
          1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 
          1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
          1, 1, 1, 1, 1, 1, 1]

# Generate a marker color list, with "teal" color for males (gender == 1) and
# "darkorange" for females (gender == 2)

# Method 1: using a for loop:
marker_color = []
for x in gender:
    if x == 1:
        marker_color.append('teal')
    elif x == 2:
        marker_color.append('darkorange')

# Method 2: using list comprehension:
marker_color = ["teal" if x == 1 else "darkorange" for x in gender]

# Plot height and weight as a scatter plot.
plt.figure(figsize=(8, 5))
plt.scatter(weight, height, c=marker_color)
plt.title("Height vs Weight")
plt.xlabel('Weight [kg]')
plt.ylabel('Height [cm]')


# ******************************************************************************
# Bonus section: display centroids of male and female distributions with
# "vlines()" and "hlines()".
for gender_code in [1, 2]:
    sub_weight = [weight[index] for index, sex in enumerate(gender) if sex == gender_code]
    sub_height = [height[index] for index, sex in enumerate(gender) if sex == gender_code]
    mean_weight = np.mean(sub_weight)
    mean_height = np.mean(sub_height)
    plt.vlines(x=mean_weight, ymin=min(sub_height), ymax=max(sub_height), 
               color="blue" if gender_code == 1 else "red", linestyle="dashed")
    plt.hlines(y=mean_height, xmin=min(sub_weight), xmax=max(sub_weight), 
               color="blue" if gender_code == 1 else "red", linestyle="dashed")
# ******************************************************************************


# Render plot.
plt.show()


