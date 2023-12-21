n=int(input())
s=input()
 
L=s.count('L')
O=s.count('O')
 
i=0
left_L=0
left_O=0
right_L=L
right_O=O
 
while i<n:
    if s[i]=='L':
        left_L+=1
        right_L-=1
    else:
        left_O+=1
        right_O-=1
    if left_L!=right_L and left_O!=right_O:
        break
    i+=1
 
if (left_O or left_L) and (right_O or right_L):
    print(left_L+left_O)
else:
    print(-1)