from universe import generate
from pilot import create_pilot, view_pilot
from menu import display_main_menu, display_loop_menu
from utils import clear, checkFile, joinPath
from systems import generate_selected_star_systems, view_nearby_systems, move_to_nearby_system
import random as rd


clear()
choice = display_main_menu()  
if choice == "1":
    gameState = True
    clear()
    create_pilot(input("Insert Pilot Name: "))
    if checkFile("universe_files/universe.json") == False:
        generate()
    if checkFile("universe_files/selected_star_systems.json") == False:
        generate_selected_star_systems(rd.randint(1, 46656), "universe_files/universe.json")



while gameState == True:
    clear()
    choice = display_loop_menu()
    
    if choice == "1":
        clear()
        view_pilot()

    if choice == "2":
        clear()
        
        view_nearby_systems("universe_files/selected_star_systems.json")
        choice = input("\nWould you like to move to a new system? Y/N:")
        if choice == "Y":
            move_to_nearby_system(input("Insert Designation: "))