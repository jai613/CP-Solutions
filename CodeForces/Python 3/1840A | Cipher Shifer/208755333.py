 
def solve():
    n=int(input())
    s=input()
    stack=[]
    ans=''
    for i in s:
        if stack and i==stack[-1]:
            ans+=stack.pop()
            continue
        if not stack:
            stack.append(i)
    print(ans)
 
 
testcases=int(input())
 
while testcases:
    solve()
    testcases-=1