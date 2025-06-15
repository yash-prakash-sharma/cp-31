# https://codeforces.com/problemset/problem/1862/B
T=int(input())
for cnt in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = []
    b.append(a[0])
    for i in range(1,n):
        if a[i]<a[i-1]:
            b.append(a[i])
        b.append(a[i])
    print(len(b))
    for i in range(len(b)):
        print(b[i],end=" ")
    print()
    