"""
Total Expenses
The much awaited event at the entertainment industry every year is the "Screen Awards". This year the event is going to be organized on December 25 to honour the Artists for their professional excellence in Cinema. The Organizers has this time decided to launch an online portal to facilitate easy booking of the Award show’s tickets.

They specifically wanted to provide an option for bulk booking in the portal, wherein there are many discounts announced. Write a program to help the Organizers to create the portal as per the requirement given below.
Given the ticket cost as 'X'.
If the number of tickets purchased is less than 50, there is no discount.
If the number of tickets purchased is between 50 and 100 (both inclusive), then 10% discount is offered.
If the number of tickets purchased is between 101 and 200(both inclusive), 20% discount is offered.
If the number of tickets purchased is between 201 and 400(both inclusive), 30% discount is offered.
If the number of tickets purchased is between 401 and 500(both inclusive), 40% discount is offered.
If the number of tickets purchased is greater than 500, then 50% discount is offered.

Input Format:
First line of the input is an integer that corresponds to the cost of the ticket X.
Second line of the input is an integer that corresponds to the number of tickets purchased.

Output Format:
Output should display a double value, which gives the total expenses in purchasing the tickets after discounts. Display the output correct to 2 decimal places.
Refer sample input and output for formatting specifications.

Sample Input 1:
100
5

Sample Output 1:
500.00

Sample Input 2:
100
300

Sample Output 2:
21000.00

"""

# Read the inputs
ticket_price = int(input("\n"))
ticket_number = int(input("\n"))          # the number of tickets

# Calculate the total price based on the ticket number
if ticket_number < 50:
    total_price = ticket_price * ticket_number
elif 50 <= ticket_number <= 100:
    total_price = ticket_price * ticket_number * 0.90  # 10% discount
elif 101 <= ticket_number <= 200:
    total_price = ticket_price * ticket_number * 0.80  # 20% discount
elif 201 <= ticket_number <= 400:
    total_price = ticket_price * ticket_number * 0.70  # 30% discount
elif 401 <= ticket_number <= 500:
    total_price = ticket_price * ticket_number * 0.60  # 40% discount
else:
    total_price = ticket_price * ticket_number * 0.50  # 50% discount

# Print the total price
print(f"{total_price:.2f}")


