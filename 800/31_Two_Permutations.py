# https://codeforces.com/problemset/problem/1761/A
T = int(input())
for cnt in range(T):
    n,a,b = [int(i) for i in input().split()]
    if (a==b and b==n) or (n-(a+b))>1:
        print("YES")
    else:
        print("NO")