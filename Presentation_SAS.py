# Sebastian Sloan
# Project 2 
# October 29, 2023 
# update project one with new features learned over the past 3 weeks.


# Use functions to organize the code making it reusable, easy to read, and easy to maintain. 
# Each of the functions for the six main menu features should take the list of players as an input parameter. 

import FileIO as IO
from datetime import date
import datetime

def display_menu():
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")
    print()
    print("POSITIONS: ")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")
    print('+' * 50) 
    print()

def add_lineup_number(player_list):

    counter = 0

    for player in player_list:

        counter += 1
        line_num = {"line_num": counter}

        player.update(line_num)
    
    return player_list

def remove_lineup_number(player_list):

    for player in player_list:
        # print(player)
        del player["line_num"]

def display_lineup(player_list):
    
    print("   Player		POS	AB	H	AVG")
    print('-' * 80)

    add_lineup_number(player_list)

        # The formula for calculating batting average is:
        # average = hits / at_bats
        # The program should round batting average to a maximum of three decimal places.
        # print(player)
    for player in player_list:
        if player["hits"] != 0:
            average = round(float(player["at_bats"])/float(player["hits"]),3)
        else:
            average = 0
        # print(number_of_players)
        # print(player)
        print(str(player["line_num"]) + '  ' + player["name"] + '\t' + player["position"] + '\t' + player["at_bats"] + '\t' + player["hits"] + '\t' + str(average))
    remove_lineup_number(player_list)
    IO.writeCSV(player_list)
    print()

def add_player(player_list):
    new_player = {}
    # Use a tuple to store all valid positions (‘C’, ‘1B’, ‘2B’, etc).

    name = input("Name: ")
    new_player["name"] = name
    try:
        positions = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')
        # When entering/editing positions, the program should always require the user to enter a valid position. 
        position = input("Position: ")

        while position not in positions:
            # print(f"'{position}' is not a valid position, please check the list again and re-enter a valid position.\n")
            print(positions)
            position = input("Position: ")
        else:
            new_player["position"] = position

    except ValueError as ve:
        print(type(ve), ve)
        print("Please only enter one of the positions shown above, thank you.")
    
    # Use data validation to make sure the user can’t enter data that doesn’t make sense 
    # (such as a negative number of hits or the player having more hits than at bats).
    try:
        at_bats = input("At Bats: ")

        while at_bats.isdigit() == False:
            print("You must enter a positive number, please try again")
            at_bats = input("At Bats: ")
        else:
            # Make sure that no error occurs if the user enters zero for the number of at bats. 
            # This occurs before the first game of the season when all players have zero at bats. 
            if float(at_bats) >= 0:
                # print(f"{at_bats} has been added")
                new_player["at_bats"] = at_bats
            else:
                print("You must enter a positive number, please try again")
                at_bats = input("At Bats: ")
    
    except ValueError as ve:
        print(type(ve), ve)
        print("The value you entered is incorrect, please enter only a numeric value.")
   
    try:
        hits = input("Hits: ")

        while hits.isdigit() == False:
            print("You must enter a positive number, please try again")
            hits = input("Hits: ")
        else:
            if float(hits) > float(at_bats):
                print("This number is not valid, your 'At Bats' score must be higher.")
                hits = input("Hits: ")
            elif float(hits) > 0:
                # print(f"{hits} has been added")
                new_player["hits"] = hits
            else:
                print("You must enter a positive number, please try again")
                hits = input("Hits: ")
    
    except ValueError as ve:
        print(type(ve), ve)
        print("The value you entered is incorrect, please enter only a numeric value.")

    player_list.append(new_player)
    IO.writeCSV(player_list)
    print(name + " was added.\n")
    print() 

def remove_player(player_list):

    add_lineup_number(player_list)

    player_to_remove = input("Enter a lineup number to remove: ")

    for player in player_list:
        if str(player["line_num"]) == player_to_remove:
            player_list.remove(player)
            print(f"'{player['name']}' has been deleted.")
            # print(player_list)
            print()

    remove_lineup_number(player_list)
    IO.writeCSV(player_list)

def move_player(player_list):

    try:
        
        add_lineup_number(player_list)

        current_player = input("Enter a current lineup number to move: ")
        # print(player_list)

        for player in player_list:
            if str(player["line_num"]) == current_player:
                print(f"player '{player['name']}' has been selected.")
                new_position = input("Enter a new lineup number: ")
                # print(player)
                # print(player_list)
                player_list.insert(int(current_player),player_list.pop(player_list.index(player)))
                print(f"'{player['name']}' has been moved.")
                print()
                break
                # print(player)
                # print(player_list)
        
        remove_lineup_number(player_list)
 
        IO.writeCSV(player_list)


    except ValueError as ve:
        print(type(ve), ve)
        print("The value you entered is incorrect, please enter only a numeric value.")

def edit_player_position(player_list):

    add_lineup_number(player_list)

    line_up_number = input("Enter a lineup number to edit: ")

    positions = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')

    for player in player_list:
        # print(player)
        if str(player["line_num"]) == line_up_number:
            print(f"You selected {player['name']}: Position = {player['position']}")
            new_position = input("Enter a new Position: ")
            if new_position in positions:
                player["position"] = new_position
                print(f"{player['name']} was updated.")
                print()
                remove_lineup_number(player_list)
                IO.writeCSV(player_list)
                break
            else:
                print(f"'{new_position}' is not a valid position.")
                print("please select option '5' again and enter one of these positions")
                print(positions)
                print()
                
def edit_player_stats(player_list):

    add_lineup_number(player_list)

    line_up_number = input("Enter a lineup number to edit: ")

    for player in player_list:
        if str(player["line_num"]) == line_up_number:
            print(f"You selected {player['name']}")
            print(f"At Bat = {player['at_bats']}")
            print(f"Hits = {player['hits']}") 
            print()
            which_stat = input("please type '1' to edit At Bat and '2' to edit Hits: ")
            if which_stat == '1':
                new_at_bat = input("Please enter a new 'At Bat' stat: ")
                if int(new_at_bat):
                    player["at_bats"] = new_at_bat
                    remove_lineup_number(player_list)
                    IO.writeCSV(player_list)
                    print(f"player {player['name']} has had their 'At Bat' Status updated.")
                    print("Please run option '6' again to edit another stat.")
                    print()
                    break
                else:
                    print(f"{which_stat} is not a valid option, please exit and run option '6' again.")
            elif which_stat == '2':
                new_hits = input("Please enter a new 'Hit' stat: ")
                if new_hits < player["hits"]:
                    if int(new_hits):
                        player["hits"] = new_hits
                        remove_lineup_number(player_list)
                        IO.writeCSV(player_list)
                        print(f"player {player['name']} has had their 'Hits' status updated.")
                        print("Please run option '6' again to edit another stat.")
                        print()
                        break
                    else:
                        print(f"{which_stat} is not a valid option, please exit and run option '6' again.")
                else:
                    print("The 'Hits' Status cannot be larger than the 'At Bat' Status, please update the 'At Bat' Status first.")
                    print("Please exit and re-run option 6.")
            else:
                print(f"{which_stat} is not a valid option, please exit and run option '5' again.")


def main():
    print('-' * 50) 
    header = "Baseball Team Manager"
    print(header.center(50))
    print()

    date_format = '%Y-%m-%d'

    print(f"CURRENT DATE:    {date.today()}")

    game_date = input("GAME DATE:    ")

    try:

        game_day = datetime.datetime.strptime(game_date, date_format)
        today = datetime.datetime.strptime(str(date.today()), date_format)

        time_to_next_game = game_day - today
        print(f"DAYS UNTIL GAME: {time_to_next_game.days}")

    except ValueError:

        print("Incorrect data format, should be YYYY-MM-DD")

    # The list will be stored in the main method.

    # Use a list of lists to store each player in the lineup. The list for a single player includes their name, position, 
    # at bats, and hits. This is the ‘inner’ list.
    # aPlayerListVariable = ['Trevor', 'SS', '588', '173'],

    # For part 1 this list will be declared with a statement in the main method.
    # The list of player lists is the ‘outer’ list. 
    # aLineupListVariable = [['Trevor','SS','588','173'], 
                                             # ['Garrett','2B','299','74']]
    
    display_menu()

    players = IO.readCSV()

    while True:
        command = input("Menu option: ")
        if command == "1":
        # For part 2 replace the statement in the main method that declares the lineup list with a statement that calls the read method
        # in the FileIO module. Call the write method of the FileIO module in any function that modifies the lineup list. Note: the line 
        # of code that declares a lineup list can be commented out for future debugging use.
            display_lineup(players)
        elif command == "2":
            add_player(players)
        elif command == "3":
            remove_player(players)
        elif command == "4":
            move_player(players)
        elif command == "5":
            edit_player_position(players)
        elif command == "6":
            edit_player_stats(players)
        elif command == "7":
            print("Bye!")
            break
        else:
            # If the user enters an invalid menu option, display an error message, and display the menu again so 
            # the user can clearly see the valid menu options. Don’t display the menu after every input. Use a function to display the menu.
            print("The command you inputted is not a valid command please try again.")
            display_menu()
            print()
            command = input("Menu option: ")


if __name__ == "__main__":
    main()
