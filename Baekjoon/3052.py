# 서로 다른 나머지 값

list1 =[]
list2 =[]
n = int(0)

for i in range(10):
    a = int(input())
    list1.append(a%42)
    list2.append(list1.count(list1[i]))
    if list2[i] == 1 :
        n = n + 1

print(n)
