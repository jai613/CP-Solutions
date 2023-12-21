for _ in range(int(input())):
 
 n=int(input())
 if n==1:
  print(1)
 elif n%2:
  print(-1)
 else:
  i=1
  while i+1<=n:
   print(i+1,end=' ')
   print(i,end=' ')
   i+=2
  print()