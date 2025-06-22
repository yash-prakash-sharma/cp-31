# https://codeforces.com/problemset/problem/1875/A
T = int(input())
for _ in range(T):
    a,b,n = [int(i) for i in input().split()]
    x = [int(i) for i in input().split()]
    res=b
    for cur in x:
        res+=min(cur,a-1)
    print(res)