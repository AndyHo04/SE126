#Name - Andy Ho

#Lab 1

#Date - 1/9/24

# Program Prompt: You will be writing one Python file for this project - it is a program that determines  whether a meeting room is in violation of fire regulations regarding the maximum room capacity. Theprogram will accept the maximum room capacity and the number of people attending the meeting. If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal to hold the meeting and tells how many additional people may legally attend. If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how any people must be excluded in order to meet the fire regulations. The user should be allowed to enter and check as many rooms as they would like without exiting the program.

#variable dictionary:


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
            answer= (input("INVALID OPTION,PLEASE CHOOSE A VALID OPTION:" ))
            if answer == "y" or answer == "n":
                return answer
            

            
        

#-----------------Main Code Below-------------
print("\tHello Welcome to the Fire Regulation Program")

#set control variable
answer = "y"

while answer.lower() == "y":
    meeting_name = input("\tPlease enter the name of the meeting:")
    room_capacity = int(input("\tPlease enter the room capacity:"))
    people_attending = int(input("\tPlease enter how many people are attending:"))
    dif = difference(people_attending, room_capacity)
    if people_attending <= room_capacity:
        print("\tThis meeting meets the fire regulations")
        print(F"\t{dif} can attend the meeting and still meet fire regulatiom")
    if people_attending > room_capacity:
        print("\this meeting does not meet fire regulations ")
        print(F"\t{abs(dif)} must be removed from the meeting to meet fire regulations.")
    answer = input("\tWould you like to enter a another meeting's information[y/n:]")
    answer = decision(answer)
print("\tThank you for using this program")