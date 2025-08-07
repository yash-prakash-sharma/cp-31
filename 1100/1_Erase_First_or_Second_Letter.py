# https://codeforces.com/problemset/problem/1917/B
T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    seen = set()
    res=0
    for i in range(n):
        seen.add(s[i])
        res+=len(seen)
        # print("for: ", i , " it is", len(seen))
    print(res)