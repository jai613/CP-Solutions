for x in range(int(input())):
 n=int(input())
 s=[int(i) for i in input().split()]
 if n==2:
  print(s[0]*s[1])
  continue
 s.sort()
 maxi=0
 for i in range(len(s)-1):
  maxi=max(s[i]*s[i+1],maxi)
 print(maxi)