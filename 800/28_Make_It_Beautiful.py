# https://codeforces.com/problemset/problem/1783/A
T = int(input())
for cnt in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    res=False
    for i in range(1,n):
        if a[i]!=a[i-1]:
            res=True
            break
    if res:
        print("YES")
        a.sort(reverse=True)
        if a[1]==a[0]:
            a[0],a[n-1]=a[n-1],a[0]
        for i in range(n):
            print(a[i], end=" ")
        print()
    else:
        print("NO")