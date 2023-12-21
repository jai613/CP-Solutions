for i in range(int(input())):
    n=int(input())
    arr=[int(i) for i in input().split()]
    if len(set(arr))==1:
        print(0)
        continue
    if len(set(arr))>1 and 1 in set(arr):
        print(-1)
        continue
    p=min(arr)
    w=arr.index(p)
    inn=0
    get=[]
    while len(set(arr))!=1 or 1 in set(arr):
        for i in range(len(arr)):
            if arr[i]<p:
                p=arr[i]
                w=i
            else:
                if arr[i]!=p:
                    if not arr[i]%p:
                        arr[i]//=p
                        get.append([i+1,w+1])
                    else:
                        arr[i]=arr[i]//p+1
                        get.append([i+1,w+1])
    if 1 in set(arr): print(-1)
    else:
        print(len(get))         
        for i in get:
            if i[0]!=i[1]:
                print(*i)