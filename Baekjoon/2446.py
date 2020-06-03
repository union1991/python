# 모래시계 

a = int(input())
n = 2*a

for i in range(1,n) :
    if i <= a :
        print(' '*(i-1) +'*'*(2*a-(2*i-1)))
    else :
        print(' '*(n-i-1) + '*' * (2*i-n+1))
