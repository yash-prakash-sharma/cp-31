# https://codeforces.com/problemset/problem/1675/B
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    ops=0
    possible=True
    for i in range(n-2,-1,-1):
        if a[i+1]==0:
            possible=False
            break
        while a[i+1]<=a[i]:
            a[i]//=2
            ops+=1
    print(ops if possible else -1)