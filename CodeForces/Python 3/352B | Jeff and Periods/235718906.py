n=int(input())
arr=[int(i) for i in input().split()]
 
dic={}
 
for i in range(n):
 if arr[i] not in dic:
  dic[arr[i]]=[]
 dic[arr[i]].append(i)
ans=[]
for j in dic:
 if len(dic[j])==1:
  ans.append([j,0])
 elif len(dic[j])==2:
  ans.append([j,dic[j][1]-dic[j][0]])
 else:
  c=1
  dif=dic[j]
  anss=-1
  for i in range(len(dif)-1):
   if anss==-1:
    anss=dif[i+1]-dif[i]
   else:
    if anss!=dif[i+1]-dif[i]:
     c=0
     break
  if c:
   ans.append([j,dic[j][1]-dic[j][0]])
ans=sorted(ans,key=lambda x:x[0])
print(len(ans)) 
for i in ans:
 print(*i)