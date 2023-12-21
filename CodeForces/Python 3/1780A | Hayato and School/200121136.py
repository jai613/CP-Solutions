for i in range(int(input())):
    n=int(input())
    s=[int(i) for i in input().split()]
    odd=even=0
    odd_ind=[]
    even_ind=[]
    for i in range(n):
        if s[i]%2:
            odd+=1
            odd_ind.append(i)
        else:
            even+=1
            even_ind.append(i)
    if not odd:
        print('NO')
    elif even==1 and odd==2:
        print('NO')
    else:
        print('YES')
        if odd>=3:
            print(odd_ind[0]+1,odd_ind[1]+1,odd_ind[2]+1)
        else:
            print(odd_ind[0]+1,even_ind[0]+1,even_ind[1]+1)