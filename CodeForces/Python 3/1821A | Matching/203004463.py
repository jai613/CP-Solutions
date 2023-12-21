for i in range(int(input())):
 n=input()
 if n[0]=='0':
  print(0)
 else:
  f=None
  val=0
  if n[0]=='?':
   f=True
   val+=9
  if f:
   print(val*10**(n.count('?')-1))
  else:
   print(10**(n.count('?')))