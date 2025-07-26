# https://codeforces.com/problemset/problem/1582/B
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    cnt0=0
    cnt1=0
    for x in a:
        cnt0+=x==0
        cnt1+=x==1
    print(cnt1*(2**cnt0))