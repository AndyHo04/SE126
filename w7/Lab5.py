#Name - Andy Ho

#Date - 2/29/24

#Lab5

#Program Prompt - In this lab, you will build a Python application that allows a user to repeatedly choose an option from a menu to search through the data provided in the text file: lab5.txt(students data)

#Variable Dictionary:
#field 0 - col.0, rec[0]
#id - a list that holds the student id's(field 0)

#field 1 - col.1, rec[1]
#lname - a list that holds the student last names(field 1)

#field 2 - col.2, rec[2]
#fname - a list that holds the student first names(field 2)

#field 3 - col.3, rec[3]
#class1 - a list that holds the student's first class(field 3)

#field 4 - col.4, rec[4]
#class2 - a list that holds the student's second class(field 4)

#field 5 - col.5, rec[5]
#class3 - a list that holds the student's third class(field 5)

#csvfile - the file that holds the data
#file - the csv reader that reads the data from the file
#rec - the data in the file

#menu - a function that displays a menu and gets a validated choice from the user
#answer(min the menu function) - the answer that the user inputs

#found_class - a list that holds the index of the people who have the class when searching for a class roster
#seq_search - a function that builds a sequential search for option 4 to view the class roster
#pick - the class that the user wants to search for from the class_input

#bin_search_id - a function that builds the binary search for option 2 to search for a student ID
#bin_search_lname - a function that builds the binary search for option 3 to search for a student Last Name
#search - the value that the user wants to search for in the binary search functions
#min - the first position of the list to be searched in the binary search functions
#max - the last position of the list to be searched in the binary search functions
#mid - the middle position of the list to be searched in the binary search functions and will eventually be the found value

#answer = loop control variable/what keeps the loop going or not
#user_choice - the choice that the user inputs in the menu function
#class_input - the class that the user wants to search for in option 4




#-----------------PROGRAM BEGINS BELOW----------------------
import csv

#create empty 1d lists
id = []
lname = []
fname = []
class1 = []
class2 = []
class3 = []

#open file
with open("w7/lab5_students.txt") as csvfile:
    
    file = csv.reader(csvfile)
    
    for rec in file:
        id.append(rec[0])
        lname.append(rec[1])
        fname.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])

#-----------------FUNCTIONS----------------------
#The menu function displays a menu and gets a validated choice from the user
def menu():
    print("\n")
    print("\n\tPlease choose from the following options:")
    print("\n\t1.See all Student Report")
    print("\n\t2.Search for a student ID")
    print("\n\t3.Search for a student Last Name")
    print("\n\t4.View a class roster[class1, class2, class3]")
    print("\n\t5.Exit")
    answer = input("\n\tEnter your choice: ")
    return answer

#build a sequential search function for option 4 to view the class roster
def seq_search(pick):
    found_class = []

    for i in range (0, len(id)):
        #ask if search value matches current value in any classes(search)
        if pick.upper() == class1[i].upper() or pick.upper() == class2[i].upper() or pick.upper() == class3[i].upper():
            found_class.append(i)#appends the index of the person who has the class
    if found_class[0] != "":
        print(f"\n\t{"ID":5} {"LastName":11} {"FirstName":8}")
        print("\t-----------------------------------------")
        for i in range(0,len(found_class)):
             print(f"\t{id[found_class[i]]:5} {lname[found_class[i]]:11} {fname[found_class[i]]:8}")
    else:
        print("\tThe class does not exist")

#build the binary search for option 2 to search for a student ID
def bin_search_id():
    search = input("\n\tEnter the student ID you are looking for: ")

    min = 0#first position of the list to be searched
    max = len(id) - 1#last position of the list to be searched
    mid = int((min + max) / 2)#middle position of the list to be searched and will eventually be the found value

    while (min < max and search.lower() != id[mid].lower()):#create the loop for the binary search to begin looking through the list
        if search < id[mid]:#if the search value is less than the middle value
            max = mid - 1#the max value will become the middle value - 1
        else:
            min = mid + 1# the min value will become the middle value + 1
        mid = int((min + max) / 2)
    if search.lower() == id[mid].lower():
        print(f"\n\t{"ID":5} {"LastName":11} {"FirstName":8} {"Class1":6} {"Class2":6} {"Class3":6}")
        print("\t--------------------------------------------------------------------------------")
        print(f"\t{id[mid]:5} {lname[mid]:11} {fname[mid]:8} {class1[mid]:6} {class2[mid]:6} {class3[mid]:6}")
    else:
        print("\tThe student ID does not exist")
#build the binary search for option 3 to search for a student Last Name
def bin_search_lname():
    search = input("\n\tEnter the last name you are looking for: ")

    min = 0#first position of the list to be searched
    max = len(lname) - 1#last position of the list to be searched
    mid = int((min + max) / 2)#middle position of the list to be searched and will eventually be the found value

    while (min < max and search.lower() != lname[mid].lower()):#creates the loop for the binary search to begin looking through the list
        if search < lname[mid]:#if the search value is less than the middle value
            max = mid - 1# the max value will become the middle value - 1
        else:
            min = mid + 1# the min value will become the middle value + 1
        mid = int((min + max) / 2)
    if search.lower() == lname[mid].lower():
        print(f"\n\t{"ID":5} {"LastName":11} {"FirstName":8} {"Class1":6} {"Class2":6} {"Class3":6}")
        print("\t--------------------------------------------------------------------------------")
        print(f"\t{id[mid]:5} {lname[mid]:11} {fname[mid]:8} {class1[mid]:6} {class2[mid]:6} {class3[mid]:6}")
    else:
        print("\tThe student's last name does not exist")
#------------------------------MAIN CODE BELOW------------------------------------------
#initialize the answer variable
answer = "y"

#Create loop for the entire main code/program
while answer == "y":
    user_choice = menu()
    if user_choice == "1":
        print(f"\t{"ID":5} {"LastName":11} {"FirstName":8} {"Class1":6} {"Class2":6} {"Class3":6}")
        print("\t-------------------------------------------------------------------------------------------")
        for i in range (0, len(id)):
            print(f"\t{id[i]:5} {lname[i]:11} {fname[i]:8} {class1[i]:6} {class2[i]:6} {class3[i]:6}")
    elif user_choice == "2":
        bin_search_id()#call the binary search function for student ID
    elif user_choice == "3":
        bin_search_lname()#call the binary search function for student Last Name
    elif user_choice == "4":
        class_input = input("\tEnter the class you are looking for: ").upper()
        seq_search(class_input)
    elif user_choice == "5":
        answer = "n"
        print("\tyou have chosen to exit")
#exit the loop
print("\tThank you for using this program")
