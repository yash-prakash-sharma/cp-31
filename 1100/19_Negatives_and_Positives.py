# https://codeforces.com/problemset/problem/1791/E
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    cnt,mini,sum=0,1000000000,0
    for i in range(n):
        cnt+=a[i]<0
        sum+=abs(a[i])
        mini=min(abs(a[i]),mini)

    print(sum-2*mini) if cnt&1 else print(sum)