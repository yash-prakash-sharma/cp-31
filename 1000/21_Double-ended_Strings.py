# https://codeforces.com/problemset/problem/1506/C
# longest common substring
def lcs(a,b):
    n,m=len(a),len(b)
    prev = [0]*(m+1)
    cur = [0]*(m+1)
    res=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1]==b[j-1]:
                cur[j]=1+prev[j-1]
                res=max(res,cur[j])
            else:
                cur[j]=0
        prev=cur.copy()
    return res

T = int(input())
for _ in range(T):
    a = input()
    b = input()
    res=len(a)+len(b)-2*lcs(a,b)
    print(res)