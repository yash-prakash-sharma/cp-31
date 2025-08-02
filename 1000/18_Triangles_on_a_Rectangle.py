# https://codeforces.com/problemset/problem/1620/B
T = int(input())
for _ in range(T):
    w,h = list(map(int, input().split()))
    lower_horizontal = list(map(int, input().split()))
    upper_horizontal = list(map(int, input().split()))
    lower_vertical = list(map(int, input().split()))
    upper_vertical = list(map(int, input().split()))
    # for horizontal
    base=max(lower_horizontal[-1]-lower_horizontal[1], upper_horizontal[-1]-upper_horizontal[1])
    res=base*h
    # for vertical
    base=max(lower_vertical[-1]-lower_vertical[1], upper_vertical[-1]-upper_vertical[1])
    res=max(res,base*w)
    print(res)
