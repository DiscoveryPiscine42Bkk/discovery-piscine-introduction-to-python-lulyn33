var = input()

try:
    var = int(var)
    if var == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
except:
    var = float(var)
    if var == 0.0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
        
    
    
    
