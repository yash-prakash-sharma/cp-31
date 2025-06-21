# https://codeforces.com/problemset/problem/1904/A
T = int(input())
for _ in range(T):
    a,b = [int(i) for i in input().split()]
    xk,yk = [int(i) for i in input().split()]
    xq,yq = [int(i) for i in input().split()]
    if a==b:
        moves = [(a,b),(a,-b),(-a,b),(-a,-b)]
    else:
        moves = [(a,b),(a,-b),(-a,b),(-a,-b),(b,a),(b,-a),(-b,a),(-b,-a)]

    visited = {(xk+x,yk+y) for x,y in moves}
    res=sum((xq+x,yq+y) in visited for x,y in moves)
    
    print(res)