#https://codeforces.com/problemset/problem/1900/A
T = int(input())
for cnt in range(T):
    n = int(input())
    s = input()
    # in case 3 '.' exist answer will be 2 as we can use as many operation 2 we want
    infinite_supply=False
    # total to count total '.' in case no infinite_supply exist
    # consq to keep track of consecutive '.'
    if s[0]=='#':
        total=0
        consq=0
    else:
        total=1
        consq=1
    for i in range(1,len(s)):
        if s[i]=='#':
            if consq>=1:
                consq=0
        else:
            consq+=1
            total+=1
            if consq>2:
                infinite_supply=True
                break
    
    if infinite_supply:
        print(2)
    else:
        print(total)