for _ in range(int(input())):
 
 n=int(input())
 arr=[int(i) for i in input().split()]
 f=1
 for i in range(n):
  if arr[i]!=i+1:
   f=0
   break
 if f:
  print(0)
 elif 1==arr[0] or n==arr[-1]:
  print(1)
 elif 1==arr[-1] and n==arr[0]:
  print(3)
 else:  
  print(2)