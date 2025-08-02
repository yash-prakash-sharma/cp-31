# https://codeforces.com/problemset/problem/1632/B
import math
T = int(input())
for _ in range(T):
    n = int(input())
    msb = int(math.log2(n-1))
    val = pow(2, msb)
    for i in range(1,val):
        print(i, end=' ')
    print(0, end=' ')
    for i in range(val,n):
        print(i, end=' ')
    print()