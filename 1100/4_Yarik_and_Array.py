# https://codeforces.com/problemset/problem/1899/C
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    i,j=0,1
    sum,res=a[0],a[0]
    while j<n:
        if (a[j]&1)==(a[j-1]&1) or sum<0:
            i=j
            sum=0
        sum+=a[j]
        res=max(res,sum)
        # print("got: ", j ,sum)
        j+=1
    print(res)