# https://codeforces.com/problemset/problem/1475/A
T = int(input())
for _ in range(T):
    n = int(input())
    print("YES" if n>2 and(n&1 or n&(n-1)!=0) else "NO")
