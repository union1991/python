#알람의 45

h, m = input().split()
h = int(h)
m = int(m)

if(h>0) :
    if(m>44) : print(h, m-45)
    else : print(h-1, m + 15)
else :
    if(m>44) : print(h, m-45)
    else : print(23,m+15)
