for _ in range(int(input())):
    n=int(input())
    if n<2050:
        print(-1)
    else:
        if n%2050==0:
            x=n//2050
            k=str(x)
            o=sum([int(i) for i in k])
            print(o)
        else:
            print(-1)