n=int(input())
dic={}
for _ in range(n):
 h,m=[int(i) for i in input().split()]
 calc=h*60+m
 if calc not in dic:
  dic[calc]=1
 else:
  dic[calc]+=1
ans=1
for i in dic:
 ans=max(ans,dic[i])
 
print(ans)