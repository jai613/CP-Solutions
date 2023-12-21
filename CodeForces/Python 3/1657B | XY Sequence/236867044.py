for _ in range(int(input())):
    n,B,x,y=[int(i) for i in input().split()]
    ans=0
    array=[0]*(n+1)
    for i in range(1,len(array)):
        if array[i-1]+x<=B:
            array[i]=array[i-1]+x
        else:
            array[i]=array[i-1]-y
        ans+=array[i]
    print(ans)