# https://codeforces.com/problemset/problem/1869/A
T = int(input())
for _ in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    if n&1:
        print(4)
        print(1, n-1)
        print(1, n-1)
        print(n-1, n)
        print(n-1, n)
    else:
        print(2)
        print(1, n)
        print(1, n)
