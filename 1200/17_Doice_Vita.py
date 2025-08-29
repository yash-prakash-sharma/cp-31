# https://codeforces.com/problemset/problem/1671/C
import bisect
def solve(sum,x,mid,cnt):
    return x >= sum+(mid-1)*cnt
T = int(input())
for _ in range(T):
    n,x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = sorted(a)
    days=x-b[0]+1
    sum,res=b[0],max(0,days)
    for i in range(1,n):
        sum+=b[i]
        if sum>x:
            break
        l,r=1,days
        while l<=r:
            mid=(l+r)>>1
            if solve(sum,x,mid,i+1):
                l=mid+1
            else:
                r=mid-1
        days=r
        res+=r
    print(res)