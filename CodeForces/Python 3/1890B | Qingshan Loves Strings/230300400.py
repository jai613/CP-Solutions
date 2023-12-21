def check(s):
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            return True
    return False
 
for _ in range(int(input())):
 
    n,m=[int(i) for i in input().split()]
    s=input()
    t=input()
    f=True
    for i in range(n-1):
        if s[i]==s[i+1]:
            #check if t has any adjacent
            if check(t):
                f=False
                break
            else:
                if t[0]==s[i] or t[-1]==s[i+1]:
                    f=False
                    break
    if f:
        print('Yes')
    else:
        print('No')
    