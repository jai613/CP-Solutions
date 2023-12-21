for _ in range(int(input())):
 
    n=int(input())
    sum=0
    while n:
        sum+=n
        n//=2
    print(sum)