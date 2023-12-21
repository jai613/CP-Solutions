for _ in range(int(input())):
 
 n,k=[int(i) for i in input().split()]
 new=[]
 for i in range(n-k,n+1):
   new.append(i)
 
 for i in range(n-k-1,0,-1):
  new.append(i)
 
 print(*new)