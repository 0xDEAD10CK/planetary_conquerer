import json
import random
import math

original_file_name = "universe_files/universe.json"
nearby_systems_file = "universe_files/selected_star_systems.json"

def generate_selected_star_systems(player_system_index, original_file_name):
    # Load the JSON file containing star systems
    with open(original_file_name, "r") as json_file:
        all_star_systems = json.load(json_file)

    # Get the total number of star systems
    total_star_systems = len(all_star_systems)

    # Define the range of star systems to extract
    selected_star_systems = []
    for i in range(player_system_index - 5, player_system_index + 6):
        selected_star_systems.append(all_star_systems[i % total_star_systems])

    with open(nearby_systems_file, "w") as selected_json_file:
        json.dump(selected_star_systems, selected_json_file, indent=2)

    return nearby_systems_file


################################################################################################################


def view_nearby_systems(nearby_systems_file):
    with open(nearby_systems_file, "r") as json_file:
        nearby_systems = json.load(json_file)
        counter = 0

        for system in nearby_systems:
            X = {
                "designation": system["designation"],
                "classification": system["classification"],
                "economy": system["economy"],
                "planets_count": len(system["planets"])  # Optional: Include the number of planets
            }

            if counter == 5:         
                print(f'\033[1;32mDesignation: {X["designation"]}, Classification: {X["classification"]}, Economy: {X["economy"]}, Planet Count: {X["planets_count"]}\033[0m')
            else:
                print(f'Designation: {X["designation"]}, Classification: {X["classification"]}, Economy: {X["economy"]}, Planet Count: {X["planets_count"]}')
            counter += 1


################################################################################################################


def move_to_nearby_system(destination_designation):
    # Load the nearby star systems
    with open(original_file_name, "r") as json_file:
        universe = json.load(json_file)
    with open(nearby_systems_file, "r") as json_file:
        nearby_systems = json.load(json_file)
    with open("pilot_files/ship.json", "r") as json_file:
        ship = json.load(json_file)

    currentIndex = 0

    #NEED CODE HERE
    for index, x in enumerate(universe):
         if x['designation'] == nearby_systems[5]['designation']:
             currentIndex = index

    # Find the selected system in the list of all star systems
    selected_system = None
    selected_system_index = None
    for index, x in enumerate(nearby_systems):
        if x['designation'] == destination_designation:
            for index, system in enumerate(universe):
                if system['designation'] == destination_designation:
                    selected_system = system
                    selected_system_index = index
                    print(f'\033[1;32m{selected_system_index}\033[0m')
                    break

    if selected_system is None:
        print(f"The system with designation '{destination_designation}' is not nearby.")
        input("Press ENTER to return...")
        return

    print(f"You have selected the system: {selected_system['designation']}")
    fuel_usage = abs(currentIndex - selected_system_index)
    ship["fuelUnits"] -= fuel_usage
    print(f"Fuel Usage: {fuel_usage}")
    print(f"Current Fuel Units: {ship['fuelUnits']}")
    with open("pilot_files/ship.json", "w") as ship_file:
        json.dump(ship, ship_file, indent=2)

    # Regenerate the nearby star systems file with the selected system as the player's system
    generate_selected_star_systems(selected_system_index, original_file_name)
    input()


################################################################################################################

