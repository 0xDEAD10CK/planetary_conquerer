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

    path = f"pilot_files/{name}"
    os.mkdir(path)
    with open(f"pilot_files/{name}/{name}-pilot.json", "w") as json_file:
        json.dump(pilot, json_file, indent=2)
    with open(f"pilot_files/{name}/{name}-ship.json", "w") as json_file:
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




