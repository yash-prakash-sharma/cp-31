# https://codeforces.com/problemset/problem/1869/B
T = int(input())
for _ in range(T):
    n,k,a,b = list(map(int, input().split()))
    cords = list(tuple(map(int, input().split())) for _ in range(n))
    res=abs(cords[b-1][0]-cords[a-1][0])+abs(cords[b-1][1]-cords[a-1][1])
    mini1,mini2=res,res
    for i in range(k):
        mini1=min(mini1,abs(cords[b-1][0]-cords[i][0])+abs(cords[b-1][1]-cords[i][1]))
        mini2=min(mini2,abs(cords[a-1][0]-cords[i][0])+abs(cords[a-1][1]-cords[i][1]))
    res=min(res,mini1+mini2)
    print(res)