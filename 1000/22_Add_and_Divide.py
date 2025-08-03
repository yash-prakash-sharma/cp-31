# https://codeforces.com/problemset/problem/1485/A
"""
Intution
(b+x)^y>a 
y > log(a)/log(b+x)
y = ceil(log(a)/log(b+x))
We can see that when x increases y decreases and viceversa
So lets start with x=0 and do x+=1 till (x+y) keeps on decreasing or reaches worst case(10^9, 1)=31, once it starts increasing we have passed optimal solution so exit
"""
import math
# T = int(input())
# for _ in range(T):
#     a,b = list(map(int, input().split()))
#     res=a+1
#     if b==1: x=1
#     else: x=0
#     while x<=32:
#         y = math.ceil(math.log(a)/math.log(b+x))
#         # print("val: ", x, y)
#         if pow(b+x,y)==a: res=min(res,x+y+1)
#         else: res=min(res,x+y)
#         # print("cur: ", res)
#         if x+y>res: break
#         x+=1
#     print(res)
T = int(input())
for _ in range(T):
    a,b = list(map(int, input().split()))
    res=1000000000
    for x in range(32):
        new_b=b+x
        if new_b==1: continue
        new_a,y=a,0
        while new_a>0:
            new_a//=new_b
            y+=1
        res=min(res,x+y)
    print(res)