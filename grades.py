# simple_grade_program.py

grade=int(input('enter the grade:'))

if grade >=85:
    print("you got an A+.")
elif grade>=75:
    print("you got an A.")
elif grade>=60:
    print("you got a B.")
elif grade>=55:
    print("you got a C.")
elif grade>=35:
    print("you got a D.")
else:
    print("you failed.")
