import json
from utils import clear


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
        "inventory": []
        }
    pilot = {
        "name": name,
        "occ": occ,
        "credits": 50000,
        }

    with open("pilot_files/pilot.json", "w") as json_file:
        json.dump(pilot, json_file, indent=2)
    with open("pilot_files/ship.json", "w") as json_file:
        json.dump(ship, json_file, indent=2)


def view_player():
    with open("pilot_files/pilot.json", "r") as json_file:
        pilot = json.load(json_file)
    with open("pilot_files/ship.json", "r") as json_file:
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
    
    input("Press ENTER to return")




