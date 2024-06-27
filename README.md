# Baseball-Team-Manager-V2

Team Management Program: Version 2
Update the team tracking program used in project #1. The flow and functionality of the program from project #1 will be the same except for the addition of the date function in this project. Remember to use appropriate function names in all modules. 
Make corrections in Project #1 based on any feedback and use a copy of that program for this version. New formatting will be added to change how the output is displayed (as described below), but it will not change what is displayed.
The first project used a list of lists to hold player data. This project will be refactored to use a list of dictionaries where each player is represented by a dictionary with four keys listed here for the player’s ‘name’, ‘position’, ‘at_bats’, and ‘hits’.  Note: the next project will use a list of objects. Here is a short example of a list of player dictionaries. This can be used to update the interface code without the need to call the function that reads from the data file. 
playersList = [
{"name":"Dominick Gilbert", "position":"1B", "at_bats":537, "hits":170},
{"name":"Craig Mitchell", "position":"CF", "at_bats":396, "hits":125}]

The batting average is calculated as needed when it is printed, not stored in the list or dictionary. 
The program will consist of one Python file to hold the main function and supporting functions, and a second Python file (FileIO.py) with two functions which read from and write to a comma delimited csv file. The program will use the file named players.csv to store the data. Remember that each row in a CSV reader object is a list and each ‘element’ in the row can be accessed with a list index. Review chapter 7, “How to read a CSV file”. 
The data is loaded into a list in the main function before the user is asked for a menu option. The lineup list variable will still be used as an argument when calling a support function as was done in Project #1. The code in the functions will need to be changed to use a dictionary that holds the player information instead of a list that holds the player information. 
The new formatting requires that the separator lines are 60 characters long and based on the multiplication operator. The format for the lineup display columns will use 3 spaces for the order number, 31 spaces for the player name, 6 spaces for the position, at bats, and hits, and 8 spaces for the batting average. The batting average must be formatted to always displays 3 decimals. Update the display formatting to match the alignment formatting shown below.
Use a tuple to represent the valid positions a player can have.









Sample Console Output
When the program starts the user has the option to enter a game date. The current date is printed by the program with the YYYY-MM-DD format. This format is used for all date input and output. 
================================================================
                   Baseball Team Manager

CURRENT DATE:    2022-09-12
GAME DATE:    


If no date is entered display the menu options.
================================================================
                   Baseball Team Manager

CURRENT DATE:    2022-09-12
GAME DATE:       

MENU OPTIONS
1 – Display lineup
2 – Add player
3 – Remove player
4 – Move player
5 – Edit player position
6 – Edit player stats
7 - Exit program

POSITIONS
C, 1B, 2B, 3B, SS, LF, CF, RF, P
================================================================
Menu option:  


If a date is entered display the number of days till the game and then the menu option. Do not display the number of games if the date entered is in the past. 

================================================================
                   Baseball Team Manager

CURRENT DATE:    2022-09-12
GAME DATE:       2022-09-13
DAYS UNTIL GAME: 1

MENU OPTIONS
1 – Display lineup
2 – Add player
3 – Remove player
4 – Move player
5 – Edit player position
6 – Edit player stats
7 - Exit program

POSITIONS
C, 1B, 2B, 3B, SS, LF, CF, RF, P
============================================================ 
Menu option:  1
   Player                            POS    AB     H     AVG
------------------------------------------------------------
1  Dominick Gilbert                   1B   545   174   0.319
2  Craig Mitchell                     CF   533   127   0.238
3  Jack Quinn                         RF   535   176   0.329
4  Simon Harris                        C   485   174   0.359
5  Darryl Moss                        3B   532   125   0.235
6  Grady Guzman                       SS   477   122   0.256
7  Wallace Cruz                       LF   475   138   0.291
8  Cedric Cooper                      2B   215    58   0.270
9  Alberto Gomez                       P   103    21   0.204

Menu option:


Notes: 
The function that reads the CSV file can use the csv module and should loop through one row of the file at a time. For each row populate the dictionary for a player based on the 4 columns of data in the file and add that dictionary object to the list of players. The function will return the list of dictionary objects.

The function that writes to the CSV file should not use the csv module writerows method since this method does not work with a dictionary. Treat the CSV file as a text file when opening the CSV file. Using a loop for the players list, call the file write method to write the name, position, at bats, and hits values separated by commas. Make sure to include a new line escape sequence after the hits value.  







Submission details
Projects can require the use of material from any of the previous chapters covered in the textbook.
Create a Team Management Python program that satisfies the specifications above. Think of the specifications as a checklist of requirements. 
Put General Comments at the beginning of the project that includes (1) your name, (2) the project name, (3) the date, and (4) a description of the project. 
Turn in a ZIP file of the final version of the program. Include a Word document which contains output of the testing done on the program. The Word document must be inside the ZIP file.
In the Comments section on the Assignment webpage, report (A) an estimate of the time it took to complete the project. Report a single value in minutes, and (B) a single rating of the project, on an ordinal scale, as either (1) Easy, (2) Moderate, (3) Hard, OR (4) Challenging. 
