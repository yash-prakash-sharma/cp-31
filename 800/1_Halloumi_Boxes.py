#https://codeforces.com/problemset/problem/1903/A
N = int(input())
for cnt in range(1,N+1):
    n,k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    res = True
    #Answer will always be YES except when k=1 and array is unsorted
    if k==1 and n>1:
        for i in range(len(a)-1):
            if a[i+1]<a[i]:
                res=False
                break
    if res:
        print("YES")
    else:
        print("NO")