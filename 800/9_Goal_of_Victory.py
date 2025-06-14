# https://codeforces.com/problemset/problem/1877/A
T = int(input())
for cnt in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    total_sum=sum(a)
    # since sum of efficieny will be 0, (a-b)+(b-a)=0 
    total_sum*=-1
    print(total_sum)