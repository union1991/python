# 시험 점수 조작

n = int(input())
score = list(map(int, input().split()))
result = int(0)

if len(score) != n :
    print("plz input",n,"number")
else :
    for i in range(n) : 
        maxS = max(score)
        result += score[i] * 100 / maxS
    print(result / n)
