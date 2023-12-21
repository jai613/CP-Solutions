n=int(input())
arr=[int(i) for i in input().split()]
pos=neg=zero=0
op=0
for i in arr:
 if i<0:
   neg+=1
   op+=-1*i-1
 elif i>0:
   pos+=1
   op+=i-1
 else:
   zero+=1
if neg%2 and not zero:
 op+=2
elif zero:
 op+=zero
print(op)