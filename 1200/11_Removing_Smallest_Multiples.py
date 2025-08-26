# https://codeforces.com/problemset/problem/1734/C
T = int(input())
for _ in range(T):
    n = int(input())
    str = input()
    s = list(str)
    res=0
    for i in range(n):
        if s[i]!='1':
            k=i+1
            j=k
            while j<=n and s[j-1]!='1':
                if s[j-1]=='0':
                    res+=k
                s[j-1]='-1'
                j+=k
    print(res)