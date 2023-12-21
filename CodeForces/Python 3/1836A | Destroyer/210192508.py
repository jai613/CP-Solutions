for _ in range(int(input())):
 n=int(input())
 x=[int(i) for i in input().split()]
 x.sort()
 f=True
 if x[0]==0:
  for i in range(n-1):
   if x[i]!=x[i+1] and (x.count(x[i])<x.count(x[i+1]) or (x[i+1]-x[i]!=0 and x[i+1]-x[i]!=1)):
    f=False
    break
  if f:
    print('YES')
  else:
    print('NO')
 else:
   print('NO')