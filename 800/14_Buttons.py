# https://codeforces.com/problemset/problem/1858/A
T = int(input())
for cnt in range(T):
    a,b,c = [int(i) for i in input().split()]
    anna_score=a+(c+1)//2
    katie_score=b+c//2
    if anna_score>katie_score:
        print("First")
    else:
        print("Second")