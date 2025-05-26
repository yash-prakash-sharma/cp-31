# https://codeforces.com/problemset/problem/1899/A
T = int(input())
for cnt in range(T):
    n=int(input())
    if n%3==0:
        print("Second")
    else:
        print("First")