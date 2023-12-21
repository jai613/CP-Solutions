 
s=[int(ii) for ii in input().split()]
n,k=s[0],s[1]
if n==k:
 print(-1)
elif n-k==1:
 for i in range(1,n+1):
  print(i,end=' ')
 print()
elif n-k==2:
 print(n,end=' ')
 for i in range(2,n):
  print(i,end=' ')
 print(1)
 print()
else:
 kk=[i for i in range(1,n+1)]
 for x in range(1,n):
  if k==0:
   break
  k-=1
 while x+1<n:
  kk[x],kk[x+1]=kk[x+1],kk[x]
  x+=2
 if x==n-1:
  kk[0],kk[n-1]=kk[n-1],kk[0]
 print(*kk)