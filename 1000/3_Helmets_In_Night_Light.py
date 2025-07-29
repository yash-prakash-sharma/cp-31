# https://codeforces.com/problemset/problem/1876/A
T = int(input())
for _ in range(T):
    n,p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res=0
    fq=n-1
    pairs=list(zip(a,b))
    pairs=sorted(pairs,key=lambda x:x[1])
    ind=0
    while fq>0 and ind<n and pairs[ind][1]<p:
        cur_fq=min(pairs[ind][0],fq)
        res+=pairs[ind][1]*cur_fq
        fq-=cur_fq
        ind+=1
    print(res+(fq+1)*p)