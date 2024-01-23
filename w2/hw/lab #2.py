#Name - Andy Ho

#Lab #2

#Program Prompt - You have been asked to produce a report that lists all the computers in the csv file lab2b.csv. Your report should look like the following sample output. The last line should print the number of computers in the file.

#variable dictionary:
#total_records - keeps count of every record in the file
#comp_type - the type of computers from the file
#manu - the brands of the computers from the file
#processor - the cpu's of the computers from the file
#ram - the rams of the computers from the file
#hdd_1 - the sizes of the first hard disk that each computer has from the file
#num_hdd - the number of hard disks that each computer from the file has
#hdd_2 - the sizes of the second hard disk if a computer has one from the fike
#os - the operating systems of the computers from the file
#year- the year each computer was purchased from the file
#rec - each record in the file
#csvfile - holds the file for the program to read

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
#final message to the user(how many computers there were in total)
print(f"\t\tThere were {total_records} computers in the file")