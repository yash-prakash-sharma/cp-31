# https://codeforces.com/problemset/problem/1805/A
T = int(input())
for cnt in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    curr=0
    for i in range(n):
        curr^=a[i]
    if n&1 or curr==0:
        print(curr)
    else:
        print(-1)