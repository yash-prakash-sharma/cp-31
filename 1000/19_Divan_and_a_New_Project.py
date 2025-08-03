# https://codeforces.com/problemset/problem/1614/B
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    pairs=[]
    for i,el in enumerate(a):
        pairs.append((el,i+1))
    res = [0]*(n+1)
    pairs = sorted(pairs, key=lambda x:x[0], reverse=True)
    val=n//2
    res[0]=val
    time_spent=0
    inc,cnt=1,0
    for el,ind in pairs:
        if cnt==0:
            res[ind]=val+inc
            time_spent+=2*inc*el
        else:
            res[ind]=val-inc
            time_spent+=2*inc*el
            inc+=1
        cnt=(cnt+1)%2
    print(time_spent)
    print(*res)