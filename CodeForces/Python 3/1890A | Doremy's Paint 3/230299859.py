for _ in range(int(input())):
 
    n=int(input())
    arr=[int(i) for i in input().split()]
    dic={}
    for i in arr:
        if i not in dic:
            dic[i]=0
        dic[i]+=1
 
    if len(dic)>2:
        print('NO')
    else:
        if len(dic)==1:
            print('YES')
        else:
            new=[]
            for i in dic:
                new.append(dic[i])
            if abs(new[0]-new[1])>1:
                print('NO')
            else:
                print('YES')