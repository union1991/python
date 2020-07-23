Day 00.

### 리스트

#### 리스트 값 입력
```
list1 = list(map(int, input().split()))
```

#### 리스트 같은 값 입력
```
list2 = [-1]*26
```


#### 리스트 str 값 하나씩 받기
```
list1 = list(input())
```


#### 리스트 중복 값 계산
```
list1={}
list2 = ["a","a","b","b","b","c"]
for i in list2:
    try: list1[i] += 1
    except: list1[i]=1
print(list1)

결과값 : {'a': 2, 'b': 3, 'c': 1}
```


#### 리스트 값 순차 및 역 정렬
```
list1.sort()
list1.sort(reverse=True)

list1=sorted(list2)
print(list1)
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


#### 가장 많이 사용된 알파벳을 대문자로 표현
```
words = input().lower()
words_list = list(set(words))
word_count = list()

for i in words_list:
    count = words.count(i)
    word_count.append(count)

if(word_count.count(max(word_count)) >= 2):
    print('?')
else:
    print(words_list[(word_count.index(max(word_count)))].upper())
```



#### 문자열 잘라서 리스트에 넣기
```
t = input()
list1=[]

for i in range(0,n):
    k = t[i:i+1]
    list1.append(int(k))
```

```
t = input()
list1=[]

for i in t:
    list1.append(i)
```



---


### 출력문

#### 확률 소숫점 3째 자리까지 출력
```
print('%.3f'%(avg*100)+'%')
```


#### 한줄로 리스트 출력
```
for p in range(26):
    print(list1[p], end=' ')
```


#### 문자를 아스키 코드로 변환하여 출력
```
x = input()
print(ord(x))   // 문자를 아스키 코드로


y = int(input())
print(chr(y))     // 아스키 코드를 문자로
```


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

```
