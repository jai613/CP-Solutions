for _ in range(int(input())):
 s=input()
 if ')(' in s:
  new='('*len(s)+')'*len(s)
  print('YES')
  print(new)
 
 elif '((' in s  or '))' in s:
  new='()'*len(s)
  print('YES')
  print(new)
 else:
  print('NO')