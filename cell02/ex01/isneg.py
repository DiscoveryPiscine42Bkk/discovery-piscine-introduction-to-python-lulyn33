num = input()

try:
    num = int(num)
    if num == 0:
        print("This number is both positive and negative.")
    elif num > 0:
        print("This number is positive.")
    else:
        print("This number is negative.")
        
except:
    num = float(num)
    if num == 0.0:
        print("This number is both positive and negative.")
    elif num > 0:
        print("This number is positive.")
    else:
        print("This number is negative.")
        
