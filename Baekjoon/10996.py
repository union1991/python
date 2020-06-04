# 별찍기 21

import math

a = int(input())
n = 2 * a

for i in range(1,n+1) :
    if i%2==1 :
        print('* '*math.ceil(a/2))
    else :
        print(' *'*int(a/2))
