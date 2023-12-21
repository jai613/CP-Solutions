n=int(input())
val=int(((1+8*n)**0.5 -1)//2)
get=val*(val+1)//2
val1=int(((1+8*get)**0.5 -1)//2)
if n==get:
 print(val)
else:
 print(n-get)