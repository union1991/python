# input 대신 sys.stdin.readline을 사용하여 다수의 합을 구하여라

'''
n = int(input())

for i in range(0, n) :
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(a+b)
'''
import sys

n = int(input())

for i in range(n) :
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
