# https://codeforces.com/problemset/problem/1692/E
T = int(input())
for _ in range(T):
    n,s = list(map(int, input().split()))
    a = list(map(int, input().split()))
    m = {}
    m[0]=-1
    sum,res=0,-1
    for i in range(n):
        sum+=a[i]
        if m.get(sum-s,-2)!=-2:
            res=max(res,i-m[sum-s])
            # print("len: ", i-m[sum-s])
        if m.get(sum,-2)==-2:
            m[sum]=i
        # print("now, ", i, sum, m)
    print(res) if res==-1 else print(n-res)