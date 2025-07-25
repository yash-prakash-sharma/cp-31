# https://codeforces.com/problemset/problem/1606/A
T = int(input())
for _ in range(T):
    s = input()
    n=len(s)
    if s[0]!=s[n-1]:
        s= s[:n-1] + s[0]
    print(s) 