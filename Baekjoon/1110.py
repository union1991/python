# 두 개가 왜 다른

a = int(input())
put=int(a)
tmp=int(0)
count=int(0)

while True :
        tmp = a//10 + a%10
        a = (a%10)*10 + (tmp%10)
        tmp = a
        count +=1
        if put == tmp : 
            break
print(count)

'''
a = int(input())
put=int(a)
tmp=int(0)
count=int(0)

while True :
    if put != tmp : 
        tmp = a//10 + a%10
        a = (a%10)*10 + (tmp%10)
        tmp = a
        count +=1
    else :
        print(count)
        break
'''
