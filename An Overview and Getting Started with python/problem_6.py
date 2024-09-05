"""
Wisconsin State Fair
Wisconsin State Fair is one of the largest midsummer celebrations in the Midwest Allis, showcasing the agriculture skills and prowess of the state. The Event organizers hired few part-time employees to work at the fair and the agreed salary paid to them are as given below:

Weekdays --- 80 / hour
Weekends --- 50 / hour

Justin is a part-time employee working at the fair. Number of hours Justin has worked in the weekdays is 10 more than the number of hours he had worked during weekends. If the total salary paid to him in this month is known, write a program to estimate the number of hours he had worked during weekdays and the number of hours he had worked during weekends.

Input Format:
First line of the input is a double value that corresponds to the total salary paid to Justin.

Output Format:
First line of the output should display the number of hours Justin has worked during the weekdays.
Second line of the output should display the number of hours Justin has worked during the weekends.
Refer sample input and output for formatting specifications.
[All text in bold corresponds to input and rest corresponds to output.]

Sample Input and Output:
Enter the total salary paid
2750
Number of weekday hours is 25
Number of weekend hours is 15

"""

def calculate_hours(total_salary):
    # Calculate the number of weekend hours (E) ensuring integer division
    E = (total_salary - 800) // 130
    # Calculate the number of weekday hours (W)
    W = E + 10
    
    return W, E

def main():
    # Read input from the user
    total_salary = int(input("Enter the total salary paid\n"))
    
    # Calculate the hours worked
    W, E = calculate_hours(total_salary)
    
    # Output the result
    print(f"Number of weekday hours is {W}")
    print(f"Number of weekend hours is {E}")

if __name__ == "__main__":
    main()
