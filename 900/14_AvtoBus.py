# https://codeforces.com/problemset/problem/1679/A
T = int(input())
for _ in range(T):
    n = int(input())
    if n&1 or n<4:
        print(-1)
        continue
    # 4a+6b=n => a=n//4 and b=ceil of 6
    # if n%4==0:
    #     maxi=n//4
    # elif n%4==2:
    #     maxi=(n-6)//4 + 1
    # if n%6==0:
    #     mini=n//6
    # elif n%6==2:
    #     mini=(n-8)//6 + 2
    # elif n%6==4:
    #     mini=(n-4)//6 + 1
    maxi=n//4
    mini=(n+5)//6
    
    print(mini, maxi)