for i in range(int(input())):
 k=input()
 n=len(k)
 if len(set(k))==1:
  print(-1)
 else:
  print(n-1)