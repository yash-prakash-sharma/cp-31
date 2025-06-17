# https://codeforces.com/problemset/problem/1834/A
T = int(input())
for cnt in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    pos_fq=0
    for i in range(n):
        if a[i]>0:
            pos_fq+=1
    neg_fq=n-pos_fq
    req_ops=0
    if pos_fq>=neg_fq:
        req_ops+=neg_fq&1
    else:
        req_ops=(neg_fq-pos_fq+1)//2
        req_ops+=(neg_fq-req_ops)&1
    print(req_ops)