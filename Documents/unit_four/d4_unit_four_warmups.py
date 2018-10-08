your_age = int(input("your age is"))

if your_age <= 2:
    ticket = 0
elif 3 <= your_age <= 12:
    ticket = 8
else:
    ticket = 10

print("you have to pay", "$", ticket)
