# https://codeforces.com/problemset/problem/1837/A
T = int(input())
for cnt in range(T):
    x,k = [int(i) for i in input().split()]
    if x%k==0:
        print(2)
        print(x-1, 1)
    else:
        print(1)
        print(x)