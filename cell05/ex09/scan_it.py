import sys
import re

param = sys.argv

if len(param) <= 2:
    print('none')
else:
    scan = re.findall(param[1], param[2])
    print(len(scan))