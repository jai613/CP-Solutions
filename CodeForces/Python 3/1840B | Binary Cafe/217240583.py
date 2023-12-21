import math
for _ in range(int(input())):
 n,k=[int(i) for i in input().split()]
 x=math.log(n,2)
 if x<k:
  print(n+1)
 else:
  print(2**k)