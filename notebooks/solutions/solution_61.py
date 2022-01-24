import matplotlib.pyplot as plt

time = [0, 1.85, 2.87, 3.78, 4.65, 5.50, 6.31, 7.14, 7.96, 8.79, 9.69]
distance = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
velocity = [0, 5.41, 9.80, 10.99, 11.49, 11.76, 12.35, 12.05, 12.20, 12.05, 11.11]
acceleration = [0, 2.92, 4.30, 1.31, 0.57, 0.32, 0.73, -0.36, 0.18, -0.18, -1.04]


# Solution using procedural mode
# ******************************

# Create a new plot with the distance, velocity and acceleration vs. time data.
plt.plot(time, distance, label='distance [m]')
plt.plot(time, velocity, label='velocity [m/s]')
plt.plot(time, acceleration, label='acceleration [m/s^2]')

# Add X and Y axis labels.
plt.xlabel('Time [s]')
plt.ylabel('Distance [m]')

# Set a title and a legend for the figure.
# Note the use of the "fontsize" and "markerscale" arguments to adjust the
# size of the legend.
plt.title('Usain Bold 100m gold medal sprint - Beijing 2008')
plt.legend(fontsize=12, markerscale=1.2)

# Display the figure.
plt.show()



# Solution using object-oriented mode
# ***********************************

# Create a new figure object, adjust the size.
fig = plt.figure(figsize=(10, 5))

# Create an axis object (a subplot). Add the distance, velocity and 
# acceleration vs. time data.
ax = fig.add_subplot()
ax.plot(time, distance, label='distance [m]', markersize=5)
ax.plot(time, velocity, label='velocity [m/s]', color='teal', markersize=5)
ax.plot(time, acceleration, label='acceleration [m/s^2]', color='darkorange')

# Add X and Y axis labels.
ax.set_xlabel('Time [s]')
ax.set_ylabel('Distance [m]')

# Set a title and a legend for the figure.
# Note the use of the "fontsize" and "markerscale" arguments to adjust the
# size of the legend.
ax.set_title('Usain Bold 100m gold medal sprint - Beijing 2008')
ax.legend(fontsize=12, markerscale=1.2)

# Display the figure.
plt.show()


