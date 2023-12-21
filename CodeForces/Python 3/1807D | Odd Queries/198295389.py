for i in range(int(input())):
 s=[int(i) for i in input().split()]
 t=[int(i) for i in input().split()]
 n,q=s[0],s[1]
 queries=[]
 for i in range(q):
  queries.append([int(i) for i in input().split()])
 pre=[0]*n
 pre[0]=t[0]
 for i in range(1,n):
  pre[i]=pre[i-1]+t[i]
 suum=pre[-1]
 for i in queries:
  l=i[0]
  r=i[1]
  k=i[2]
  if l>=2:
   rang=pre[r-1]-pre[l-2]
  else:
   rang=pre[r-1]  
  repl=(r-l+1)*k
  ans=suum+repl-rang
  if ans%2:
   print('YES')
  else:
   print('NO')