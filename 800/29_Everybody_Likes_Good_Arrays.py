# https://codeforces.com/problemset/problem/1777/A
T = int(input())
for cnt in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    parity=a[0]&1
    res=0
    for i in range(1,n):
        if a[i]&1 == parity:
            res+=1
        else:
            parity=a[i]&1
    print(res)
    
