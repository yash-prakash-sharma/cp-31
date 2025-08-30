# https://codeforces.com/problemset/problem/1594/C
T = int(input())
for t in range(T):
    n, c = input().split()
    n = int(n)
    s = input()
    fq,ind=0,0
    for i in range(n):
        if s[i]==c:
            fq+=1
            ind=i
    if fq==n:
        print(0)
    else:
        if ind!=0:
            if n>=(2*(ind+1)):
                print(2)
                print(n-1,n)
            else:
                print(1)
                print(ind+1)
        else:
            print(2)
            print(n-1,n)