# https://codeforces.com/problemset/problem/1791/C
T = int(input())
for cnt in range(T):
    n = int(input())
    s = input()
    i,j=0,n-1
    while(i<j):
        if s[i]!=s[j]:
            i+=1
            j-=1
        else:
            break
    print(j-i+1)