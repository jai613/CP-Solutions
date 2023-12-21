for _ in range(int(input())):
 n=int(input())
 s=[int(i) for i in input().split()]
 s.sort()
 ans=0
 l=0
 r=n-1
 while l<=r:
  ans+=(s[r]-s[l])
  l+=1
  r-=1
 print(ans)