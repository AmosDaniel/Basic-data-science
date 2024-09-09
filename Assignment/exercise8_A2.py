"""
Write a Python program that takes a score (between 0 and 100) as input and 
prints the corresponding grade based on the following criteria:

A for scores 90 and above

B for scores 80-89

C for scores 70-79

D for scores 60-69

F for scores below 60


"""

mark = int(input("Enter the mark of the student: "))

if (mark >= 90):
    print("Grade A")
elif (mark >= 80 and mark < 90):
    print("Grade B")
elif (mark >= 70 and mark < 80):
    print("Grade C")
elif (mark >= 60 and mark < 70):
    print("Grade D")
else:
    print("Grade F")




