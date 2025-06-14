# https://codeforces.com/problemset/problem/1866/A
n = int(input())
a = [int(i) for i in input().split()]
res=100000
for i in range(n):
    res=min(res,abs(a[i]))
print(res)