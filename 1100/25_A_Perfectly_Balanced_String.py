# https://codeforces.com/problemset/problem/1673/B
T = int(input())
for _ in range(T):
    s = input()
    fq = [0]*26
    n,i=len(s),0
    while i<n and fq[ord(s[i])-ord('a')]==0:
        fq[ord(s[i])-ord('a')]+=1
        i+=1
    k=i
    while i<n and s[i]==s[i-k]:
        i+=1
    print("YES") if i==n else print("NO")