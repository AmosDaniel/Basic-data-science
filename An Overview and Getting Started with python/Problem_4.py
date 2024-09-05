"""
Tickets sold for Charity Event
HelpIndia, a famous NGO has been selective in identifying events to raise funds for charity. Suzanne is a volunteer from the NGO who was selling tickets to the public for the charity event. She sold 'X' more adult tickets than children tickets and she sold twice as many senior tickets as children tickets. Assume that an adult ticket costs $5, children ticket costs $2 and senior ticket costs $3.
Suzanne made 'Y' dollars from ticket sales. Find the number of adult tickets, children tickets, and senior tickets sold.

 
Input Format:
The first input is an integer value X that corresponds to the number of adult tickets more than children tickets.
The second input is an integer value Y that corresponds to the money in dollars made by Suzanne from ticket sales.

Output Format:
The first line of the output should display the number of children tickets sold.
The second line of the output should display the number of adult tickets sold.
The third line of the output should display the number of senior tickets sold.
Refer sample input and output for formatting specifications.
[All text in bold corresponds to input and rest corresponds to output.]

Sample Input and Output :
Enter the value of X
10
Enter the value of Y
700
Number of children tickets sold : 50
Number of adult tickets sold : 60
Number of senior tickets sold : 100

"""

# enter the ticket sold
ticket_sold = int(input("Enter the value of X\n"))
total_money = int(input("Enter the value of Y\n"))

child_ticket = (total_money - 5 * ticket_sold) // 13
adult_ticket = child_ticket + ticket_sold
senior_ticket = 2 * child_ticket

print(f"Number of children tickets sold : {child_ticket}")
print(f"Number of adult tickets sold : {adult_ticket}",)
print(f"Number of senior tickets sold : {senior_ticket}",)