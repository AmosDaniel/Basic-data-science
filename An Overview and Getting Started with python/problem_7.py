"""
Command Line Argument- Count
Write a program to accept strings as command line argument and print the number of arguments entered.

Sample Input (Command Line Argument) 1:
Command Arguments

Sample Output 1:
Arguments :
Command
Arguments
Number of arguments is 2

Sample Input (Command Line Argument) 1:
Commands

Sample Output 2:
Arguments :
Commands
Number of arguments is 1

"""

import sys

# Retrieve command-line arguments (excluding the script name)
arguments = sys.argv[1:]

# Print each argument
print("Arguments :")
for arg in arguments:
    print(arg)

# Print the number of arguments
print(f"Number of arguments is {len(arguments)}")
