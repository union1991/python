Day 00.

### 리스트

#### 리스트 값 입력
```
list1 = list(map(int, input().split()))
```


#### 리스트 값 순차 및 역 정렬
```
list1.sort
list1.sort(reverse=True)
```


#### 리스트 0번째 제외한 합계
```
sum(list1[1:])
```


#### 리스트 값 더하기
```
list1.append(n)
```


#### 리스트 초기화
```
list1=[]
```


#### 리스트 값 제거
```
del list1[0]
```


#### 문자열 중복 제거
```
n = input()
n = ''.join(set(n))


```





#### 문자열 잘라서 리스트에 넣기
```
t = input()
list1=[]

for i in range(0,n):
    k = t[i:i+1]
    list1.append(int(k))
```


### 출력문

#### 확률 소숫점 3째 자리까지 출력
```
print('%.3f'%(avg*100)+'%')
```


#### 문자를 아스키 코드로 변환하여 출력
```
x = input()
print(ord(x))   // 문자를 아스키 코드로


y = int(input())
print(chr(y))     // 아스키 코드를 문자로
```

n = input()
n = ''.join(set(n))
list1=[]
list2=[]

for j in range(26):
    list2.append(int(-1))

for i in range(len(n)):
    k = n[i:i+1]
    list2[ord(k)-97] = ord(k)-97
#    for o in range(26):
#        if (ord(k)-97) == list2[o]:
#            list2[o]=ord(k)-97

    #list1.append(str(k))


print(list2)
#print(ord(n)-97)


