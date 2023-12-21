t=int(input())
 
while t:
  
  n=int(input())
  p=[int(i) for i in input().split()]
  x=None
  for i in range(n):
   if p[i]!=i+1:
    x=p.index(i+1)
    break
  if x:
   p[i:x+1]=p[i:x+1][::-1]
  print(*p)
  t-=1
  