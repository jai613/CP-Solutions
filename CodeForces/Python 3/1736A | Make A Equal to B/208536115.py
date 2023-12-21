 
for _ in range(int(input())):
 n=int(input())
 h=[int(ii) for ii in input().split()]
 i=[int(ii) for ii in input().split()]
 if h.count(1)==i.count(1) and h.count(0)==i.count(0):
  if h==i:
   print(0)
  else:
   print(1)
 else:
  h1=h.count(1)
  i1=i.count(1)
  diff=abs(h1-i1)
  f=0
  ans=0
  if h1<i1:
   for k in range(n):
    if h.count(1)==i.count(1):
     f=1
     break
    if h[k]==0 and h[k]!=i[k]:
     h[k]=1
     ans+=1
  else:
   for k in range(n):
    if h.count(1)==i.count(1):
     f=1
     break
    if h[k]==1 and h[k]!=i[k]:
     h[k]=0
     ans+=1
  if h==i:
    print(ans)
  else:
    print(ans+1)