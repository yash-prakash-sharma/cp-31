# https://codeforces.com/problemset/problem/1857/A
T = int(input())
for cnt in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    freq_odd=0
    for i in range(n):
        if (a[i]&1):
            freq_odd+=1
    if freq_odd&1:
        print("NO")
    else:
        print("YES")