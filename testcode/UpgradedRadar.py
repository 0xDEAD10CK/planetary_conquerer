import json
import matplotlib.pyplot as plt
import numpy as np

def generate_star_systems(num_systems):
    star_systems = []
    for i in range(num_systems):
        x = np.random.randint(-50, 50)
        y = np.random.randint(-50, 50)
        star_systems.append({"name": f"System{i+1}", "x": x, "y": y})
    return star_systems

def convert_to_polar_coordinates(systems):
    polar_coordinates = []
    for system in systems:
        x, y = system['x'], system['y']
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(y, x)  # Angle in radians
        polar_coordinates.append((theta, r))
    return polar_coordinates

def move_systems(systems, central_system, new_central_system):
    dx = new_central_system['x'] - central_system['x']
    dy = new_central_system['y'] - central_system['y']
    
    # Move the systems relative to the new central system
    for system in systems:
        if system['x'] >= central_system['x']:
            system['x'] += dx
        else:
            system['x'] -= dx
        
        if system['y'] >= central_system['y']:
            system['y'] += dy
        else:
            system['y'] -= dy



# Generate 50 star systems
star_systems = generate_star_systems(50)

# Select an initial central system
initial_central_system = np.random.choice(star_systems)

# Convert XY coordinates to polar coordinates relative to the initial central system
polar_coordinates = convert_to_polar_coordinates(star_systems)

# Plotting the radar plot
def plot_systems(polar_coordinates, systems):
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    for (theta, r), system in zip(polar_coordinates, systems):
        ax.plot(theta, r, 'ro')  # Plot each star system as a red dot
        ax.text(theta, r, system['name'], verticalalignment='bottom', horizontalalignment='right')
    ax.plot(0, 0, 'bo')  # Plot initial central system at the center
    plt.show()

plot_systems(polar_coordinates, star_systems)

# Suppose the user selects a new central system
new_central_system = np.random.choice(star_systems)

# Move systems to reflect the change in central system
move_systems(star_systems, initial_central_system, new_central_system)

# Convert XY coordinates to polar coordinates relative to the new central system
polar_coordinates = convert_to_polar_coordinates(star_systems)

# Plotting the radar plot with updated positions
plot_systems(polar_coordinates, star_systems)
