#W3D1 Demo - text file handling & storing to 1d lists

import csv

#total counter for all records
total_records = 0

print(f"{'Type':8} {'manu':8} {'processor':3} {'ram':3} {'hdd_1':5} {'num_hdd':3} {'hdd_2':5} {'os':4} {'year':4}")

with open("w3/lab2b.csv") as csvfile:

    file = csv.reader(csvfile)


    for rec in file:
        #print(rec)#show as a LiST[]

        #keep track of the rec count in the file
        total_records += 1
        #total_records = total_records + 1

        #FILTER FOR DISPLAY--------------
        #---comp type -- rec[0]
        if rec[0] == "D":
            comp_type = "Desktop"
        elif rec[0] == "L":
            comp_type = "Laptop"
        else:
            comp_type = "ERROR--" + str(rec[0])
        
        #--manufacturer -- rec[1]
        if rec[1] == "DL":
            manu = "Dell"
        elif rec[1] == "GW":
            manu = "Gateway"
        elif rec[1] == "HP":
            manu = rec[1]
        else:
            manu = "ERROR --" + str(rec[1])

        #--Processor / ram / hdd_1/ num_hdd - exact from file
        processor = rec[2]
        ram = rec[3]
        hdd_1 = rec[4]
        num_hdd = rec[5]

        if rec[5] == "1":
            hdd_2 = "    "#"----" #"none"
            os = rec[6]
            year = rec[7]
        
        elif rec[5] == "2":
            hdd_2 = rec[6]
            os = rec[7]
            year = rec[8]
        else:
            hdd_2 = "ERR0R--" + str(rec[5])
            os = "ERR0R--"
            year = "ERROR --"

        #final print for each record
        #print(f"{comp_type:8} {manu:8} {processor:3} {ram:3} {hdd_1:5} {num_hdd:3} {hdd_2:5} {os:4} {year:4}")
        print(f"{comp_type:8} {manu:8} {processor:3} {ram:3} {hdd_1:5} {num_hdd:3} {hdd_2:5} {os:4} {year:4}")
        
#------DISCONNECED FROM FILE-----------------------

print(f"TOTAL RECORDS: {total_records}")

