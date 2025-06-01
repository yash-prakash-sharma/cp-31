# https://codeforces.com/problemset/problem/1881/A
T = int(input())
for cnt in range(T):
    n,m = [int(i) for i in input().split()]
    x = input()
    s = input()
    # ro store x after applying operations
    cur_x=x
    op_cnt=0
    appeared=False
    # since we can apply operation max 5 times as len(cur_x)=2^5=32
    while op_cnt<=5:
        if s in cur_x:
            appeared=True
            break
        cur_x+=cur_x
        op_cnt+=1
        # print(f"In operation {op_cnt}, it became {cur_x}")
    if appeared:
        print(op_cnt)
    else:
        print(-1)