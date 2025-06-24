import sys

parameter = sys.argv
print(f"parameters: {len(parameter)}")
for i in parameter[1:]:
    print(f"{i} : {len(i)}")