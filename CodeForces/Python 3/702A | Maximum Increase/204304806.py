n=int(input())
s=[int(i) for i in input().split()]
l=0
maxi=0
liss=[]
ll=0
for r in range(len(s)-1):
 if s[r]>=s[r+1]:
  maxi=max(maxi,ll)
  ll=0
 else:
  ll+=1
if ll:
 maxi=max(maxi,ll)
print(maxi+1)