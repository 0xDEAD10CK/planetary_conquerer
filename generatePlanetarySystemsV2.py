import random
import json
import itertools
from descriptors import generate_descriptor, generate_star_system_type, generate_star_system_economy
import os

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
planet_types = ["Rocky", "Gas Giant", "Frozen", "Oceanic", "Desert"]

def generate_planet_name():
    return ''.join(random.choice(alpha) for _ in range(5))

def generate_universe():
    solarSystems, used_planet_names = [], set()
    index = 0

    for chars in itertools.product(alpha, repeat=3):
        solar_system = {
            "index": index,
            "designation": ''.join(chars),
            "classification": generate_star_system_type(),
            "economy": generate_star_system_economy(random.randint(1, 100)),
            "planets": []
        }

        num_planets = random.randint(3, 8)

        for _ in range(num_planets):
            planet_name = generate_planet_name()

            while planet_name in used_planet_names:
                planet_name = generate_planet_name()

            used_planet_names.add(planet_name)

            planet_type = random.choice(planet_types)
            planet_descriptor = generate_descriptor(planet_type)

            planet = {
                "designation": planet_name,
                "type": planet_type,
                "description": planet_descriptor
            }

            solar_system["planets"].append(planet)

        solarSystems.append(solar_system)
        index = index +1

    random.shuffle(solarSystems)
    return solarSystems

universe_path = "universe_files"

if not os.path.exists(universe_path):
    os.mkdir("universe_files")
    open("universe_files/universe.json", 'a').close()

generated_data = generate_universe()
total_planets = sum(len(system["planets"]) for system in generated_data)

print("Total unique Solar Systems:", len(generated_data))
print("Total unique planets:", total_planets)

with open("universe_files/universe.json", "w") as json_file:
    json.dump(generated_data, json_file, indent=2)
