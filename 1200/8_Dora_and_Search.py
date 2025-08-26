# https://codeforces.com/problemset/problem/1793/C
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    l,r = 0,n-1
    begin,end=0,n-1
    while l<r:
        if a[l]==b[begin] or a[l]==b[end]:
            if a[l]==b[begin]:
                begin+=1
            else:
                end-=1
            l+=1
        elif a[r]==b[begin] or a[r]==b[end]:
            if a[r]==b[begin]:
                begin+=1
            else:
                end-=1
            r-=1
        else:
            break
    print(l+1, r+1) if l<r else print(-1)