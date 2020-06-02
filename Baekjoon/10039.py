# 시험 평균 점수 구하기
 
sum = int(0)

for i in range(5) :
    i = int(input())
    if i >= 40 :
        sum += i
    else :
        i = 40
        sum += i
print(int(sum/5))
