# https://codeforces.com/problemset/problem/1909/B
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    k=0
    while k<=60:
        set,not_set=False,False
        for x in a:
            if x&(1<<k): set=True
            else: not_set=True
        if set and not_set:
            break
        k+=1
    print(1<<(k+1))