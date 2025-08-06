# https://codeforces.com/problemset/problem/1411/B
T = int(input())
for _ in range(T):
    n = int(input())
    # TC O(2520*18) 2520=LCM(1,2,..9)
    while True:
        s = str(n)
        flag2=True
        for c in s:
            dig=ord(c)-ord('0')
            if dig>1 and n%dig!=0:
                flag2=False
                break
        if flag2:
            break
        n+=1
    print(n)