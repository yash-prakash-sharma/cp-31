# https://codeforces.com/problemset/problem/1837/B
T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    consq=1
    cur=1
    for i in range(1,n):
        if s[i]==s[i-1]:
            cur+=1
            consq=max(consq,cur)
        else:
            cur=1
    print(consq+1)   