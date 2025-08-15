# https://codeforces.com/problemset/problem/1820/B
T = int(input())
for _ in range(T):
    n,k = list(map(int, input().split()))
    mat = [list(map(int,input().split())) for _ in range(n)]
    i,j,cnt=0,0,0
    while i<n-1:
        j=0
        while j<(n-1-i) or (i<n//2 and j==n-1-i):
            if mat[i][j]!=mat[n-1-i][n-1-j]:
                cnt+=1
            j+=1
        i+=1
    poss=False
    if cnt==k or (k>=cnt and (n%2==1 or (k-cnt)%2==0)): poss=True
    print("YES") if poss else print("NO")