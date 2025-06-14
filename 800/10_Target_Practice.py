# https://codeforces.com/problemset/problem/1873/C
T = int(input())
for cnt in range(T):
    grid = [input().strip() for _ in range(10)]
    points=0
    for i in range(10):
        for j in range(10):
            if grid[i][j]=='X':
                val_i=min(i,9-i)
                val_j=min(j,9-j)
                if val_i==4 and val_j==4:
                    points+=5
                elif val_i>=3 and val_j>=3:
                    points+=4
                elif val_i>=2 and val_j>=2:
                    points+=3
                elif val_i>=1 and val_j>=1:
                    points+=2
                else:
                    points+=1
    print(points)