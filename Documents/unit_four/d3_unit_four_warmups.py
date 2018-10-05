grade = int(input("What grade are you in?"))

if grade <= 5:
    print("You are in lower school.")
elif 5 < grade < 9:
    print("You are in middle school.")
else:
    print("You are in high school.")