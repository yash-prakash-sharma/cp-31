# https://codeforces.com/problemset/problem/1890/A
T = int(input())
for cnt in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    # b1+b2=b2+b3=b3+b4=…=bn−1+bn=k
    # b1 = b3 = b5 = ... bn if n odd else bn-1
    # b2 = b4 = b6 = ... bn if n even else bn-1
    # so there can be only 2 different integers with equal freq if n even
    # or with difference 1 in freq if n is odd
    # also consider edge case when all element equal
    val1,val2=-1,-1
    cnt1,cnt2=0,0
    is_possible=True
    for i in range(n):
        if a[i]==val1:
            cnt1+=1
        elif a[i]==val2:
            cnt2+=1
        else:
            if val1==-1:
                val1=a[i]
                cnt1=1
            elif val2==-1:
                val2=a[i]
                cnt2=1
            else:
                is_possible=False
                break
    if is_possible and cnt2==0:
        print("Yes")
    elif is_possible and n%2==0 and cnt1==cnt2:
        print("Yes")
    elif is_possible and n%2==1 and abs(cnt1-cnt2)==1:
        print("Yes")
    else:
        print("No")
    
