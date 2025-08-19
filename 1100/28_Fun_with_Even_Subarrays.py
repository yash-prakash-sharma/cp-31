# https://codeforces.com/problemset/problem/1631/B
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    i,res=n-1,0
    while i>=0 and a[i]==a[n-1]:
        i-=1
    while i>=0:
        i-=(n-i-1)
        res+=1
        while i>=0 and a[i]==a[n-1]:
            i-=1
    print(res)