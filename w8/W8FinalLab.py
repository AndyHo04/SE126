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



#--------------------------PROGRAM BEGINS BELOW------------------------------------------

#------------------------------LISTS-----------------------------------------------------
#create empty lists for each row
row_1 = ["#", "#", "#", "#", "#" "#", "#", "# ","\t","#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#","\t", "#", "#",  "#", "#", "#", "#", "#", "#"]
row_2 = ["#", "#", "#", "#", "#" "#", "#", "# ","\t","#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#","\t", "#", "#",  "#", "#", "#", "#", "#", "#"]
row_3 = ["#", "#", "#", "#", "#" "#", "#", "# ","\t","#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#","\t", "#", "#",  "#", "#", "#", "#", "#", "#"]
row_4 = ["#", "#", "#", "#", "#" "#", "#", "# ","\t","#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#","\t", "#", "#",  "#", "#", "#", "#", "#", "#"]
row_5 = ["#", "#", "#", "#", "#" "#", "#", "# ","\t","#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#","\t", "#", "#",  "#", "#", "#", "#", "#", "#"]
row_6 = ["#", "#", "#", "#", "#" "#", "#", "# ","\t","#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#","\t", "#", "#",  "#", "#", "#", "#", "#", "#"]
row_7 = ["#", "#", "#", "#", "#" "#", "#", "# ","\t","#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#","\t", "#", "#",  "#", "#", "#", "#", "#", "#"]
row_8 = ["#", "#", "#", "#", "#" "#", "#", "# ","\t","#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#","\t", "#", "#",  "#", "#", "#", "#", "#", "#"]
row_9 = ["#", "#", "#", "#", "#" "#", "#", "# ","\t","#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#","\t", "#", "#",  "#", "#", "#", "#", "#", "#"]
row_10 = ["#", "#", "#", "#", "#" "#", "#", "# ","\t","#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#","\t", "#", "#",  "#", "#", "#", "#", "#", "#"]
row_11 = ["#", "#", "#", "#", "#" "#", "#", "# ","\t","#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#","\t", "#", "#",  "#", "#", "#", "#", "#", "#"]
row_12 = ["#", "#", "#", "#", "#" "#", "#", "# ","\t","#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#","\t", "#", "#",  "#", "#", "#", "#", "#", "#"]
row_13 = ["#", "#", "#", "#", "#" "#", "#", "# ","\t","#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#","\t", "#", "#",  "#", "#", "#", "#", "#", "#"]
row_14 = ["#", "#", "#", "#", "#" "#", "#", "# ","\t","#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#","\t", "#", "#",  "#", "#", "#", "#", "#", "#"]
row_15 = ["#", "#", "#", "#", "#" "#", "#", "# ","\t","#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#","\t", "#", "#",  "#", "#", "#", "#", "#", "#"]
#all_rows = []
#for i in range (0, len(row_1)):
#    all_rows.append([row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9, row_10, row_11, row_12, row_13, row_14, row_15])

#------------------------------FUNCTIONS-------------------------------------------------
def menu():
    print("\t\t1. Purchase Seat(s)")
    print("\t\t2. View Total Ticket Sales")
    print("\t\t3. View Sales Information")
    print("\t\t4. Checkout")
    print("\t\t5. Quit")
    choice = int(input("Enter your choice: "))
    return choice

#------------------------------MAIN PROGRAM BELOW----------------------------------------