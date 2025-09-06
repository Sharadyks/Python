Grade = ""
marks = int(input("Enter marks of student: "))

if marks<60:
    Grade = "F"
elif marks<70:
    Grade = "D"
elif marks<80:
    Grade = "C"
elif marks<90:
    Grade = "B"
elif marks<=100:
    Grade = "A"
else : print("Enter valid marks")
print(Grade)