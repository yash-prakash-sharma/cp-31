# https://codeforces.com/problemset/problem/1766/A
T = int(input())
for cnt in range(T):
    n = int(input())
    num=n
    inital_dig=n
    digs=0
    while num>0:
        inital_dig=num
        num//=10
        digs+=1
    print(9*(digs-1)+inital_dig)