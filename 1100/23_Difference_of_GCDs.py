# https://codeforces.com/problemset/problem/1708/B
T = int(input())
for _ in range(T):
    n,l,r = list(map(int, input().split()))
    flag = True
    res=[]
    for i in range(1,n+1):
        cur=((l+i-1)//i)*i
        if cur<=r: res.append(cur)
        else:
            flag=False
            break
    if flag:
        print("YES")
        print(*res)
    else: print("NO")