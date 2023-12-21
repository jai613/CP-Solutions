for _ in range(int(input())):
 m,n=[int(i) for i in input().split()]
 arr=[int(i) for i in input().split()]
 b=[int(i) for i in input().split()]
 for i in range(len(b)):
  x=arr.index(min(arr))
  arr[x]=b[i]
 print(sum(arr))