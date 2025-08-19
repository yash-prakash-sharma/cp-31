# https://codeforces.com/problemset/problem/1610/B
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    i,j=0,n-1
    while i<j and a[i]==a[j]:
        i+=1
        j-=1
    if i>=j:
        print("YES")
    else:
        op1,op2=a[i],a[j]
        i,j=0,n-1
        while i<j:
            if a[i]!=a[j]:
                if a[i]==op1:
                    i+=1
                elif a[j]==op1:
                    j-=1 
                else:
                    break
            else:
                i+=1
                j-=1
        if i>=j:
            print("YES")
            continue
        i,j=0,n-1
        while i<j:
            if a[i]!=a[j]:
                if a[i]==op2:
                    i+=1
                elif a[j]==op2:
                    j-=1 
                else:
                    break
            else:
                i+=1
                j-=1
        if i>=j:
            print("YES")
        else:
            print("NO")