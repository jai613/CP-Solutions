n,x=[int(i) for i in input().split()]
lr=[]
for _ in range(n):
 lr.append([int(i) for i in input().split()])
 
start=1
ans=0
for i in lr:
 a,b=i[0],i[1]
 if a!=start:
  start+=((a-start)//x)*x
 ans+=(b-start+1)
 start=b+1
print(ans)
 
 