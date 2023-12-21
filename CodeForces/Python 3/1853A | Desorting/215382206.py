import math
 
for _ in range(int(input())):
 
    n=int(input())
    arr=[int(i) for i in input().split()]
    if sorted(arr)!=arr:
        print(0)
        continue
    if len(set(arr))==1:
        print(1)
        continue
    else:
        k=float('inf')
        for i in range(n-1):
            k=min(abs(arr[i+1]-arr[i]),k)
        print(math.ceil(k//2)+1)  