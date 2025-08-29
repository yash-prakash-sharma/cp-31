# https://codeforces.com/problemset/problem/1679/B
n,q = list(map(int, input().split()))
a = list(map(int, input().split()))
arr = []
sum,fq,val=0,0,0
for x in a:
    arr.append([x, fq])
    sum+=x
for t in range(q):
    t = list(map(int, input().split()))
    if t[0]==1:
        ind=t[1]-1
        if arr[ind][1]<fq:
            arr[ind][0]=val
            arr[ind][1]=fq
        sum-=arr[ind][0]
        arr[ind][0]=t[2]
        sum+=arr[ind][0]
    else:
        val=t[1]
        sum=n*val
        fq+=1
    print(sum)