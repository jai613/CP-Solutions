for _ in range(int(input())):
    n=int(input())
    ans=4*n+(n-1)+2*((n-2)*(n-1)//2-1)+3
    print(ans)
        