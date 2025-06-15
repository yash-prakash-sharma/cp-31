# https://codeforces.com/problemset/problem/1859/A
T = int(input())
for cnt in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    min_ele=min(a)
    fq=0
    for i in range(n):
        if a[i]==min_ele:
            fq+=1
    if fq==n:
        print(-1)
    else:
        print(fq, n-fq)
        for i in range(fq):
            print(min_ele, end=" ")
        print()
        for i in range(n):
            if a[i]!=min_ele:
                print(a[i], end=" ")
        print()