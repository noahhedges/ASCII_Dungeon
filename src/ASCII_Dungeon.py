import time
from Save_State_Manager import *

def newGame():
    # ASCII forest landscape

    print("You find yourself waking in an unknown forest...\nYour head is pounding, " \
    "the only thing you can remember is your name. You think it was...\nName: ")

    player_name = input()
    createNewSaveState(player_name)

    print("\nRight! It was " + player_name + "!\nUpon remembering your name, you notice the weathered armour on your back" \
    " and the damaged sword in your sheath.\nYou must have been some kind of warrior.")
    time.sleep(5)
    print("\n\nYou see a castle in the distance its presence beckoning you in its direction.\nYou pick yourself up, and" \
    " begin your journey through...")
    time.sleep(5)
    print("\n\nACT 1: The Forest")
    # Replace "ACT 1: The Forest" with ASCII art



def mainMenu():
    print("Welcome to ASCII Dungeon!\nPlease select your menu option:\n\n1. New Save\n2. Load Save\n3. Delete Save\n4. Exit")
    # Replace "Welcome to ASCII Dungeon" with displaying "ASCII Dungeon" title in ASCII art
    option = input()
    match option:
            case "1": # Creates new save file.
                print("Creating new save...\n")
                newGame()
            case "2": # Display three save profiles, allow user to choose one iff save state exists.
                print("Select Save State to Load:")
                displaySaveStates()
            case "3": # Display three save profiles, allow user to delete one iff save state exists.
                print("Select Save State to Delete:")
                displaySaveStates()
            case "4": # Exits game.
                print("Exiting...")
                return
            case _: # Default case
                print("Invalid input, please retry.\n")
                mainMenu()

mainMenu()