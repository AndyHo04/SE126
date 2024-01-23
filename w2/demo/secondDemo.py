import csv

#initialize counting vars - counts from file
total_records = 0
total_salaries = 0

#initialize empty lists - 1 list per FIELD
names = []
ages = []
salaries = []

#connect to the file
with open("w2/demo/example.csv") as unicorn:

    #read the file - access
    narwhal = csv.reader(unicorn)

    #go in and "read" each recordin the file
    for rec in narwhal:
        #for"for every record found in the file(entire row of field data)"

        #dislay the data VALUES in NEAT columns
        print(f"{rec[0]:10} \t{rec[1]:3} \t${rec[2]:10}")

        #store data from rec list(current record being read) to list 
        #adding to a list ----> .append() which requires LIST NAME as starting object
        names.append(rec[0]) #NAME
        ages.append(int(rec[1])) #AGES
        salaries.append(float(rec[2])) #SALARY


        #keep literal count of number of records
        total_records += 1

        #keep running total of salaries
        total_salaries += float(rec[2])

#final total displays
print(f"TOTAL RECORDS: {total_records} | TOTAL SALARY: ${total_salaries:.2f}")

#process the lists to display the text file information
#PROCESS LIST --> FOR LOOP!
#for something in something else

for index in range(0, total_records):
    #"for each value in the range of 0 to total number of values in total records"
    print(f"INDEX: {index} \t {names[index]} is {ages[index]} years old")

#process through the list to create a total age value
total_age = 0 
for index in range(0, total_records):
    #add each age to a total age variable
    total_age += ages[index]

#determine the average age. then display
average_age = total_age / total_records
print(f"AVERAGE AGE:{average_age:.2f}")

#what it looks like if we do a while loop(comparison to for loop)
total_age = 0
index = 0 
while index < total_records:
    index += 1
    total_age += ages[index]