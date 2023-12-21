for _ in range(int(input())):
    n=int(input())
    if n%2:
        print(1,end=' ')
        x=2
        while x+1<=n:
            print(x+1,end=' ')
            print(x,end=' ')
            x+=2
        print()
    else:
        x=1
        while x+1<=n:
            print(x+1,end=' ')
            print(x,end=' ')
            x+=2
        print()