for i in range(int(input())):
 n=int(input())
 k=sum([int(i) for i in input().split()])
 if k==n:
  print(0)
 else: 
  if k<=n:
   print(1)
  else:
   print(k-n)