#Name - Andy Ho

#Lab - 4 individial

#Program prompt - In Python, process the text file “lab4A_GOT_NEW.txt” to store each field into their own corresponding lists. Process the lists to print the them as they appear in the file.  Re-process the lists to add the House Motto (dependent on Field4/Allegiance; see motto chart below). Re-Process the lists to print each record fully with the House Mottos

#variable dictionary:
#total_records - how many records were in the file
#field 0 - first names, col.0, rec[0]
#fname - list that holds the first names (col.0, rec[0])
#field 1 -last names, col.1, rec[1]
#lname - list that holds the last names (col.1, rec[1])
#field 2 - ages, col.2, rec[2]
#age - list that holds the ages (col.2, rec[2])
#field 3 - nicknames, col.3 rec[3]
#nickname - list that holds the nicknames (col.3 rec[3])
#field 4 - allegiances, col.4 rec[4]
#allegiances - list that holds the allegiances (col.4 rec[4])
#csvfile - the file used in this lab
#file - allows the program to read the file
#house_stark - count of all people in House Stark
#night_watch - count of all people in Night's Watch
#house_tully - count of all people in House Tully
#house_lannister - count of all people in House Lannister
#house_baratheon - count of all people in House Baratheon
#house_targaryen - count of all people in House Targaryen
#motto - list that holds all the alleigiance's mottos
#all_ages - all the ages of everyone in the file added up
#average_age - the average age of everyone in the file

#---------------main program below------------------------
import csv

total_records = 0
#create 1d lists
fname = []
lname = []
age = []
nickname = []
allegiance = []

print(f"{'FNAME':10} {'LNAME':10} {'AGE':6} {'NICKNAME':18} ALLEGIANCE")
print("------------------------------------------------------------------------")

#connect to file and store the data into 1d list
with open('w4/file/lab4A_GOT_NEW.txt') as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        total_records += 1
        fname.append(rec[0])
        lname.append(rec[1])
        age.append(rec[2])
        nickname.append(rec[3])
        allegiance.append(rec[4])
#process the lists and print the values out
for i in range (0, len(fname)):
    print(f"{fname[i]:10} {lname[i]:10} {age[i]:6} {nickname[i]:18} {allegiance[i]}")

print("\n\n")
print(f"{'FNAME':10} {'LNAME':10} {'AGE':6} {'NICKNAME':18} {'ALLEGIANCE':16} HOUSE MOTTO")
print("-----------------------------------------------------------------------------------------")
#store house allegiances to variables to keep track and list to store the mottos
house_stark = 0
night_watch = 0
house_tully = 0
house_lannister =0
house_baratheon = 0
house_targaryen = 0
motto = []
#process the lists to add the house mottos
for i in range(0, len(fname)):
    if allegiance[i] == "House Stark":
        motto.append("Winter is Coming")
        house_stark += 1
    elif allegiance[i] == "Night's Watch":
        motto.append("And now my watch begins.")
        night_watch += 1
    elif allegiance[i] == "House Tully":
        motto.append("Family. Duty. Honor.")
        house_tully += 1
    elif allegiance[i] == "House Lannister":
        motto.append("Hear me roar!")
        house_lannister += 1
    elif allegiance[i] == "House Baratheon":
        motto.append("Ours is the fury.")
        house_baratheon += 1
    elif allegiance[i] == "House Targaryen":
        motto.append("Fire & Blood")
        house_targaryen += 1
#reprocess list to display motto with other values
for i in range (0, len(fname)):
    print(f"{fname[i]:10} {lname[i]:10} {age[i]:6} {nickname[i]:18} {allegiance[i]:16} {motto[i]}")
    
print("\n\n")
print(f"{'FNAME':10} {'LNAME':10} {'AGE':6} {'NICKNAME':18} {'ALLEGIANCE':16} HOUSE MOTTO")
print("-----------------------------------------------------------------------------------------")
#reprocess the list to add all the ages up
all_ages = 0
average_age = 0
for i in range(0, len(fname)):
    all_ages += (int(age[i]))
#calculate average age
average_age = all_ages / total_records
#display final value and statements
for i in range (0, len(fname)):
    print(f"{fname[i]:10} {lname[i]:10} {age[i]:6} {nickname[i]:18} {allegiance[i]:16} {motto[i]}")
print("-----------------------------------------------------------------------------------------")
print(f"There were {total_records} people in the list")
print(f"The average age of everyone was {average_age:.0f}")
print(f"There were {house_stark} people in House Stark")
print(f"There were {house_baratheon} people in House Baratheon")
print(f"There were {night_watch} people in Night's Watch")
print(f"There were {house_tully} people in House Tully")
print(f"There were {house_lannister} people in House Lannister")
print(f"There were {house_targaryen} people in House Targaryen")

