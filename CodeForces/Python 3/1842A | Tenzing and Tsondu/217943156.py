for _ in range(int(input())):
 
 n,m=[int(i) for i in input().split()]
 tso=[int(i) for i in input().split()]
 tenz=[int(i) for i in input().split()]
 
 x=sum(tso)
 y=sum(tenz)
 if x==y:
  print('Draw')
 elif x>y:
  print('Tsondu')
 else:
  print('Tenzing')