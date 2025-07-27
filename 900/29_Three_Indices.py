# https://codeforces.com/problemset/problem/1380/A
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    possible=False
    for i in range(1,n-1):
        if a[i]>a[i-1] and a[i]>a[i+1]:
            print("YES")
            print(i, i+1, i+2)
            possible=True
            break
    if possible==False:
        print("NO")