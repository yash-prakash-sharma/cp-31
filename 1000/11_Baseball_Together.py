# https://codeforces.com/problemset/problem/1725/B

n,D = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
if D<a[0]:
    print(n)
else:
    i,j=0,n-1
    while(i<j):
        fq=(D+a[j])//a[j]
        if j-i+1<fq: break
        i+=fq-1
        j-=1
        # print(i,j,fq)
    print(n-j-1)