# https://codeforces.com/problemset/problem/1820/B
T = int(input())
for _ in range(T):
    s = input()
    n,prev=len(s),-1
    consq=0
    for i in range(n):
        if s[i]=='1':
            consq=max(consq,i-prev)
        else:
            prev=i
    # handle cases like "11011"
    if consq!=n and s[0]=='1' and s[n-1]=='1':
        cur=2
        i=1
        while s[i]==s[i-1]:
            i+=1
            cur+=1
        i=n-2
        while s[i]==s[i+1]:
            i-=1
            cur+=1
        consq=max(consq,cur)
        
    if consq==n:
        print(consq*consq)
    else:
        l=(consq+1)//2
        print(l*(consq+1-l))