# 알파벳을 입력 받고 해당 자리의 알파

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
