# 사용된 숫자 개수

a = int(input())
b = int(input())
c = int(input())
mult = a * b * c
mult = str(mult)

for i in range(0, 10):
    print(mult.count(str(i)))
