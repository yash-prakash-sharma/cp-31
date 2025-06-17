# https://codeforces.com/problemset/problem/1829/B
T = int(input())
for cnt in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    res=0
    cur_len=0
    for i in range(n):
        if a[i]==1:
            res=max(res,cur_len)
            cur_len=0
        else:
            cur_len+=1
    print(max(res,cur_len))