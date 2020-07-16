# 평균보다 높은 학생 비율 출력

n = int(input())

for i in range(n):
    case1 = list(map(int, input().split()))
    avg = (sum(case1)-case1[0])/case1[0]
    del case1[0]
    case1.sort(reverse=True)
    fin = int(0)
    for j in range(len(case1)):
        if case1[j] > avg:
            fin +=1
        else :
            break
    fin = float((fin/len(case1)))
    print('%.3f'%(fin*100)+'%')
