n=int(input())
s=[int(i) for i in input().split()]
maxi=0
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