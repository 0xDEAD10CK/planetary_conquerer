import json
import matplotlib.pyplot as plt
import numpy as np

with open("universe.json", "r") as json_file:
        systems = json.load(json_file)

# def generate_star_systems(num_systems):
#     star_systems = []
#     for i in range(num_systems):
#         x = np.random.randint(-1000, 1000)
#         y = np.random.randint(-1000, 1000)
#         star_systems.append({"name": f"System{i+1}", "x": x, "y": y})
#     return star_systems

def convert_to_polar_coordinates(systems):
    polar_coordinates = []
    for system in systems:
        x, y = system['x-coord'], system['y-coord']
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(y, x)  # Angle in radians
        polar_coordinates.append((theta, r))
    return polar_coordinates


def move_systems(systems, central_system, new_central_system):
    dx = new_central_system['x-coord'] - central_system['x-coord']
    dy = new_central_system['y-coord'] - central_system['y-coord']
    
    # Move the systems relative to the new central system
    for system in systems:
        if system['x-coord'] >= central_system['x-coord']:
            system['x-coord'] += dx
        else:
            system['x-coord'] -= dx
        
        if system['y-coord'] >= central_system['y-coord']:
            system['y-coord'] += dy
        else:
            system['y-coord'] -= dy


def plot_systems(polar_coordinates, systems, central_system, max_range=10):
    # Extract polar coordinates and names
    thetas, rs = zip(*polar_coordinates)
    names = [system['designation'] for system in systems]
    
    # Convert polar coordinates to Cartesian coordinates
    xs = np.array(rs) * np.cos(thetas)
    ys = np.array(rs) * np.sin(thetas)
    
    # Adjust the coordinates to center the plot around the central system
    central_x = central_system['x-coord']
    central_y = central_system['y-coord']
    xs -= central_x
    ys -= central_y
    
    # Filter systems based on maximum range
    visible_systems = [(x, y, name) for x, y, name in zip(xs, ys, names) if abs(x) <= max_range and abs(y) <= max_range]
    xs, ys, names = zip(*visible_systems)
    
    # Plot the systems
    plt.figure(figsize=(10, 10))
    plt.scatter(xs, ys, color='red')
    
    # Plot central system
    plt.scatter(0, 0, color='blue', label=central_system['designation'])
    
    # Plot names
    for name, x, y in zip(names, xs, ys):
        plt.text(x, y, name, fontsize=8, verticalalignment='bottom', horizontalalignment='right')
    
    # Set limits
    plt.xlim(-max_range, max_range)
    plt.ylim(-max_range, max_range)
    
    # Set aspect ratio to equal
    plt.gca().set_aspect('equal', adjustable='box')
    
    # Set tick marks with steps of one from 0 to 10 and 0 to -10
    plt.xticks(np.arange(-max_range, max_range + 1, 1))
    plt.yticks(np.arange(-max_range, max_range + 1, 1))
    
    # Show plot
    plt.legend()
    plt.grid(True)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Star Systems')
    plt.show()



# Generate 50 star systems
# star_systems = generate_star_systems(1000)

# Select an initial central system
initial_central_system = np.random.choice(systems)

# Convert XY coordinates to polar coordinates relative to the initial central system
polar_coordinates = convert_to_polar_coordinates(systems)


# Plot the star systems with the initial central system
plot_systems(polar_coordinates, systems, initial_central_system, max_range=10)


# Suppose the user selects a new central system
new_central_system = np.random.choice(systems)

# Plotting the radar plot with updated positions
plot_systems(polar_coordinates, systems, new_central_system, max_range=10)

