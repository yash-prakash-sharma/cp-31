# https://codeforces.com/problemset/problem/1788/A
T = int(input())
for cnt in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    freq2=0
    for i in range(n):
        freq2+=a[i]==2
    if freq2%2==0:
        freq2/=2
        cnt=a[0]==2
        i=1
        while cnt!=freq2:
            cnt+=a[i]==2
            i+=1
        print(i)
    else:
        print(-1)