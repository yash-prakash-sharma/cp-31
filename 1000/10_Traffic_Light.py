# https://codeforces.com/problemset/problem/1744/C
T = int(input())
for _ in range(T):
    n, c = input().split()
    n = int(n)
    s = input()
    if c=='g':
        print(0)
        continue
    i=0
    res=0
    while i < n:
        if s[i]=='g': break
        i+=1
    prev=i
    i=n-1
    while i>=0:
        if s[i]==c:
            if prev<i: res=max(res,n-i+prev)
            else: res=max(res, prev-i)
        elif s[i]=='g':
            prev=i
        i-=1
    print(res)