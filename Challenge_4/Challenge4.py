print("Enter a value between 0 and 100 for each mark\n")

labGrade = input("Weekly labs: ")
practiceGrade = input("Daily practice: ")
labExamGrade = input("Lab Exam: ")
quiz1Grade = input("Quiz 1: ")
quiz2Grade = input("Quiz 2: ")
quiz3Grade = input("Quiz 3: ")
ass1Grade = input("Assignment 1: ")
ass2Grade = input("Assignment 2: ")
ass3Grade = input("Assignment 3: ")
finalExamGrade = input("How much do you desire as an overall grade in CIS 1500: ")

###################### Your code here ##############################

currCouseMark = "0"
examPoints = "0"
examPercentage = "0"

###################################################################

print("**************************************************")
print("Assessment\t\tWeight\t\tMarks\t\t")
print("--------------------------------------------------")
print("Weekly Labs\t\t10\t\t" + labGrade)
print("Daily Practice\t\t10\t\t" + practiceGrade)
print("Lab Exam\t\t10\t\t" + labExamGrade)
print("Quiz 1\t\t\t5\t\t" + quiz1Grade)
print("Quiz 2\t\t\t5\t\t" + quiz2Grade)
print("Quiz 3\t\t\t5\t\t" + quiz3Grade)
print("Assignment 1\t\t5\t\t" + ass1Grade)
print("Assignment 2\t\t7\t\t" + ass2Grade)
print("Assignment 3\t\t8\t\t" + ass3Grade)
print("Final Exam\t\t35\t\tTo be determined")
print("**************************************************")
print("Current course mark = " + currCouseMark + " out of 65.00")
print("You need " + examPoints + " / 35.00 to reach your goal (" + finalExamGrade + "%)")
print("In percentage, you need " + examPercentage + "% to reach your goal (" + finalExamGrade + "%)")
print("**************************************************")
