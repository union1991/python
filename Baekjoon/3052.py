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


### 다른 사람 코드
'''
num_list = []
for _ in range(10):
    num = int(input())
    num_list.append(num % 42)
num_list = set(num_list)    // 'set' 중복된 값을 제외해준다.
print(len(num_list))
'''
