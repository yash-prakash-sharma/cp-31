# https://codeforces.com/problemset/problem/1814/A
T = int(input())
for cnt in range(T):
    n,k = [int(i) for i in input().split()]
    if n%2==0 or (n-k)%2==0:
        print("YES")
    else:
        print("NO")