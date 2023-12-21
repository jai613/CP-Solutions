import math
for _ in range(int(input())):
 arr=[int(i) for i in input().split()]
 n=arr[0]
 if n%2==0:
  k=n//2
  if k%2==0:
   print(k,k//2,k//2)
  else:
   print(2,(n-2)//2,(n-2)//2)
 else:
  print(1,n//2,n//2)