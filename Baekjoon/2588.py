# 세 자리 두 수를 곱하는 과정을 나타내라.

a = int(input())
b = int(input())

print(int(b%10)*a)
print(((int(b%100)//10)*a))
print((int(b/100)*a))
print(a*b)
