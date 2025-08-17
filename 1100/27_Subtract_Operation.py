# https://codeforces.com/problemset/problem/1656/B
T = int(input())
for _ in range(T):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    # need to find el-a[i]=k
    s= set(a)
    flag=False
    for x in a:
        if (k+x) in s:
            flag=True
            break
    print("YES") if flag else print("NO")