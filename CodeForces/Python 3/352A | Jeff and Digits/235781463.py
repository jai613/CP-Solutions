n=int(input())
arr=[int(i) for i in input().split()]
z=arr.count(0)
f=arr.count(5)
if not z:
 print(-1)
else:
 if f<9:
  print(0)
 else:
  g=(f//9)*9*'5'+'0'*z
  print(g)