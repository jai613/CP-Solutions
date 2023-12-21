for _ in range(int(input())):
    n=int(input())
    if n==2:
        print(-1)
        continue
    z=[i for i in range(1,n**2+1) if i%2]+[i for i in range(1,n**2+1) if not i%2]
    for i in range(0,n**2,n):
        print(*z[i:i+n])