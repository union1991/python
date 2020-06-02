# 두 번째로 큰 수를 출력

a,b,c = map(int, input().split())
list1 =[a,b,c]

if a == max(list1) :
    if b > c :
        print(b)
    else :
        print(c)
elif b == max(list1) :
    if a > c :
        print(a)
    else :
        print(c)
else :
    if a > b :
        print(a)
    else :
        print(b)

        
        
 '''
 다른 사람 코드
 
 a,b,c = map(int, input().split())
 
 M = max(a,b,c)
 N = min(a,b,c)
 
 print(a + b + c -N -M)

 '''


