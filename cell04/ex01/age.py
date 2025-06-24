age = input('Please tell me your age: ')
age = int(age)

print(f"You are currently {age} years old.")
i = 0
ten = 10
while i < 3:
    getting_old = age + ten
    print(f"In {ten} years, you'll be {getting_old} years old.")
    i += 1
    ten += 10
