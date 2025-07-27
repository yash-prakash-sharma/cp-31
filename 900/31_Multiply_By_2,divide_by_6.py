# https://codeforces.com/problemset/problem/1374/B
T = int(input())
for _ in range(T):
    n = int(input())
    num=n
    fq2,fq3=0,0
    while num%2==0:
        num//=2
        fq2+=1
    while num%3==0:
        num//=3
        fq3+=1
    if num>1 or fq2>fq3:
        print(-1)
    else:
        print(fq3+(fq3-fq2))