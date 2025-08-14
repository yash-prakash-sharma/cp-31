# https://codeforces.com/problemset/problem/1821/B
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    i,l,r=0,0,n-1
    # original array persist till
    while i<n and a[i]==b[i]:
        i+=1
    # how long sorted subarray exist
    i+=1
    if i!=n: l=i
    while i<n and b[i]>=b[i-1]:
        i+=1
    # to find logest sorted subarray decrease l if we can include more elements from left
    while l>1 and b[l-2]<=b[l-1]:
        l-=1
    print(l, i)