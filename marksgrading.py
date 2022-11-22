math = int(input("Enter Math marks\n"))
engl = int(input("Enter English marks\n"))
geog = int(input("Enter Geograph marks\n"))
civs = int(input("Enter Civis marks\n"))


def marks_grading(a, b, c, d) -> float:
    total = a + b + c + d
    average = total / 4
    return average


grade = marks_grading(math, engl, geog, civs)
if 0 <= grade <= 29:
    print("You have fail,Your grade is F your Average Marks is ", grade)
elif 30 <= grade <= 44:
    print("You have fail,Your grade is D your Average Marks is ", grade)
elif 45 <= grade <= 64:
    print("You have Pass,Your grade is C your Average Marks is ", grade)
elif 65 <= grade <= 74:
    print("You have Pass,Your grade is B your Average Marks is ", grade)
elif 75 <= grade <= 100:
    print("You have Pass,Your grade is A your Average Marks is ", grade)
else:
    print("Invalid values")
