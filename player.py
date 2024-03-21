import json
from utils import clear
import os


def create_pilot(name):
    occList = ["Fighter", "Trader", "Diplomat", "Scientist"]
    occ = ""

    while occ not in occList:
        clear()
        print(f"Select an occupation for {name} from", occList)
        occ = input("Occupation: ")
    
    
    # Create directory if it doesn't exist
    pilot_directory = "./pilot_files/"
    if not os.path.exists(pilot_directory):
        os.makedirs(pilot_directory)

    # Create subdirectory for the pilot
    pilot_directory = f"./pilot_files/{name}"
    os.makedirs(pilot_directory)
    

    ship = {
        "name": "The Fresh Glizzy",
        "class": "Peasant",
        "fuelUnits": 50,
        "modules": ["Scanner"],
        "inventory": {}
        }
    pilot = {
        "name": name,
        "occ": occ,
        "level": 1,
        "credits": 50000,
        }

    with open(f"pilot_files/{name}/pilot.json", "w") as json_file:
        json.dump(pilot, json_file, indent=2)
    with open(f"pilot_files/{name}/ship.json", "w") as json_file:
        json.dump(ship, json_file, indent=2)

    return name


def view_player(name):
    saveLocation = f"pilot_files/{name}/{name}"
    with open(f"{saveLocation}-pilot.json", "r") as json_file:
        pilot = json.load(json_file)
    with open(f"{saveLocation}-ship.json", "r") as json_file:
        ship = json.load(json_file)

        print("Pilot:")
        print("Name:", pilot["name"])
        print("Occupation:", pilot["occ"])
        print("Credits:", pilot["credits"])
        print("\nShip:")
        print("Name:", ship["name"])
        print("Class:", ship["class"])
        print("Fuel:", ship["fuelUnits"], "units")
        print("Modules:", ship["modules"])
        print("Inventory:", ship["inventory"])
    
    input("Press ENTER to return")




