for _ in range(int(input())):
 
    n=int(input())
    arr=[int(i) for i in input().split()]
    c=0
    for i in range(n):
        if arr[i]==i+1:
            c+=1
    if c%2==0:
        print(c//2)
    else:
        print(c//2+1)