# https://codeforces.com/problemset/problem/1883/B
T = int(input())
for _ in range(T):
    n,k = [int(i) for i in input().split()]
    s = input()
    freq = [0] * 26
    for i in range(n):
        freq[ord(s[i])-ord('a')]+=1
    odd_freq=0
    for val in freq:
        odd_freq+=val&1
    if odd_freq<=k+1:
        print("YES")
    else:
        print("NO")