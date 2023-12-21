for _ in range(int(input())):
 
    n=int(input())
    arr=[int(i) for i in input().split()]
    g=max(arr)
    if len(set(arr))==1:
        print(0)
        continue
    if arr[0]==g:
        print(g)
    else:
        new=sorted(arr)
        c=1
        maxi=0
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                maxi=max(maxi,arr[i])
        print(maxi)