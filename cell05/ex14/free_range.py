import sys

if len(sys.argv) == 2:
    print('none')
else:
    first_num = int(sys.argv[1])
    second_num = int(sys.argv[2])
    new_lst = []
    while first_num <= second_num:
        new_lst.append(first_num)
        first_num += 1
    print(new_lst)