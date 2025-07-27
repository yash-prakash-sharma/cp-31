# https://codeforces.com/problemset/problem/1537/B
T = int(input())
for _ in range(T):
    n,m,i,j = list(map(int, input().split()))
    # as diagonally opp will make him travel farthest
    print(1, 1, n, m)
