# https://codeforces.com/problemset/problem/1878/A
T = int(input())
for cnt in range(T):
    n,k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    # if k appears in a even once we can select we can select subsegment of length 1 with it
    # So we only need to check if k exists in a
    if k in a:
        print("YES")
    else:
        print("NO")