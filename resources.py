import random
import json
from drilling import run_miner
def scan_resources():
    chance = random.randint(1,100)

def generate_resource():
    with open("pilot_files/ship.json", "r") as json_file:
        ship = json.load(json_file)

    collected_ore = run_miner()

    if collected_ore[1] in ship["inventory"]:
        ship["inventory"][collected_ore[1]] += collected_ore[0]
    else:
        ship["inventory"][collected_ore[1]] = collected_ore[0]


    with open("pilot_files/ship.json", "w") as json_file:
        json.dump(ship, json_file, indent=2)


    print(collected_ore)
    print(ship)
