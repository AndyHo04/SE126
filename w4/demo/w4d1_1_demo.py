import csv

#create 1d lists [ will be parallel to each other]
#base lists on fields in file

fname = []
lname = []
test1 = []
test2 = []
test3 = []

#connect to fle&read data into 1D lists
with open("w4/file/listPractice1-1.txt") as csvfile:

    file = csv.reader(csvfile)

    #come back and show print (file) later
    

    for rec in file:
        #store data from file fields to their respective lists
        #by PARALLEL - storing initial file record data at same positiion (index) in each list --> use the same [INDEX] across each list to find "matching" data
        fname.append(rec[0])
        lname.append(rec[1])
        test1.append(int(rec[2]))#cast int int for math
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#disconnected from file --------------------------------

#process the lists --> for loop
print(f"{'FIRST':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'}")
print("---------------------------------------------------------------------------------")
for i in range (0, len(fname)): #len() returns Length of (item) -> for lists, it is the # of items in the list

    print(f"{fname[i]:12} \t {lname[i]:12} \t {test1[i]} \t {test2[i]} \t {test3[i]}")
print("---------------------------------------------------------------------------------")


#calculate and store each student's Average Test Score
avg = 0
total_count = 0
average = []

for i in range(0, len(test1)):
    #calculate avg for student
    avg = (test1[i] + test2[i] + test3[i]) /3

    #append this to the average[]
    average.append(avg)

#display student's fname and test average
print(f"{'FIRST'}\t{'AVERAGE'}")
for i in range (0, len(fname)):
    print(f"{fname[i]:12} \t {average[i]:8.1f}")


#SEQUENTIAL SEARCH - "in sequence" --> from beginning THROUGH the end(we learn in week 6)
low_name = ""
low_avg = 100 #sarts with highest value to drop to find lowest

for i in range(0, len(average)):

    #determine if current average is lower than current low_avg
    if average[i] < low_avg:

        low_avg = average[i]#current average is lower, so becomes new low value
        low_name = fname[i]



#DISPLAY: total students in file
print(f"STUDENTS IN FILE: {len(fname)}")
print(f"LOWEST AVERAGE: {low_name} - {low_avg:.1f}")

#--------------2d lists---------------------------
print(f"\n\n---2D LIST DISPLAY-------------------------------------")
print(f"{'FIRST':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'}")
print('---------------------------------------------------------------------------------')
#use your 1d parallel lists to populate a new, 2d list
#Hint:the 2d list is a list ... populated with 8d lists
all_students = []

for i in range(0, len(fname)):

    #add each student's data to their (index) place in the all_students[] list 
    all_students.append([fname[i], lname[i], test1[i], test2[i], test3[i], average[i]])

#display the 2d list to the console - for now, just get the lists to display ie ['Floyd','Eastham','100','85' '93']
print(f"\n\n---2D LIST individial vales-------------------------------------")
for i in range (0, len(all_students)):
    print(f"{all_students[i]}")

#display the 2d list to the console where each vlaue eppears as a value(and not a list item)
    #we have lists within a list - outter for handles main list(all_students)
    for x in range(0, len(all_students[i])):
        #inner for handles each value found at current list(all_students[i])
        print(f"{all_students[i][x]}", end="\t")

    print()

    #include an extra exmpy print() to cancel the interiror prints end=""