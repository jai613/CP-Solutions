 
for x in range(int(input())):
 n=int(input())
 mk=[int(i) for i in input().split()]
 i=0
 maxi=0
 for j in range(len(mk)):
  sub=mk[i:j+1]
  if set(sub)=={0}:
   maxi=max(maxi,len(sub))
  else:
   i+=1
 print(maxi)