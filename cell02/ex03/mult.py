#!/usr/bin/env python3
print("Enter the first number:")
num_1 = float(input())
num_1 = int(num_1) if num_1.is_integer() else num_1
print("Enter the second number:")
num_2 = float(input())
num_2 = int(num_2) if num_2.is_integer() else num_2

result = num_1 * num_2
print(f"{num_1} x {num_2} = {result}")

if result == 0:
    print("The result is positive and negative.")
elif result > 0:
    print("This result is positive.")
else:
    print("The result is negative.")

