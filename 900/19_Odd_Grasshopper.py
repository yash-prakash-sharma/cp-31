# https://codeforces.com/problemset/problem/1607/B
T = int(input())
for _ in range(T):
    x,n = list(map(int, input().split()))
    rem=n%4
    if(rem==0):
        print(x)
    elif(rem==1):
        print(x-n if x%2==0 else x+n)
    elif(rem==2):
        print(x+1 if x%2==0 else x-1)
    else:
        print(x+n+1 if x%2==0 else x-(n+1))