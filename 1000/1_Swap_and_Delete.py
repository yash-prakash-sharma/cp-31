# https://codeforces.com/problemset/problem/1913/B
T = int(input())
for _ in range(T):
    s = input()
    fq_0,fq_1=0,0
    for c in s:
        if c == '0':
            fq_0+=1
        else:
            fq_1+=1

    i,n = 0,len(s)
    while i<n:
        if (s[i]=='0' and fq_1>0) or (s[i]=='1' and fq_0>0):
            fq_0 -= s[i]=='1'
            fq_1 -= s[i]=='0'
            i+=1
        else:
            break
    print(n-i)