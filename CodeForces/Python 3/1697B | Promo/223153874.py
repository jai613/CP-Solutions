n,q=[int(i) for i in input().split()]
arr=[int(i) for i in input().split()]
a=[]
arr.sort(reverse=True)
pre=[arr[0]]
for i in range(1,n):
 pre.append(pre[-1]+arr[i])
for _ in range(q):
 x,y=[int(i) for i in input().split()]
 if x==1 or y==0 or x==y:
  s=pre[x-1]
 else:
  s=pre[x-1]-pre[x-y-1]
 a.append(s)
for i in a:
 print(i)