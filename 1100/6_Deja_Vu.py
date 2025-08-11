# https://codeforces.com/problemset/problem/1891/B
T = int(input())
for _ in range(T):
    n,q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))
    # https://codeforces.com/problemset/problem/1891/B
T = int(input())
for _ in range(T):
    n,q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))
    """Approach 1
    prev=31
    for i in range(q):
        if x[i]>=prev: continue
        val=(1<<x[i])
        for j in range(n):
            if a[j]%val==0:
                a[j]+=(val>>1)
        prev=x[i]
    print(*a)
    """
    pre = [0]*31
    for i in range(1,31):
        sum,val=0,i
        for el in x:
            if el<=val:
                sum+=(1<<(el-1))
            val=min(val,el-1)
        pre[i]=sum
    res=[]
    for el in a:
        i,cnt=1,0
        while el%i==0:
            i=i<<1
            cnt+=1
        res.append(el+pre[cnt-1])
    print(*res)