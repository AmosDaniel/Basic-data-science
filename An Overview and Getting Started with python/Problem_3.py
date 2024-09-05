"""
Total Expenses for the Event
 
The prime functionality of an Event Management System is budgeting. An Event Management System should estimate the total expenses incurred by an event and the percentage rate of each of the expenses involved in planning and executing an event. Nikhil, the founder of "Pine Tree" wanted to include this functionality in his company’s Amphi Event Management System and requested your help in writing a program for the same.

The program should get the branding expenses, travel expenses, food expenses and logistics expenses as input from the user and calculate the total expenses for an event and the percentage rate of each of these expenses.

Input Format:
First input is a int value that corresponds to the branding expenses.
Second input is a int value that corresponds to the travel expenses.
Third input is a int value that corresponds to the food expenses.
Fourth input is a int value that corresponds to the logistics expenses.

Output Format:
First line of the output should display the float value that corresponds to the total expenses for the Event.
Next four lines should display the percentage rate of each of the expenses.
Refer sample input and output for formatting specifications.
[All text in bold corresponds to input and rest corresponds to output.]

Sample Input and Output:
Enter branding expenses
20000
Enter travel expenses
40000
Enter food expenses
15000
Enter logistics expenses
25000
Total expenses : Rs.100000.00
Branding expenses percentage : 20.00%
Travel expenses percentage : 40.00%
Food expenses percentage : 15.00%
Logistics expenses percentage : 25.00% 

"""

branding = int(input("Enter branding expenses: ")) # enter expense for branding
travel = int(input("Enter travel expenses: ")) # enter expense for travel
food = int(input("Enter food expenses: ")) # enter expense for food
logistic = int(input("Enter logistic expenses: ")) # enter expense for logistic

total_expense = branding + travel + food + logistic # total expense for brand, travel, food, logistic 

# expense in percentage for each expense after total them
branding_percentage = (branding / total_expense * 100)
travel_percentage = (travel / total_expense * 100)
food_percentage = (food / total_expense * 100)
logistic_percentage = (logistic / total_expense * 100)

print("Total expenses : Rs.", total_expense)
print(f"Branding expenses percentage :  {branding_percentage:.2f} %")
print(f"Travel expenses percentage : {travel_percentage:.2f} %")
print(f"Food expenses percentage : {food_percentage:.2f} %")
print(f"Logistics expenses percentage : {logistic_percentage:.2f} %")



