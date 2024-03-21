import json
import matplotlib.pyplot as plt
import numpy as np

# Read data from JSON file
with open('./star_systems.json', 'r') as f:
    data = json.load(f)

# Convert XY coordinates to polar coordinates
polar_coordinates = []
for star_system in data['star_systems']:
    x, y = star_system['x'], star_system['y']
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)  # Angle in radians
    polar_coordinates.append((theta, r))

# Plotting the radar plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
for theta, r in polar_coordinates:
    ax.plot(theta, r, 'bo')  # Plotting each star system as a blue dot

plt.show()