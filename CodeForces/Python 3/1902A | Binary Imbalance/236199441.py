for _ in range(int(input())):
 n=int(input())
 s=input()
 flag=False
 c=0
 if n==1:
  if s=='1':
   print('NO')
  else:
   print('YES')
 else:
  for i in range(n-1):
   if s[i]=='0':
    c+=1
   if s[i]!=s[i+1]:
    flag=True
    break
  if flag or (c==n-1):
   print('YES')
  else:
   print('NO')