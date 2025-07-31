# https://codeforces.com/problemset/problem/1791/D
T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    # store frequency of unique elements upto i from prefix and suffix
    pre_fq = [0]*n
    post_fq = [0]*n
    # for prefix
    vis = [False]*26
    pre_fq[0]=1
    vis[ord(s[0])-ord('a')]=True
    for i in range(1,n):
        if vis[ord(s[i])-ord('a')]==False: pre_fq[i]=pre_fq[i-1]+1
        else: pre_fq[i]=pre_fq[i-1]
        vis[ord(s[i])-ord('a')]=True
    # for suffix and get result
    vis = [False]*26
    post_fq[n-1]=1
    vis[ord(s[n-1])-ord('a')]=True
    res=pre_fq[n-2]+post_fq[n-1]
    for i in range(n-2,0,-1):
        if vis[ord(s[i])-ord('a')]==False: post_fq[i]=post_fq[i+1]+1
        else: post_fq[i]=post_fq[i+1]
        vis[ord(s[i])-ord('a')]=True
        res=max(res,pre_fq[i-1]+post_fq[i])
    print(res)