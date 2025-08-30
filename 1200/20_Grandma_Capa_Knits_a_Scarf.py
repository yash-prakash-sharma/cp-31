# https://codeforces.com/problemset/problem/1582/C
def solve(s, c):
    l,r,res=0,len(s)-1,0
    while l<r:
        if s[l]==s[r]:
            l+=1
            r-=1
        else:
            if s[l]==c:
                l+=1
                res+=1
            elif s[r]==c:
                r-=1
                res+=1
            else:
                return -1
    return res
T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    i,j=0,n-1
    while i<j and s[i]==s[j]:
        i+=1
        j-=1
    if i==j:
        print(0)
    else:
        val1=solve(s,s[i])
        val2=solve(s,s[j])
        if val1==-1 or val2==-1:
            print(max(val1, val2))
        else:
            print(min(val1,val2))