#Name - Andy Ho

#Lab 1

#Date - 1/9/24

# Program Prompt: You will be writing one Python file for this project - it is a program that determines  whether a meeting room is in violation of fire regulations regarding the maximum room capacity. Theprogram will accept the maximum room capacity and the number of people attending the meeting. If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal to hold the meeting and tells how many additional people may legally attend. If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how any people must be excluded in order to meet the fire regulations. The user should be allowed to enter and check as many rooms as they would like without exiting the program.

#variable dictionary:
#difference - function that calculates the sum of people attending the meeting and the max capacaity of the room
#people(parameter in the difference function) - how many people are attending the meeting
#max_cap(parameter in the difference function) - the max capacity of the room 
#over_under (in the difference function) - the sum of the people attending the room and the max capacity of the room
#decision - function that determines whether the user's choice for continuing the program is valid. 
#response - (parameter in the decision function) - the users response to continuing the program
#answer(in the decision function) - users response to the continuing the program after choosing a invalid option
#answer(in main program) - loop control variable and users choice to continuing the program
#meeting_name - the name of the meeting
#room_capacity - the max capacity of the room
#people_attending - how many people are in the meeting
#dif - what the return value of the difference function is attached to



#----------------Functions---------------
#Create the difference function
def difference(people, max_cap):
    over_under = max_cap - people
    return over_under

#create the decision function
def decision(response):
    if response == "y" or response == "n":
        return response
    elif response != "y" or response != "n":
        answer = "y" 
        while answer != "y" or answer !="n":
            answer= (input("INVALID OPTION,PLEASE CHOOSE A VALID OPTION:" )).lower()
            if answer == "y" or answer == "n":
                return answer
            

            
        

#-----------------Main Code Below-------------
print("\tHello Welcome to the Fire Regulation Program")

#set control variable
answer = "y"

while answer.lower() == "y":
    #prompt the user for a meeting name
    meeting_name = input("\tPlease enter the name of the meeting:")
    #promt the user for the max capacity
    room_capacity = int(input("\tPlease enter the room capacity:"))
    #prompt the user to enter the amount of people in the meeting
    people_attending = int(input("\tPlease enter how many people are attending:"))
    #call the difference function by attaching it to a variable
    dif = difference(people_attending, room_capacity)
    #create the if statement for if the meeting meets fire regulations
    if people_attending <= room_capacity:
        print("\tThis meeting meets the fire regulations")
        print(F"\t{dif} can attend the meeting and still meet fire regulation.")
    #create the if statement for if the meeting does not meet fire regulations
    if people_attending > room_capacity:
        print("\this meeting does not meet fire regulations ")
        print(F"\t{abs(dif)} must be removed from the meeting to meet fire regulations.")
    #ask the user if they want to enter more information
    answer = input("\tWould you like to enter a another meeting's information[y/n:]").lower()
    #call the decision function by attaching it to answer to ensure a valid option is chosen
    answer = decision(answer)
#display the goodbye statement
print("\tThank you for using this program")