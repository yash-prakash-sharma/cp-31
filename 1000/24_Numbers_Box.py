# https://codeforces.com/problemset/problem/1447/B
T = int(input())
for _ in range(T):
    n,m = list(map(int, input().split()))
    rectangle = [list(map(int, input().split())) for _ in range(n)]
    cnt_neg,sum=0,0
    mini=abs(rectangle[0][0])
    for i in range(n):
        for j in range(m):
            cnt_neg+=rectangle[i][j]<=0
            sum+=abs(rectangle[i][j])
            mini=min(mini,abs(rectangle[i][j]))
    if cnt_neg&1:
        print(sum-2*mini)
    else:
        print(sum)