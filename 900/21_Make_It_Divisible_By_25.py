# https://codeforces.com/problemset/problem/1593/B
T = int(input())

def check_existence(num, res, val):
    n=len(num)
    for i in range(n-1,0,-1):
        if num[i]==val[1]:
            ind=i-1
            while ind>=0:
                if num[ind]==val[0]:
                    res=min(res,n-ind-2)
                    return res
                ind-=1
    return res

for _ in range(T):
    num = input()
    res=len(num)
    posible_values = ["00", "25", "50", "75"]
    for val in posible_values:
        res=min(res, check_existence(num,res,val))
    print(res)