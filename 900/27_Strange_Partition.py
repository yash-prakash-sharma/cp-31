# https://codeforces.com/problemset/problem/1471/A
T = int(input())
for _ in range(T):
    n,x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    mini=0
    maxi=0
    for num in a:
        maxi+=(num+x-1)//x
        mini+=num
    mini=(mini+x-1)//x
    print(mini, maxi)