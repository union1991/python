# 상근날드

ham = int(2000)
soda = int(2000)

for i in range(5) :
    a = int(input())
    if i < 3  :
        if a < ham :
            ham = a
        else :
            ham = ham
    else : 
        if a < soda :
            soda = a
        else :
            soda = soda

print(int(ham)+int(soda)-50)
