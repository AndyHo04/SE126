#Name - Andy Ho

#Lab #4 in class

#Program Prompt - Part 1 - Write a program that reads the data file (below) and stores the data into 1D parallel lists (remember, one list for every field).  Once the lists are populated (and the file is "closed"), process the lists to reprint the file data, record by record as they originally appear in the file. Part 2 - Next, reprocess the lists to find each student's current average score along with the class average.  While processing in the for loop, store each student's average into a new list called 'avg' and reprint the records to include this numeric average.  Reprocess the lists one final time to find the letter equivalent of each student's average and store this into a new list called 'let_avg'.  Reprint the lists for a third time, record by record including average score and average letter equivalent.  After this third print of the original file data, print to the console the total number of student's in the class along with the class numeric average.  Part 3 -After your final display using the 1D parallel lists, create one new, empty list, that will become a 2D list.  Then, using a for loop and the 1D parallel lists, store the data to the 2D list you have created. Each index in the 2D list should contain a list of data. This list of data should contain the fname, lname, test1, test2, test3, num_average, and letter_average for the respective student. Process through this 2D list to display the data from the file (it should appear just like your previous 3 prints!)


#variable dictionary:
#total_records - keeps count of all records in file
#field 0 - col.0, rec[0]
#fname - list that holds the first names(col.0, rec[0])
#field 1 - col.1, rec[1]
#lname - list that holds the last names(col.1, rec[2])
#field 2 - col.2, rec[2]
#test1 - list that olds the scores of test 1 (col.2 rec[2])
#field 3 - col. 3 rec[3]
#test 2 - list that holds the scores of test 2 (col.3 rec[3])
#field 4 - col.4 rec[4]
#test 3 - list that holds the scores of test 3(col.4 rec[4])
#csvfile - the file used in this lab
#file - allows the program to read the file
#avg - average grade of the three tests for all students
#num_average = list that holds the average grade of all students
#letter_grade - list that holds the letter grades from the average grades of all students
#all_stuidents - 2d list that holds the 1d parallel lists(first name, last name, test1, test2, test 3, average grade, letter grade)

#--------------------main base program below------------------------
import csv

#create 1d lists [ will be parallel to each other]
#base lists on fields in file

total_records = 0
fname = []
lname = []
test1 = []
test2 = []
test3 = []

print(f"{'FIRST':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'}")
print("---------------------------------------------------------------------------------")
#connect to file&read data into 1D lists
with open("w4/file/listPractice1-1.txt") as csvfile:

    file = csv.reader(csvfile)

    
    #part 1
    for rec in file:

        total_records += 1
        #store data from file fields to their respective lists
        fname.append(rec[0])
        lname.append(rec[1])
        test1.append(int(rec[2]))#cast int  for math
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

for i in range (0, len(fname)): 
    print(f"{fname[i]:12} \t {lname[i]:12} \t {test1[i]} \t {test2[i]} \t {test3[i]}")

#create divider
print("\n\n")

#part2
print(f"{'FIRST':12} \t{'LAST':12} \t {'TEST1':4} \t {'TEST2':4} \t {'TEST3':4}  {'AVERAGE':3}")
print("---------------------------------------------------------------------------------")
#connect to file&read data into 1D lists
#calculate and store each student's Average Test Score
avg = 0
num_average = []

for i in range(0, len(test1)):
    #divide the average
    avg = (test1[i] + test2[i] + test3[i]) /3

    num_average.append((avg))

for i in range (0, len(fname)):
    print(f"{fname[i]:12} \t{lname[i]:12} \t {test1[i]:4} \t {test2[i]:4} \t {test3[i]:4} \t {num_average[i]:3.0f}")

print("\n\n")
#calculate the letter grade
print(f"{'FIRST':12} \t{'LAST':12} \t {'TEST1':4} \t {'TEST2':4} \t {'TEST3':4} \t {'AVERAGE':5} {'GRADE':2}")
print("---------------------------------------------------------------------------------")
letter_grade = []

#assign letter grades to a list
for i in range(0, len(fname)):
    if num_average[i] >= 90:
        letter_grade.append('A')
    elif num_average[i] >= 80:
        letter_grade.append('B')
    elif num_average[i] >= 70:
        letter_grade.append('C')
    elif num_average[i] >= 60:
        letter_grade.append('D')
    else:
        letter_grade.append('F') 
   
    

for i in range (0, len(fname)):
    print(f"{fname[i]:12} \t{lname[i]:12} \t {test1[i]:4} \t {test2[i]:4} \t {test3[i]:4} \t{num_average[i]:5.0f} \t   {letter_grade[i]}")

print("\n\n")
#part 3
print(f"{'FIRST':16}{'LAST':21}{'TEST1':17}{'TEST2':16}{'TEST3':14}{'AVERAGE':11}GRADE")
print("-----------------------------------------------------------------------------------------------------------")
#create 2d lists
all_students = []

for i in range(0, len(fname)):

    #add each student's data to their (index) place in the all_students[] list 
    all_students.append([fname[i], lname[i], test1[i], test2[i], test3[i], round(num_average[i]), letter_grade[i]])

#display the 2d list to the console where each value appears as a value(and not a list item)
for i in range (0, len(all_students)):
    for x in range (0, len(all_students[i])):
         print(f"{all_students[i][x]:8}", end="\t")

    print()
