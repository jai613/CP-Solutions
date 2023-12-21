for _ in range(int(input())):
 a,b,c=[int(i) for i in input().split()]
 if a+b==c or a==b+c or c+a==b:
  print('YES')
 elif a==b==c:
  if a%2==0:
   print('YES')
  else:
   print('NO')
 elif a==b:
  if c%2:
   print('NO')
  else:
   print('YES')
 elif a==c:
  if b%2:
   print('NO')
  else:
   print('YES')
 elif c==b:
  if a%2:
   print('NO')
  else:
   print('YES')
 else:
  print('NO')
 