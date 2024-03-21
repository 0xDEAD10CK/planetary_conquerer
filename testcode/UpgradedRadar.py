import json
import matplotlib.pyplot as plt
import numpy as np

def generate_star_systems(num_systems):
    star_systems = []
    for i in range(num_systems):
        x = np.random.randint(-100, 100)
        y = np.random.randint(-100, 100)
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


def plot_systems(polar_coordinates, systems, central_system, max_range=10):
    # Extract polar coordinates and names
    thetas, rs = zip(*polar_coordinates)
    names = [system['name'] for system in systems]
    
    # Convert polar coordinates to Cartesian coordinates
    xs = np.array(rs) * np.cos(thetas)
    ys = np.array(rs) * np.sin(thetas)
    
    # Adjust the coordinates to center the plot around the central system
    central_x = central_system['x']
    central_y = central_system['y']
    xs -= central_x
    ys -= central_y
    
    # Filter systems based on maximum range
    visible_systems = [(x, y, name) for x, y, name in zip(xs, ys, names) if abs(x) <= max_range and abs(y) <= max_range]
    xs, ys, names = zip(*visible_systems)
    
    # Plot the systems
    plt.figure(figsize=(8, 8))
    plt.scatter(xs, ys, color='red')
    
    # Plot central system
    plt.scatter(0, 0, color='blue', label=central_system['name'])
    
    # Plot names
    for name, x, y in zip(names, xs, ys):
        plt.text(x, y, name, fontsize=8, verticalalignment='bottom', horizontalalignment='right')
    
    # Set limits
    plt.xlim(-max_range, max_range)
    plt.ylim(-max_range, max_range)
    
    # Set aspect ratio to equal
    plt.gca().set_aspect('equal', adjustable='box')
    
    # Show plot
    plt.legend()
    plt.grid(True)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Star Systems')
    plt.show()


# Generate 50 star systems
star_systems = generate_star_systems(100)

# Select an initial central system
initial_central_system = np.random.choice(star_systems)

# Convert XY coordinates to polar coordinates relative to the initial central system
polar_coordinates = convert_to_polar_coordinates(star_systems)


# Plot the star systems with the initial central system
plot_systems(polar_coordinates, star_systems, initial_central_system, max_range=10)


# Suppose the user selects a new central system
new_central_system = np.random.choice(star_systems)

# Plotting the radar plot with updated positions
plot_systems(polar_coordinates, star_systems, new_central_system, max_range=10)

