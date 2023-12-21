for _ in range(int(input())):
 
    x,y,n=[int(i) for i in input().split()]
    if y-(n*(n-1))//2<x:
        print(-1)
    else:
        g=n*(n-1)//2
        start=y-g
        i=n-1
        k=0
        print(x,end=' ')
        while k<n-1:
            start+=i
            print(start,end=' ')
            i-=1
            k+=1
        print()