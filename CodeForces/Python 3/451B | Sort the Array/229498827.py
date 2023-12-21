n=int(input())
arr=[int(i) for i in input().split()]
i=0
f=None
c=0
while i<(n-1):
  start=i
  c=0
  while i<n-1 and arr[i]>arr[i+1]:
   c=1
   i+=1
  if c:
   arr[start:i+1]=arr[start:i+1][::-1]
   f=1
   for x in range(n-1):
    if arr[x]>arr[x+1]:
     f=0
     break
   break
  i+=1
if not c:
 print('yes')
 print(n,n)
elif f:
 print('yes')
 print(start+1,i+1)
else:
 print('no')