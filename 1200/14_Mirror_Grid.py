# https://codeforces.com/problemset/problem/1703/E
T = int(input())
for _ in range(T):
    n = int(input())
    a = [list(input().strip()) for _ in range(n)]
    res,i,j=0,0,0
    while i<n//2:
        j=i
        while j<n-i-1:
            cnt0,cnt1=0,0
            if a[i][j]=='0':
                cnt0+=1
            else:
                cnt1+=1
            if a[j][n-i-1]=='0':
                cnt0+=1
            else:
                cnt1+=1
            if a[n-i-1][n-j-1]=='0':
                cnt0+=1
            else:
                cnt1+=1
            if a[n-j-1][i]=='0':
                cnt0+=1
            else:
                cnt1+=1
            res+=min(cnt0,cnt1)
            j+=1
        i+=1
    print(res)