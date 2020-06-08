# 최대 최소 값 구하기
a = int(input())
n = list(map(int, input().split()))

if a == len(n):
    print(min(n),max(n))
else :
    print("Too many or less input NUM")
exit()
