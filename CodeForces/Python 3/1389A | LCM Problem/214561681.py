import math
for _ in range(int(input())):
 
 arr=[int(i) for i in input().split()]
 a,b=arr[0],arr[1]
 if b-a<a:
  print(-1,-1)
 else:
  print(a,2*a)