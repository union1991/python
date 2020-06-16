# 연속되는 O

n = int(input())

for i in range(n) : 
    score = int(0)
    stack = int(0)
    list1 = list(map(str, input()))
    for u in range(len(list1)) :
        if list1[u] == 'O' :
            stack += 1
            score +=stack
        else :
            stack = 0
    print(score)

