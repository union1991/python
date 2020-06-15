# 사용된 숫자 개수

a, b, c = map(int, input().split())
mult = a * b * c
mult = str(mult)

for i in range(0, 10):
    print(mult.count(str(i)))
