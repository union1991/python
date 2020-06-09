# 최대값과 위치 찾기

list1=[]

for i in range(9) :
    n = int(input())
    list1.append(n)

big = max(list1)
ind = list1.index(big)
print(big, ind+1)
