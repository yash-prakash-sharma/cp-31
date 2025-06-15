# https://codeforces.com/problemset/problem/1845/A
T = int(input())
for cnt in range(T):
    n,k,x = [int(i) for i in input().split()]
    if x==1:
        if k==1 or (k==2 and n&1):
            print("NO")
        else:
            print("YES")
            if n&1:
                print((n-3)//2 + 1)
                n-=3
                print(3, end=" ")
            else:
                print(n//2)
            while n>0:
                print(2, end=" ")
                n-=2
            print()
    else:
        print("YES")
        print(n)
        for i in range(n):
            print(1, end=" ")
        print()    
