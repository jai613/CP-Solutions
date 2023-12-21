 
for _ in range(int(input())):
 s=input()
 i=0
 a=0
 while len(set(s))!=1 and i+1<len(s):
  if s[i]!=s[i+1]:
   s=s[:i]+s[i+2:]
   a+=1
   if len(s)==1:
    break
   i=0
  else:
   i+=1
   
 if a%2==0:
  print('NET')
 else:
  print('DA')