import math
for _ in range(int(input())):
 n=int(input())
 k=int(math.log(n,2))+1
 act_sum=n*(n+1)//2
 rem_=(2**k-1)*2
 print(act_sum-rem_)
 