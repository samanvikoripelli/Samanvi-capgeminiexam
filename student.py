name = input("student name")
s1 = float(input("marks for subject 1"))
s2 = float(input("marks for subject 2"))
s3 = float(input("marks for subject 3"))
s4 = float(input("marks for subject 4"))
s5 = float(input("marks for subject 5"))
total = s1 + s2 + s3 + s4 + s5
percentage = total / 5
if percentage >= 90:
    print("grade: A")
elif percentage >= 80:
    print("grade: B")
elif percentage >= 70:
    print("grade: C")
else:
    print("grade: Fail") 