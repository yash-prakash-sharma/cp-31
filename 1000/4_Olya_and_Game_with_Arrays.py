# https://codeforces.com/problemset/problem/1859/B
T = int(input())
for _ in range(T):
    n = int(input())
    res=0
    mini=1000000000
    least=mini
    mini_index=0
    for ind in range(n):
        m = int(input())
        a = list(map(int, input().split()))
        min1,min2=1000000000,1000000000
        for x in a:
            if x<=min1:
                min2=min1
                min1=x
            elif x<min2:
                min2=x
        res+=min2
        mini=min(mini,min2)
        least=min(least, min1)
        mini_index=ind
    print(res-mini+least)