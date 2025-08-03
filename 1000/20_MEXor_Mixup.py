# https://codeforces.com/problemset/problem/1567/B
def xor_upto_n(n):
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:  # n % 4 == 3
        return 0

T = int(input())
for _ in range(T):
    a,b = list(map(int, input().split()))
    res=a
    xr=xor_upto_n(a-1)
    if xr==b: print(res)
    else:
        if b^xr==a:
            print(res+2)
        else: 
            print(res+1)
    