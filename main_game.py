from universe import generate
from player import create_pilot, view_player
from menu import display_main_menu, display_loop_menu, display_ship_menu
from utils import clear, checkFile, joinPath
from systems import generate_selected_star_systems, view_nearby_systems, move_to_nearby_system
from resources import generate_resource
#from save_load import save, load
import random as rd


playerName = ""

clear()
choice = display_main_menu()  
if choice == "1":
    gameState = True
    clear()
    playerName = create_pilot(input("Insert Pilot Name: "))
    if checkFile("universe_files/universe.json") == False:
        generate()
    if checkFile("universe_files/selected_star_systems.json") == False:
        generate_selected_star_systems(rd.randint(1, 46656), "universe_files/universe.json")

elif choice == "2":
    playerName = input("Insert Player Name to Load: ")
    gameState = True

while gameState == True:
    clear()
    choice = display_loop_menu()
    
    if choice == "1":
        clear()
        view_player(playerName)

    if choice == "2":
        clear()
        choice = display_ship_menu()

        if choice == "2":
            generate_resource(playerName)

    if choice == "3":
        clear()
        
        view_nearby_systems("universe_files/selected_star_systems.json")
        choice = input("\nWould you like to move to a new system? Y/N:")
        if choice == "Y":
            move_to_nearby_system(input("Insert Designation: "))