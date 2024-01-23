#Name - Andy Ho

#Lab #3 in class

#Program Prompt - Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.

#variable dictionary:
#total_records - keeps count of every record in the file
#field 0 - col.0, rec([0])
#comp_type - a list that hold type of computers(rec[0]) from the file
#field 1 - col.1, rec([1])
#manu - a list that holds the brands of the computers(rec[1])from the file
#field 2 - col.2, rec([2])
#processor - a list that holds the cpu's of the computers(rec[2]) from the file
#field 3 - col.3, rec([3])
#ram - a lst that holds the rams of the computers (rec[3])from the file
#field 4 - col.4 rec([4])
#hdd_1 - the list that holds sizes of the first hard disk that each computer(rec[4]) has from the file
#field 5 - col.5 rec([5]), determines where the remaining records are stored
#num_hdd - the list that number of hard disks that each computer(rec[5]) from the file has
#field 6 -col.6 rec([6])
#hdd_2 - a list that the sizes of the second hard disk if a computer has one(rec[6]) from the file
#field 7 - col.7 rec([7])
#os - A list the operating systems of the computers(rec[7]) from the file
#field 8 - col.8 rec([8])
#year- a list that holds the years each computer was purchased(rec[8]) from the file
#rec - each record in the file
#csvfile - holds the file for the program to read
#desktop_count - counts the amount of desktops
#desktop_money - how much it would cost to replace the desktops
#laptop_count - counts the amount of laptops
#laptop_money - how much it would cost to replace the laptops

#----------main code below---------------

#create a header
print(f"{'type':8} {'Brand':8} {'CPU':3} {'RAM':3} {'1st Disk':8} {'No.HDD':2} {'2nd disk':10} {'OS':2} YEAR")
print("----------------------------------------------------------------------------------------------------------")

import csv

#keep count of total records
total_records = 0

#create empty list names
comp_type = []
manu = []
processor = []
ram = []
hdd_1 = []
num_hdd = []
hdd_2 = []
os = []
year = []

#use the lab2b.csv file
with open("w2/hw/lab2b.csv") as csvfile:

    #let the program read the file
    file = csv.reader(csvfile)

    #let each record in the file be processed
    for rec in file:
        #keep total of records:
        total_records += 1

        #variables for each field - store each type of informationn to a variable using the index
        #filter comp types
        if rec[0] == "D":
            comp_type.append("Desktop")
        elif rec[0] == "L":
            comp_type.append("Laptop")
        else:
            comp_type.append("ERROR--" + str(rec[0]))
        
        #comp_type.append(rec[0])0 - THIS IS A NO
       
       #filter manufacturers
        if rec[1] == "DL":
            manu.append("Dell")
        elif rec[1] == "GW":
            manu.append("Gateway")
        elif rec[1] == "HP":
            manu.append("HP")
        else:
            manu = "ERROR --" + str(rec[1])

        #manu.append(rec[1]) - THIS IS A NO
         
        processor.append(rec[2])
        ram.append(rec[3])
        hdd_1.append(rec[4])
        num_hdd.append(rec[5])
        
        #if the computer has a second hard disk
        if len(rec) == 9:
            hdd_2.append(rec[6])
            os.append(rec[7])
            year.append(rec[8])
        #if the computer does not have a second hard disk
        else:
            hdd_2.append("   ")
            os.append(rec[6])
            year.append(rec[7])

        
        

#Display the information to the user
for index in range(total_records):
    print(f"{comp_type[index]:8} {manu[index]:7}  {processor[index]:3} {ram[index]:3} {hdd_1[index]:10} {num_hdd[index]:6} {hdd_2[index]:8} {os[index]:4} {year[index]:3}")
#keep the total count of desktops/laptops and money cost
desktop_count = 0
laptop_count = 0
desktop_money = 0 
laptop_money = 0
#use the for loop to process the desktops
for index in range(0, len(comp_type)):
    #let the program look through the comp type list
    if comp_type[index] == "Desktop" and int(year[index]) <= 16:
        desktop_count += 1 #add 1 every time a desktop that is processed is outdated and needs to be replaced
        desktop_money += 2000 #add $2000 every time a desktop is processed and going to be replaced
    if comp_type[index] == "Laptop" and int(year[index]) <= 16:
        laptop_count += 1 #add 1 every time a laptop that is processed is outdated and needs to be replaced
        laptop_money += 1500 #add $1500 every time a desktop is processed and going to be replaced

#final message to the users
print(f"\t\tThere were {total_records} computers in the file")
print(f"\t\tTo replace {desktop_count} it will cost ${desktop_money}")
print(f"\t\tTo replace {laptop_count} it will cost ${laptop_money}")
print(f"Press enter to key to continue...")
