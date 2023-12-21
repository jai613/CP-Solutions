for i in range(int(input())):
    n=int(input())
    if n%2:
        for i in range(1,n+1):
            print(i,end=' ')
        print()
    else:
        for i in range(1,n+1):
            print(2*i,end=' ')
        print()