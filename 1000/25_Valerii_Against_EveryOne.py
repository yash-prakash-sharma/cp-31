# https://codeforces.com/problemset/problem/1438/B
T = int(input())
for _ in range(T):
    n = int(input())
    b = list(map(int, input().split()))
    s = set()
    flag = False
    for i in range(n):
        if b[i] in s:
            flag=True
            break
        else:
            s.add(b[i])
    print("YES") if flag else print("NO")