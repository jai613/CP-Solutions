for _ in range(int(input())):
 
    n=int(input())
    arr=[int(i) for i in input().split()]
    summ=sum(arr)
    if summ%2==0:
        print('YES')
    else:
        print('NO')