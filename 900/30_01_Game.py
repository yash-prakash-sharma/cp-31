# https://codeforces.com/problemset/problem/1373/B
T = int(input())
for _ in range(T):
    s = input()
    fq_0,fq_1=0,0
    for c in s:
        if c=='1': fq_1+=1
        else: fq_0+=1
    no_of_moves=min(fq_0,fq_1)
    print("DA" if no_of_moves&1 else "NET")
    