import random
import json

def scan_resources():
    chance = random.randint(1,100)

def generate_resource():
    with open("universe_files/universe.json", "r") as json_file:
        universe = json.load(json_file)