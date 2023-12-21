for _ in range(int(input())):
 n,k=[int(i) for i in input().split()]
 s=input()
 a=0
 x=n-1
 while x>=0:
  if s[x]=='B':
   a+=1
   x-=k
  else:
   x-=1
 print(a)