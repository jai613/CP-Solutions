for i in range(int(input())):
 n=int(input())
 arr=[int(x) for x in input().split()]
 arr.sort()
 print(arr[-1]+arr[-2]-arr[0]-arr[1])