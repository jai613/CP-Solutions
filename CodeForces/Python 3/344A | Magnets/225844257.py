A=list()
for _ in range(int(input())):
    A.append(input())
ans=0
i=0
while i+1<len(A):
    if A[i][0]==A[i+1][0]:
        while i+1<len(A) and A[i][0]==A[i+1][0]:
            i+=1
    else:
        ans+=1
        i+=1
print(ans+1)