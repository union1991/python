# 윤년 계산기(4의 배수이면서 100의 배수이면 윤년이 아니고, 4의 배수이면서 400의 배수면 윤년이다.)

a = input()
a = int(a)

if(a%4==0 and a%100!=0) : print("1")
elif(a%4==0 and a%400==0) : print("1")
else : print("0")
