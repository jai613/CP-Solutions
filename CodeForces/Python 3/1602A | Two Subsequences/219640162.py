for _ in range(int(input())):
 s=input()
 ind=0
 mini=s[0]
 for i in range(1,len(s)):
  if mini>s[i]:
   mini=s[i]
   ind=i
 print(mini,s[:ind]+s[ind+1:])