n,k=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
x=set()
f=False
if n==2:
    if len(set(a))==1:
        print(0)
    else:
        if k==1:
            print(-1)
        else:
            print(1)
elif n==1 or len(set(a))==1:
    print(0)
 
else:
    ans=0
    for i in range(k-1,n):
        if len(x)>1:
            f=True
            break
        x.add(a[i])
        ans=a[i]
    if len(x)>1:
        f=True
    if f is False:
        cur=k-1
        while a[cur]==ans:
            cur-=1
        print(cur+1)
    else:
        print(-1)
 
            
            
 
 
 
 
 
 
 
 
        
        