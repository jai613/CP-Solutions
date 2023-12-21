n=int(input())
arr=[int(i) for i in input().split()]
s1=list()
s2=list()
dic={}
for i in arr:
 if i not in dic:
  dic[i]=1
 else:
  dic[i]+=1
ok=1
f=False
for i in dic:
 if dic[i]>2:
  f=True
  break
 elif dic[i]==2:
  s1.append(i)
  s2.append(i)
 else:
  if ok==2:
   ok=1
   s2.append(i)
  else:
   ok=2
   s1.append(i)
if f:
 print('NO')
else:
 
 s1.sort()
 s2.sort(reverse=True)
 print('YES')
 print(len(s1))
 print(*s1)
 print(len(s2))
 print(*s2)