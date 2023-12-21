def solve():
    n=int(input())
    a=[int(i) for i in input().split()]
    start=1
    for i in range(n):
        if start==a[i]:    
            start=a[i]+1
        start+=1
    print(start-1)
 
 
 
 
t=int(input())
while t:
    solve()
    t-=1