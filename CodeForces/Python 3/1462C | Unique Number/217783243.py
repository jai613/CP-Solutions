for _ in range(int(input())):
 
 n=int(input())
 if n>45:
  print(-1)
 else:
  x=9
  s=0
  ans=''
  while (n-s)-x>0:
   ans+=str(x)
   s+=x
   x-=1
  ans+=str(n-s)
  print(ans[::-1])