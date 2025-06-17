# https://codeforces.com/problemset/problem/1831/A
T = int(input())
for cnt in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [0]*n
    for i in range(n):
        b[i]=n+1-a[i]
        print(b[i], end=" ")
    print()