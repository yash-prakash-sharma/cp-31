# https://codeforces.com/problemset/problem/1312/B
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(*a)