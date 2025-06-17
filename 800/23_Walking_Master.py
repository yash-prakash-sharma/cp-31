# https://codeforces.com/problemset/problem/1806/A
T = int(input())
for cnt in range(T):
    a,b,c,d = [int(i) for i in input().split()]
    vertical_dist=d-b
    if vertical_dist<0 or c>a+vertical_dist:
        print(-1)
    else:
        print(vertical_dist+abs(a+vertical_dist-c))