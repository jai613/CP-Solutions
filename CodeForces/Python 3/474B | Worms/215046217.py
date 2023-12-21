n=int(input())
arr=[int(i) for i in input().split()]
x=int(input())
that=[int(i) for i in input().split()]
 
import bisect
 
 
pre=[0]*(n)
pre[0]=arr[0]
for i in range(1,n):
    pre[i]=pre[i-1]+arr[i]
for i in that:
    print(bisect.bisect_left(pre,i)+1)