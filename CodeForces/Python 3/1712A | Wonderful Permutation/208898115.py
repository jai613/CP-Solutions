for i in range(int(input())):
 a=[int(i) for i in input().split()]
 n,k=a[0],a[1]
 s=[int(i) for i in input().split()]
 ans=0
 for i in range(k):
  ans+=1 if s[i]>k else 0
 print(ans)