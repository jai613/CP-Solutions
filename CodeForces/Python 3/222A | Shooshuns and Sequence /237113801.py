n,k=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
i=n-1
while a[-1]==a[i] and i>=0:
            i-=1
if i>=k-1:
            print(-1)
else:
            print(i+1)