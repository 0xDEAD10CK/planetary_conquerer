import time
import random
import math
from colorama import init, Fore, Style

# Function to clear the console (for better animation)
def clear_console():
    print("\033c", end="")

# Function to display the ASCII image
def display_image(image):
    clear_console()
    for row in image:
        print(row)

# Function to add debris around the laser beam
def add_debris(image, debrisX, debrisY):
    for i in range(debrisX, debrisY):
        row = list(image[i])
        for j in range(10, 15):
            if random.random() < 0.3:  # Adjust the probability as desired
                randomColor = random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE])
                debris_char = random.choice(['.', ',', ':', ';', "'", "\""])
                row[j] = f"{randomColor}{debris_char}{Style.RESET_ALL}"
            elif row[j] != " " and random.random() < 0.4:  # Remove spaces to maintain width
                row[j] = " "
        for j in range(22, 27):  # Add debris on the other side
            if random.random() < 0.3:
                debris_char = random.choice(['.', ',', ':', ';', "'", "\""])
                row[j] = debris_char
            elif row[j] != " " and random.random() < 0.4:  # Remove spaces to maintain width
                row[j] = " "
        image[i] = "".join(row)



# Animate the image

def run_miner():
    # Define the initial ASCII image
    drill_image = [
        "         |      |///|      |                           ",
        "         |      |///|      |                           ",
        "         |      |///|      |                           ",
        "         |      |///|      |                           ",
        "         |      |///|      |                           ",
        "         |      /+++\      |                           ",
        "         |     |=====|     |                           ",
        "         |      \===/      |                           ",
        "         \       \=/       /                           ",
        "          \       V       /                            "
    ]

    # Define variables
    finished = False
    x = 0
    y = 0
    debrisZoneX = 6
    debrisZoneY = 10
    ore_name = random.choice(["Helindesite", "Kelorium", "Veqsum", "Lomdesium"])
    while finished == False :  # You can change the number of frames

        drill_image[1] = f"         |      |///|      |   MINING IN PROGRESS  "
        drill_image[1] += f"  Percentage: {x*10:2d}%       "
        drill_image[2] = f"         |      |///|      |   ORE COLLECTED: "
        drill_image[2] += f"{y}"

        display_image(drill_image)
        add_debris(drill_image, debrisZoneX, debrisZoneY)
        time.sleep(0.5)  # Adjust the sleep time for desired speed
        #drill_image.insert(0, " " * 16 + "|///|" + " " * 16)  # Add a new line at the top

        hitChance = random.random()

        if hitChance >= 0.95:
            drill_image.insert(5, " " * 9 +"|"+ " " * 6 + "|///|" + " " * 6 + "|" + " " * 9)
            y += math.ceil(random.random() * 10000)
            debrisZoneX += 1
            debrisZoneY += 1
            x += 1

        if x == 10:
            drill_image[1] = f"         |      |///|      |   MINING IN PROGRESS  "
            drill_image[1] += f"  Percentage: {x*10:2d}%       "
            display_image(drill_image)
            add_debris(drill_image, debrisZoneX, debrisZoneY)
            finished = True
            print("finished")

    return y, ore_name


