for _ in range(int(input())):
 
    n=int(input())
    arr=[int(i) for i in input().split()]
    odd=even=0
    for i in arr:
        if i%2:
            odd+=1
        else:
            even+=1
    if odd and even:
        print('YES')
    else:
        if not odd:
            print('NO')
        else:
            if odd%2:
                print('YES')
            else:
                print('NO')