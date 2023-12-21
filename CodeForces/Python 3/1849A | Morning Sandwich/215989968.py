for _ in range(int(input())):
 
    arr=[int(i) for i in input().split()]
    b,c,h=arr[0],arr[1],arr[2]
    if b>c+h:
        print(2*(c+h)+1)
    elif b<=c+h:
        print(2*b-1)