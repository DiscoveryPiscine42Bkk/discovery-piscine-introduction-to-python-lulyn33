import sys

if len(sys.argv) <= 1:
    print('none')
else:
    para = sys.argv[1:]
    for i in para:
        if i[-3::] != 'ism':
            i = i + 'ism'
            print(i)
        