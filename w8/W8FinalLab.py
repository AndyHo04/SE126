#Name - Andy Ho

#Lab 8 - Final Lab

#Program Prompt - Write a program that can be used by a small theater to sell tickets for performances. The theater’s auditorium has 15 rows of seats with 30 seats in each row. The program should display a screen that shows which seats are available and which are taken. Seats thar are available are represented by # and seats that are taken are represent by a *.There are aisles after seats H and V.

#Row                                          Seats
#    A  B  C  D  E  F  G  H     J  K  L  M  N  O  P  Q  R  S  T  U  V     W  X  Y  Z  1  2  3  4
#1   #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #
#2   #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #
#3   #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #
#4   #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #
#5   #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #
#6   #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #
#7   #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #
#8   #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #
#9   #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #
#10  #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #
#11  #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #
#12  #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #
#13  #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #
#14  #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #
#15  #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #  #  #  #  #  #     #  #  #  #  #  #  #  #

#The program should display the above seating map, with # to denote open seats and * to denote taken seats. The user must enter the row and seat numbers for tickets being sold. Every time a ticket or group of tickets is purchased (meaning the user is prompted to enter the seat(s) they wish to choose) the program should also be also displaying the total ticket prices (see page 2 table for pricing) in addition to the current seating chart’s availability. Use a menu to allow your user to do more than just purchase tickets:
#Use a menu to allow your user to do more than just purchase tickets:
# 1. Purchase Seat(s)
# 2. View Total Ticket Sales
# 3. View Sales Information
# 4. Checkout
# 5. Quit
# The program should keep a total of all ticket sales. The user should be given an option of viewing this amount (menu 2).
# The program should also give the user an option to see a list of how many seats have been sold, how many seats are available in each row, and how may seats are available in the entire theater (menu 3).
#The program should allow the user to “check out” ie purchase their tickets. This option should show the user how many tickets they’ve purchased, along with a summary of the seats they’ve chosen, and the total cost for the tickets. Prompt the user for their amount,display their change, and then reset the customer ticket counter – this means a new customer could purchase more tickets without restarting the program, but the Total Ticket Sales and the View Sales Information will stay unchanged. 
#The price for tickets are calculated using the following;
#Row 1 – Row 5 are $200.00
#Row 6 – Row 10 are $175.00
#Row 11 – Row 15 are $150.00

#Variable Dictionary:
#seat_A - list of seats in row A
#seat_B - list of seats in row B
#seat_C - list of seats in row C
#seat_D - list of seats in row D
#seat_E - list of seats in row E
#seat_F - list of seats in row F
#seat_G - list of seats in row G
#seat_H - list of seats in row H
#seat_I - list of seats in row I
#seat_J - list of seats in row J
#seat_K - list of seats in row K
#seat_L - list of seats in row L
#seat_M - list of seats in row M
#seat_N - list of seats in row N
#seat_O - list of seats in row O
#seat_P - list of seats in row P
#seat_Q - list of seats in row Q
#seat_R - list of seats in row R
#seat_S - list of seats in row S
#seat_T - list of seats in row T
#seat_U - list of seats in row U
#seat_V - list of seats in row V
#seat_W - list of seats in row W
#seat_X - list of seats in row X
#seat_Y - list of seats in row Y
#seat_Z - list of seats in row Z
#seat_1 - list of seats in row 1
#seat_2 - list of seats in row 2
#seat_3 - list of seats in row 3
#seat_4 - list of seats in row 4

#menu - function that will give user options
    #choice - user input for the menu

#seat_map - function that will display the seating map
    #row - the row number

#row_get - function that will get the row choice from the user
    #row_choice - the row number

#seat_get - function that will get the seat choice from the user
    #acceptable_seats - list of acceptable seats
    #seat_choice - the seat letters

#more_seats - function that will ask the user if they want to buy more tickets
    #choice - user input for more tickets

#user_choice - user input for the menu
#answer_tickets - user input for they want to buy more tickets
#total_ticket_sales - the total ticket sales
#row_1 - the amount of seats available in row 1
#row_2 - the amount of seats available in row 2
#row_3 - the amount of seats available in row 3
#row_4 - the amount of seats available in row 4
#row_5 - the amount of seats available in row 5
#row_6 - the amount of seats available in row 6
#row_7 - the amount of seats available in row 7
#row_8 - the amount of seats available in row 8
#row_9 - the amount of seats available in row 9
#row_10 - the amount of seats available in row 10
#row_11 - the amount of seats available in row 11
#row_12 - the amount of seats available in row 12
#row_13 - the amount of seats available in row 13
#row_14 - the amount of seats available in row 14
#row_15 - the amount of seats available in row 15
#seats_sold - the amount of seats sold
#seats_available - the amount of seats available in the theater
#tickets_purchased - the amount of tickets the user purchased
#user_total_cost - the total cost for the user
#row1_5cost - the cost of the tickets for row 1-5
#row6_10cost - the cost of the tickets for row 6-10
#row11_15cost - the cost of the tickets for row 11-15
#row_list - list of the rows the user has purchased
#seat_list - list of the seats the user has purchased
#row - used to call the row_get function()
#seat - used to call the seat_get function()
#user_amount - the amount the user is paying
#user_change - the change the user will get back
#display - used to call the seat_map function() at the end of the loop


#--------------------------PROGRAM BEGINS BELOW------------------------------------------

#------------------------------LISTS-----------------------------------------------------
#create empty lists for each row
seat_A = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_B = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_C = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_D = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_E = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_F = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_G = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_H = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_I = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_J = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_K = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_L = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_M = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_N = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_O = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_P = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_Q = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_R = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_S = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_T = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_U = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_V = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_W = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_X = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_Y = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_Z = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_1 = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_2 = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_3 = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
seat_4 = ["#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#",]
#all_rows = []
#for i in range (0, len(row_1)):
#    all_rows.append([row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9, row_10, row_11, row_12, row_13, row_14, row_15])

#------------------------------FUNCTIONS-------------------------------------------------
#menu function that will give user options
def menu():
    print("\t\t1. Purchase Seat(s)")
    print("\t\t2. View Total Ticket Sales")
    print("\t\t3. View Sales Information")
    print("\t\t4. Checkout")
    print("\t\t5. Quit")
    choice = (input("\t\tEnter your choice: "))
    return choice
def seat_map():
    print("\t\tROW\t\t\t\t\t\t\tSEATS")
    print("\t\t\t A  B  C  D  E  F  G  H     I  J  K  L  M  N  O  P  Q  R  S  T  U  V     W  X  Y  Z  1  2  3  4")
    for i in range(0,15):
        row = i + 1#will add the row number for every row
        print(f"\t\t",i + 1,"\t", seat_A[i],"",seat_B[i],"",seat_C[i],"",seat_D[i],"",seat_E[i],"",seat_F[i],"",seat_G[i],"",seat_H[i],"   ",seat_I[i],"",seat_J[i],"",seat_K[i],"",seat_L[i],"",seat_M[i],"",seat_N[i],"",seat_O[i],"",seat_P[i],"",seat_Q[i],"",seat_R[i],"",seat_S[i],"",seat_T[i],"",seat_U[i],"",seat_V[i],"   ",seat_W[i],"",seat_X[i],"",seat_Y[i],"",seat_Z[i],"",seat_1[i],"",seat_2[i],"",seat_3[i],"",seat_4[i])#shows the seat map
#function that will get the row choice from the user
def row_get():
    row_choice = -1 #intialize the row
    while row_choice < 1 or row_choice > 15:#has to be a valid row between 1 and 15
        try:
            row_choice = int(input("\t\tEnter the ROW you wish to sit in [1-15]: "))
            if row_choice < 1 or row_choice > 15:
                print("\t\tNOT A VALID ROW, PLEASE ENTER A VALID ROW [1-15]")
        except:#will show the error but will not break the program
            print("\t\tNOT A VALID ROW, PLEASE ENTER A VALID ROW [1-15]")
    return row_choice

def seat_get():
    acceptable_seats = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4"]#only seats available
    
    seat_choice = input("\t\tEnter the SEAT you wish to sit in [A-Z, 1-4]: ").upper()
    
    if seat_choice not in acceptable_seats:#will check if the seat is valid
        print("\t\tNOT A VALID SEAT, PLEASE ENTER A VALID SEAT [A-Z, 1-4]")
    if seat_choice == "*":#will not allow the user to enter a taken seat
        print("\t\tSorry but that seat is already taken")
    return seat_choice
def more_seats():
    choice = input("\t\tDo you want to continue to add more seats [Y/N]: ").upper()
    return choice

#------------------------------MAIN PROGRAM BELOW----------------------------------------
#initialize variables
user_choice = ""
answer_tickets = "y"
total_ticket_sales = 0
row_1 = 30
row_2 = 30
row_3 = 30
row_4 = 30
row_5 = 30
row_6 = 30
row_7 = 30
row_8 = 30
row_9 = 30
row_10 = 30
row_11 = 30
row_12 = 30
row_13 = 30
row_14 = 30
row_15 = 30
seats_sold = 0
seats_available = 450
tickets_purchased = 0
user_total_cost = 0
row1_5cost = 200
row6_10cost = 175
row11_15cost = 150
row_list = []
seat_list = []
#start of loop
print("\t\tWelcome to the Theater Ticket Program")
while user_choice != "5":
    user_choice = menu()
    if user_choice == "1":#purchase seats
        answer_tickets = "y"
        seat_map()
        while answer_tickets.lower() == "y":
            print("\t\t------TICKET COSTS-------")
            print("\t\tRow 1 - Row 5: $200.00")
            print("\t\tRow 6 - Row 10: $175.00")
            print("\t\tRow 11 - Row 15: $150.00")
            row = row_get()
            seat = seat_get()
            row_list.append(row)#add the rows to the list
            seat_list.append(seat)#add the seats to the list
            tickets_purchased += 1
            if row == 1 or row == 2 or row == 3 or row == 4 or row == 5:
                user_total_cost += row1_5cost#the cost of the tickets for an individual user
                total_ticket_sales += row1_5cost#the total ticket sales of all users
                if row == 1:
                    row_1 -= 1
                elif row == 2:
                    row_2 -= 1
                elif row == 3:
                    row_3 -= 1
                elif row == 4:
                    row_4 -= 1
                elif row == 5:
                    row_5 -= 1
            elif row == 6 or row == 7 or row == 8 or row == 9 or row == 10:
                user_total_cost += row6_10cost
                total_ticket_sales += row6_10cost
                if row == 6:
                    row_6 -= 1
                elif row == 7:
                    row_7 -= 1
                elif row == 8:
                    row_8 -= 1
                elif row == 9:
                    row_9 -= 1
                elif row == 10:
                    row_10 -= 1
            elif row == 11 or row == 12 or row == 13 or row == 14 or row == 15:
                user_total_cost += row11_15cost
                total_ticket_sales += row11_15cost
                if row == 11:
                    row_11 -= 1
                elif row == 12:
                    row_12 -= 1
                elif row == 13:
                    row_13 -= 1
                elif row == 14:
                    row_14 -= 1
                elif row == 15:
                    row_15 -= 1
            seats_sold += 1
            seats_available -= 1
            answer_tickets = more_seats()#ask if the user wants to buy more tickets
    elif user_choice == "2":#View total Ticket Sales
        print(f"\t\tThe total ticket sales is: ${total_ticket_sales}")
    elif user_choice == "3":#View the Sales Information
        print(f"\t\tThe amount of seats sold is {seats_sold}")
        print(f"\t\tThe amount of seats available is {seats_available}")
        #show all the aviable seats in each row
        print(f"\n\t\tThe amount of seats available in row 1 is {row_1}")
        print(f"\n\t\tThe amount of seats available in row 2 is {row_2}")
        print(f"\n\t\tThe amount of seats available in row 3 is {row_3}")
        print(f"\n\t\tThe amount of seats available in row 4 is {row_4}")
        print(f"\n\t\tThe amount of seats available in row 5 is {row_5}")
        print(f"\n\t\tThe amount of seats available in row 6 is {row_6}")
        print(f"\n\t\tThe amount of seats available in row 7 is {row_7}")
        print(f"\n\t\tThe amount of seats available in row 8 is {row_8}")
        print(f"\n\t\tThe amount of seats available in row 9 is {row_9}")
        print(f"\n\t\tThe amount of seats available in row 10 is {row_10}")
        print(f"\n\t\tThe amount of seats available in row 11 is {row_11}")
        print(f"\n\t\tThe amount of seats available in row 12 is {row_12}")
        print(f"\n\t\tThe amount of seats available in row 13 is {row_13}")
        print(f"\n\t\tThe amount of seats available in row 14 is {row_14}")
        print(f"\n\t\tThe amount of seats available in row 15 is {row_15}")
    elif user_choice == "4":#Checkout
        print("\n\n\t\tWelcome to the Checkout")
        print(f"\t\tYou have purchased {tickets_purchased} tickets")
        print(f"\t--------------------SEATS PURCHASED----------------------")
        for i in range(0, len(row_list)):
            print(f"\t\t\t   ROW:{row_list[i]} SEAT:{seat_list[i]}")#show all the rows and seats the user has purchased
        print(f"\t\tThe total cost for all your tickets is: ${user_total_cost}")
        user_amount = float(input("\t\tEnter the amount you are paying: $"))
        if user_amount < user_total_cost:
            print("\t\tSorry but you have not given enough money")
            print("\t\tPlease try again")
            user_amount = float(input("\t\tEnter the amount you are paying: $"))
        user_change = user_amount - user_total_cost
        print(f"\t\tYour change is: ${user_change}")
        print("\t\tThank you for your purchase")
        for i in range(0,len(seat_list)):
            if seat_list[i] == "A":
                if seat_A != "*":
                    seat_A[row_list[i] - 1] = "*"
            elif seat_list[i] == "B":
                if seat_B != "*":
                    seat_B[row_list[i] - 1] = "*"
            elif seat_list[i] == "C":
                if seat_C != "*":
                    seat_C[row_list[i] - 1] = "*"
            elif seat_list[i] == "D":
                if seat_D != "*":
                    seat_D[row_list[i] - 1] = "*"
            elif seat_list[i] == "E":
                if seat_E != "*":
                    seat_E[row_list[i] - 1] = "*"
            elif seat_list[i] == "F":
                if seat_F != "*":
                    seat_F[row_list[i] - 1] = "*"
            elif seat_list[i] == "G":
                if seat_G != "*":
                    seat_G[row_list[i] - 1] = "*"
            elif seat_list[i] == "H":
                if seat_H != "*":
                    seat_H[row_list[i] - 1] = "*"
            elif seat_list[i] == "I":
                if seat_I != "*":
                    seat_I[row_list[i] - 1] = "*"
            elif seat_list[i] == "J":
                if seat_J != "*":
                    seat_J[row_list[i] - 1] = "*"
            elif seat_list[i] == "K":
                if seat_K != "*":
                    seat_K[row_list[i] - 1] = "*"
            elif seat_list[i] == "L":
                if seat_L != "*":
                    seat_L[row_list[i] - 1] = "*"
            elif seat_list[i] == "M":
                if seat_M != "*":
                    seat_M[row_list[i] - 1] = "*"
            elif seat_list[i] == "N":
                if seat_N != "*":
                    seat_N[row_list[i] - 1] = "*"
            elif seat_list[i] == "O":
                if seat_O != "*":
                    seat_O[row_list[i] - 1] = "*"
            elif seat_list[i] == "P":
                if seat_P != "*":
                    seat_P[row_list[i] - 1] = "*"
            elif seat_list[i] == "Q":
                if seat_Q != "*":
                    seat_Q[row_list[i] - 1] = "*"
            elif seat_list[i] == "R":
                if seat_R != "*":
                    seat_R[row_list[i] - 1] = "*"
            elif seat_list[i] == "S":
                if seat_S != "*":
                    seat_S[row_list[i] - 1] = "*"
            elif seat_list[i] == "T":
                if seat_T != "*":
                    seat_T[row_list[i] - 1] = "*"
            elif seat_list[i] == "U":
                if seat_U != "*":
                    seat_U[row_list[i] - 1] = "*"
            elif seat_list[i] == "V":
                if seat_V != "*":
                    seat_V[row_list[i] - 1] = "*"
            elif seat_list[i] == "W":
                if seat_W != "*":
                    seat_W[row_list[i] - 1] = "*"
            elif seat_list[i] == "X":
                if seat_X != "*":
                    seat_X[row_list[i] - 1] = "*"
            elif seat_list[i] == "Y":
                if seat_Y != "*":
                    seat_Y[row_list[i] - 1] = "*"
            elif seat_list[i] == "Z":
                if seat_Z != "*":
                    seat_Z[row_list[i] - 1] = "*"
            elif seat_list[i] == "1":
                if seat_1 != "*":
                    seat_1[row_list[i] - 1] = "*"
            elif seat_list[i] == "2":
                if seat_2 != "*":
                    seat_2[row_list[i] - 1] = "*"
            elif seat_list[i] == "3":
                if seat_3 != "*":
                    seat_3[row_list[i] - 1] = "*"
            elif seat_list[i] == "4":
                if seat_4 != "*":
                    seat_4[row_list[i] - 1] = "*"
            
        #reset the variables for a new user
        user_total_cost = 0
        tickets_purchased = 0
        row_list = []
        seat_list = []
    elif seats_available == 0:
        user_choice = "5"
        print("\t\tSorry but there are no more seats available")
        print("\t\tThank you for using the Theater Ticket Program")
    else:
        display = seat_map()
        print("\t\tThank you for using the Theater Ticket Program")
        #exit the loop
#end of loop
print("\t\tEnjoy your time at the Theater")
#end of program

        

        


