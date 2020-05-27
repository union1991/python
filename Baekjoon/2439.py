# n개의 별찍기 우측 정렬

n = int(input())

for i in range(n) :
    print(" "*(n-(i+1))+"*"*(i+1))
