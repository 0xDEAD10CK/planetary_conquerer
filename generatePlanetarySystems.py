import random
import json
from descriptors import generate_descriptor, generate_star_system_type, generate_star_system_economy
import sys

alpha = ["A","B","C","D","E","F","G","H",
         "I","J","K","L","M","N","O","P",
         "Q","R","S","T","U","V","W","X",
         "Y","Z","1","2","3","4","5","6",
         "7","8","9","0"]

planet_types = ["Rocky", "Gas Giant", "Frozen", "Oceanic", "Desert"]
used_planet_names = set()
solarSystems = []

def generate():
    for char1 in alpha:
        for char2 in alpha:
            for char3 in alpha:
                star_system_type = generate_star_system_type()
                star_system_economy = generate_star_system_economy(random.randint(1,100))
                
                solar_system = {
                    "designation": char1 + char2 + char3,
                    "classification": star_system_type,
                    "economy": star_system_economy,
                    "planets": []
                }

                num_planets = random.randint(3, 8)  # Generate a random number of planets per system

                for i in range(num_planets):
                    planet_name = ""
                    planet_type = random.choice(planet_types)
                    planet_descriptor = generate_descriptor(planet_type)

                    while True:
                        for j in range(5):
                            planet_name = planet_name + random.choice(alpha)

                        if planet_name not in used_planet_names:
                            break

                    used_planet_names.add(planet_name)

                    planet = {
                        "designation": planet_name,
                        "type": planet_type,
                        "description": planet_descriptor
                    }

                    solar_system["planets"].append(planet)

                solarSystems.append(solar_system)

    random.shuffle(solarSystems)
    return solarSystems

def print_star_system_by_name(system_name):
    for solar_system in solarSystems:
        if solar_system["designation"] == system_name:
            print("Solar System Name:", solar_system["designation"])
            print("Star System Type:", solar_system["classification"])
            print("Economy Status:", solar_system["economy"])
            print("Planets:")
            for planet in solar_system["planets"]:
                print("- Planet Name:", planet["designation"])
                print("  Planet Type:", planet["type"])
                print("  Descriptor:", planet["description"])
            print("Star System size in bytes:",str(sys.getsizeof(solar_system))+"b")
            return  # Exit the loop once the star system is found

generated_data = generate()
total_planets = 0

for solar_system in generated_data:
    total_planets += len(solar_system["planets"])

print("Total unique Solar Systems:",len(solarSystems))
print("Total unique planets:", total_planets)


# Convert the generated data to JSON format and save it to a file
with open("universe.json", "w") as json_file:
    json.dump(generated_data, json_file, indent=2)
