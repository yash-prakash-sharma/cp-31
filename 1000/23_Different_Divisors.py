# https://codeforces.com/problemset/problem/1474/B
def find_primes(n):
    isPrime = [True]*(n+1)
    p=2
    while p*p<=n:
        if isPrime[p]:
            i=p*p
            while i<=n:
                isPrime[i]=False
                i+=p
        p+=1
    res=[]
    for i in range(2,n+1):
        if isPrime[i]: res.append(i)
    return res
    
def lower_bound(arr, target):
    lo, hi = 0, len(arr) - 1
    res = len(arr)
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] >= target:
            res = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return arr[res]
res = find_primes(50000)
print
T = int(input())
for _ in range(T):
    d = int(input())
    a=1
    a*=lower_bound(res,a+d)
    a*=lower_bound(res,a+d)
    print(a)
    
    
    