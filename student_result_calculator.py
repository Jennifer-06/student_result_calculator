print("Enter marks obtained in 5 subjects (out of 100):")

subject1 = float(input("Subject 1: "))
subject2 = float(input("Subject 2: "))
subject3 = float(input("Subject 3: "))
subject4 = float(input("Subject 4: "))
subject5 = float(input("Subject 5: "))

total_marks = subject1 + subject2 + subject3 + subject4 + subject5

percentage = (total_marks / 500) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B+"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

print("\nTotal Marks Obtained:", total_marks, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
