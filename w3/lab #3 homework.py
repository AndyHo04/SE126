#Name - Andy Ho

#lab #3 Homework

#Program Prompt - Rewrite the Voter Registration Lab utilizing the data from the file voters.csv.  Store the field data into respective 1D lists, and then process the lists to determine the 4 final output values (make sure they are clearly labeled!). This final solution should have NO input() statements and when the console is ran it should print all 4 totals (you may reprint the data from the lists/fie if you would like)  Use your original Voter Registration Lab (or the solution file!) as starter code, but edit it to connect to a file and store data into lists, then use a for loop to process each voter and their data to find the 4 totals.

#Variable Dictionary:
#total_records - keeps track and counts all records in file and stores it
#individuals_not_of_age - keeps track and counts all individuals who are not eligible to store it
#individuals_eligible_unregistered - keeps track and counts all individuals who are eligible but have not registered to store it
#individuals_eligible_unvoted - keeps track and counts all individuals who are eligible but have not voted to store it
#individuals_voted - keeps track and counts all individuals who have voted to store it
#field 0 - col.0 (rec[0])
#id - a list that holds the ids of people, (rec[0])
#field 1 - col.1 (rec[1])
#age - a list that holds the age of people, (rec[1])
#field 2 - col.2 (rec[2])
#registered - a list that holds the answer to if people are registered or not, (rec[2])
#field 3 - col.3 (rec[3])
#votes - a list that holds the answer to if people voted or not (rec[3])
#csvfile - holds the voter registration data file
#file - holds csvfile for the program to read
#rec - every record in the file





#-------------------------Main code below--------------------------------

import csv

#keep count of total records and voter registraion information
total_records = 0
individuals_not_of_age = 0
individuals_eligible_unregistered = 0
individuals_eligible_unvoted = 0
individuals_voted = 0

#create empty lists to store data from file
id =[]
age = []
registered = []
votes = []

#allow program to access the file with data
with open("w3/voters_202040.csv") as csvfile:

    #allow file to be read by program
    file = csv.reader(csvfile)

    for rec in file:#for every record in the file

        #print rec to show the data
        print(rec)
        #add 1 to total records
        total_records += 1

        #store data to the lists
        id.append(int(rec[0]))
        age.append(int(rec[1]))
        registered.append(rec[2])
        votes.append(rec[3])

#create for loop statement for program to filter the data into the variables
for i in range(total_records):
    #if individuals are not eligible
    if age[i] <= 18:
        individuals_not_of_age += 1
    #if individuals are eligible but have not registered
    elif age[i] >= 18 and registered [i]== "N":
        individuals_eligible_unregistered += 1
    #if individuals have registered but have not voted
    elif registered[i] == "Y" and votes[i]== "N":
        individuals_eligible_unvoted += 1
    #if individuals have voted
    elif registered[i] == "Y" and votes[i] == "Y":
        individuals_voted += 1
#end of for loop
#display final output and messages to user
print(f"The total amount of records processed was {total_records}")
print(f"Number of individuals not eligible: {individuals_not_of_age}")
print(f"Number of individuals who are enough to vote but have not registered: {individuals_eligible_unregistered} ")
print(f"Number of individuals who are eligible but did not vote: {individuals_eligible_unvoted}")
print(f"Number of individuals who voted: {individuals_voted}")

        










