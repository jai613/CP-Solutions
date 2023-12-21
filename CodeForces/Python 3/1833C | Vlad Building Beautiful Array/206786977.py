for i in range(int(input())):
 n=int(input())
 s=[int(i) for i in input().split()]
 odd=even=0
 mini=maxi=s[0]
 for i in s:
  mini=min(i,mini)
  maxi=max(i,maxi)
  if i%2:
   odd+=1
  else:
   even+=1
 if odd==n or even==n:
  print('YES')
 elif mini%2:
  print('YES')
 elif not mini%2 and not maxi%2:
  print('NO')
 elif mini%2 and not maxi%2:
  print('NO')
 elif maxi%2 and not mini%2:
  print('NO')
 else:
  print('YES')