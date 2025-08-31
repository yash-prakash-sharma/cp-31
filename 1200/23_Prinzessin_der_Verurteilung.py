# https://codeforces.com/problemset/problem/1536/B
T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    flag=False
    t=""
    for i in range(26):
        t=chr(ord('a')+i)
        if t not in s:
            flag=True
            break
    for i in range(26):
        if flag:
            break
        for j in range(26):
            t=chr(ord('a')+i)+chr(ord('a')+j)
            if t not in s:
                flag=True
                break
    for i in range(26):
        if flag:
            break
        for j in range(26):
            if flag:
                flag=True
                break
            for k in range(26):
                t=chr(ord('a')+i)+chr(ord('a')+j)+chr(ord('a')+k)
                if t not in s:
                    flag=True
                    break
    print(t)