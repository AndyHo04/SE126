#Name - Andy Ho

#Lab - MIDTERM

#Program Prompt - For your Midterm Project in SE126 you will be building a program of your own design! You must work individually to design a program and file of your choosing.

#About Program - A 2023-2024 Premier League(England Soccer League) stat sheet program that allows users to see how teams are doing from their current standing, how many goals they have scored, how many points they have, and etc. 

#Variable Dictionary:



#-----------------------PROGRAM BEGINS BELOW-----------------------------------

import csv

#Empty LISTS for data from file to be stored
team = []
standing = []
points = []
wins = []
draws = []
losses = []
goals_scored = []
goals_allowed = []
goals_difference = []
motto = []
nickname = []

#connect to file for program to read and append(store) the data to lists
with open("week5_listReview/MidtermProject/Premier_League_Stats.csv") as csvfile:
   
    file = csv.reader(csvfile)

    for rec in file:
        team.append(rec[0])
        standing.append(int(rec[1]))
        points.append(int(rec[2]))
        wins.append(int(rec[3]))
        draws.append(int(rec[4]))
        losses.append(int(rec[5]))
        goals_scored.append(int(rec[6]))
        goals_allowed.append(int(rec[7]))
        goals_difference.append(int(rec[8]))
    
#add/append team mottos
for i in range(0, len(team)):
    if team[i] == "Liverpool":
        motto.append("You'll Never Walk Alone")
    elif team[i] == "Mancity":
        motto.append('Pride In Battle')
    elif team[i] == "Arsenal":
        motto.append('Victory Through Harmony')
    elif team[i] == "Astonvilla":
        motto.append('Prepared')
    elif team[i] == "Tottenham":
        motto.append('To Dare Is To Do')
    elif team[i] == "Manutd":
        motto.append("Wisdom and Effort")
    elif team [i] == "Westham":
        motto.append("I'm Forever Blowing Bubbles")
    elif team [i] == "Brighton":
        motto.append('We Never Give Up')
    elif team [i] == "Newcastle":
        motto.append('Triumphing by Brave Defense')
    elif team [i] == "Wolverhampton":
        motto.append('Out of Darkness Cometh Light')
    elif team[i] == "Chelsea":
        motto.append('Unless God Is With Us, All Will Be In Vain')
    elif team [i] == "Bournemouth":
        motto.append('Together, Anything Is Possible')
    elif team [i] == "Fulham":
        motto.append('Building Better Lives Through Sport')
    elif team [i] == "Crystalpalace":
        motto.append("Passion and Determination")
    elif team [i] == "Brentford":
        motto.append('Nothing Is Impossible')
    elif team[i] == "Nottmforest":
        motto.append('Virtue Outlives Death')
    elif team [i] == "Lutontown":
        motto.append('May It Be Given to Skill and Industry')
    elif team[i] == "Everton":
        motto.append('Nothing But The Best Is Good Enough')
    elif team [i] == "Burnley":
        motto.append('The Prize and The Cause of Our Labour')
    elif team [i] == "Sheffield":
        motto.append('Out Run Out Fight Out Play')

#add/append nicknames
for i in range(0, len(team)):
    if team[i] == "Liverpool":
        nickname.append('The Reds')
    elif team[i] == "Mancity":
        nickname.append('The Sky Blues')
    elif team[i] == "Arsenal":
        nickname.append('The Gunners')
    elif team[i] == "Astonvilla":
        nickname.append('Lions')
    elif team[i] == "Tottenham":
        nickname.append('Spurs')
    elif team[i] == "Manutd":
        nickname.append("The Red Devils")
    elif team [i] == "Westham":
        nickname.append("The Hammers")
    elif team [i] == "Brighton":
        nickname.append('Seagulls/Albions')
    elif team [i] == "Newcastle":
        nickname.append('The Magpies')
    elif team [i] == "Wolverhampton":
        nickname.append('Wolves')
    elif team[i] == "Chelsea":
        nickname.append('The Blues')
    elif team [i] == "Bournemouth":
        nickname.append('The Cherries')
    elif team [i] == "Fulham":
        nickname.append('The Cottagers')
    elif team [i] == "Crystalpalace":
        nickname.append("Eagles")
    elif team [i] == "Brentford":
        nickname.append('The Bees')
    elif team[i] == "Nottmforest":
        nickname.append('Tricky Trees')
    elif team [i] == "Lutontown":
        nickname.append('The Hatters')
    elif team[i] == "Everton":
        nickname.append('The Toffees')
    elif team [i] == "Burnley":
        nickname.append('The Clarets')
    elif team [i] == "Sheffield":
        nickname.append('The Blades')
#-------------------------FUNCTIONS------------------------------
#a menu to list the teams for the 2023-2024 Premier League
def menu():
    print("\t\t\t\t\tLiverpool\n\t\t\t\t\tMancity\n\t\t\t\t\tArsenal\n\t\t\t\t\tAstonvilla\n\t\t\t\t\tTottenham\n\t\t\t\t\tManutd\n\t\t\t\t\tWestham\n\t\t\t\t\tBrighton\n\t\t\t\t\tNewcastle\n\t\t\t\t\tWolverhampton\n\t\t\t\t\tChelsea\n\t\t\t\t\tBournemouth\n\t\t\t\t\tFulham\n\t\t\t\t\tCrystalpalace\n\t\t\t\t\tBrentford\n\t\t\t\t\tNottmforest\n\t\t\t\t\tLutontown\n\t\t\t\t\tEverton\n\t\t\t\t\tBurnley\n\t\t\t\t\tSheffield")

#create the sequential search function which will search through the entire list to find the value you are looking for
def seq_search(pick):

    #initilaize the index variabl
    choice_index = ""#this is empty

    #create a for loop so that the program looks through the list from start to end to find the value you are looking for
    for i in range(0, len(team)):

        #look at each value in the list to see if it matches what you are looking for from your input
        if team[i] == pick:
            choice_index = i #stores the index(location) to this variable
        
    return choice_index #returns your choice

#----------------------MAIN CODE BELOW--------------------------------

total_searchs = 0
answer = "y"


#create while loop to introduce the user to the program and keep them in as long as they want
while answer.lower() == "y":
    #HEADING
    print("\n\n\t\t\t2023-2024 Premier League Stats for Each Team")
    print("---------------------------------------------------------------------------------------------------")
    display = menu()
    

    choice = input("\t\t\t\tEnter the team you want to look at:")

    decision = seq_search(choice)

    if decision != "":#if you have a chosen a team that is in the Premier League
        total_searchs += 1
        print(f"\n\n\n\t\t\t{team[decision]}({nickname[decision]})")
        print(f"\t\t\tMOTTO:{motto[decision]}")
        print(f"\t\t\t-------------------------------")
        print(f"\t\t\tStanding:{standing[decision]}\n\t\t\tPoints:{points[decision]}\n\t\t\tWins:{wins[decision]}\n\t\t\tDraws:{draws[decision]}\n\t\t\tLosses:{losses[decision]}\n\t\t\tGoals Scored:{goals_scored[decision]}\n\t\t\tGoals Allowed:{goals_allowed[decision]}\n\t\t\tGoal Difference:{goals_difference[decision]}")
    else: #if you have chosen a team that is not in the Premier League
        print(f"\t\t\tThe team {choice} is not in the Premier League this season")

    #give user opportunity to stop looking at teams and break out of loop
    answer = input("\t\t\tDo you want to continue looking at teams [y/n]:")
#exit loop
print(f"\t\t\tThank you for using this program, You looked at {total_searchs} teams during your session.")





    







