for i in range(int(input())):
 n=int(input())
 l=0
 c=0
 s=input()
 f=False
 for r in range(n):
  sub=s[l:r+1]
  if r==0:
   continue
  if sub.count('a')==sub.count('b'):
   f=True
   print(l+1,r+1)
   c+=1
  else:
   l+=1
 if not f:
  print(-1,-1)