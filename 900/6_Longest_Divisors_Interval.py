# https://codeforces.com/problemset/problem/1855/B
# suppose ans=[l,r] then [1,r-l+1] will also work as it will also have a multiple in [l,r]
# mod property z%n, Ex: z%3=0,1,2 so {1,2,3} for {l,l+1,l+2} as
T = int(input())
for _ in range(T):
    n = int(input())
    res=1
    while(n%res==0):
        res+=1
    print(res-1)