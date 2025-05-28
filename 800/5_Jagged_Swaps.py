# https://codeforces.com/problemset/problem/1896/A
T = int(input())
for cnt in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    # As we can't sort if first element is not min, otherwise we can always sort
    if a[0]==min(a):
        print("YES")
    else:
        print("NO")