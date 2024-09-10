"""
Salary Computation
Danny has recently got his job offer as an Event Concept Creator at Sparsh Event Services. The Company has sent him a detailed salary structure with details of his basic salary, HRA and DA. The Company has promised to pay him as under:

If his basic salary is less than Rs. 15000, then HRA = 15% of basic salary and DA = 90% of basic salary.
If his basic salary is either equal to or above Rs. 15000, then HRA = Rs. 5000 and DA = 98% of basic salary.

If the Danny’s salary is given as input, write a program to find his gross salary.

Note : Gross Salary = Basic Salary+HRA+DA
 
Input Format:
First line of the input is an integer that corresponds to the basic salary of Danny.

Output Format:
Output should display the double value that refers to the gross salary of Danny. Display the output correct to 2 decimal places.
Refer sample input and output for formatting specifications.

Sample Input 1:
12000

Sample Output 1:
24600.00

Sample Input 2:
30000

Sample Output 2:
64400.00

"""

basic_salary = int(input("\n")) # enter salary for Danny

GrossSalary1 = basic_salary + (15 / 100 * basic_salary) + (90 / 100 * basic_salary) # gross salary if less than 15000
GrossSalary2 = basic_salary + 5000 + (98 / 100 * basic_salary) # gross salary if equal or more than 15000

if basic_salary < 15000: # condition to determine gross for Danny
    print(f"{GrossSalary1:.2f}")
elif basic_salary >= 15000:
    print(f"{GrossSalary2:.2f}")
else:
    print(f"try again")


