# a,b 두 수를 입력하고 비교하여라.

a, b = input().split()
a = int(a)
b = int(b)

if (a > b): print(">")
elif (a == b): print("==")
else: print("<")
