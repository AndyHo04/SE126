#NAME - Andy Ho

#Lab - week 2 in class lab

#date - 1/16/24

#program prompt - The csv file lab2a.csv contains a list of rooms, the maximum number of people that the roomcan accommodate, and the number of people currently registered for the event. Write aprogram that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list. After the file is completely processed the program should display the number of records processed and thenumber of rooms that are over the limit.

#variable dictionary:
#total_records - the amount of records that were in the file
#rooms - a list that holds all the rooms
#maxs - list that holds all the max values
#mins - list that holds the min values
#csvfile - holds lab2a.csv
#file - allows for program to read the lab2a.csv file
#rec - tells the program to process one record at a time
#over - sum of min and max values
#total_rooms - rooms that were over max capacity

#------------main program below-----------
#import the csv
import csv 

#store the total amount of records
total_records = 0

#initialize empty lists
rooms = []
maxs = []
mins = []

#connect to file
with open("w2/hw/lab2a.csv") as csvfile:
    
    #allow the file to be read by the program
    file = csv.reader(csvfile)

    #read/process the file data one at a time
    for rec in file:
        
        #store data to a list and add it to a list
        rooms.append(rec[0]) #rooms
        maxs.append(int(rec[1])) #max capacity for rooms
        mins.append(int(rec[2])) # min capacity for rooms

        #keep literal count of numbers of records
        total_records += 1

#set count for rooms over limit
#print the header
print(f"{'ROOM':20} {'MAX':5} {'MIN':6} OVER")

total_room = 0
for index in range(total_records):
    if mins[index] > maxs[index]:
        #increment the rooms over capacity
        total_room += 1
        #calculate the sum of rooms that have over capacity
        over = mins[index] - maxs[index]
        #print rooms that have 
        # over capacities
        print(f"{rooms[index]:20} {maxs[index]:3} {mins[index]:5} {over:5}")
#display final values
print(f"There were {total_records} records processed")
print(f"there were {total_room} rooms over the limit")
print("Press enter to continue...")



        
    




