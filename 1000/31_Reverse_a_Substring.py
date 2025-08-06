# https://codeforces.com/problemset/problem/1155/A
n = int(input())
s = input()
t = ''.join(sorted(s))
# print(t, s)
if t==s: print("NO")
else: 
    print("YES")
    i=0
    while i <(len(s)-1) and s[i]<=s[i+1]:
        i+=1
    print(i+1, i+2)