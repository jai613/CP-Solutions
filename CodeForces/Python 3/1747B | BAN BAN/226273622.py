t=int(input())
 
for _ in range(t):
    n=int(input())
    s='BAN'*n
    l=0
    r=len(s)-1
    sett=[]
    while l<=r:
        if s[r]=='N' and s[l]!='N':
            sett.append([l+1,r+1])
            r-=3
            l+=3
        else:
            l+=1
    print(len(sett))
    for i in sett:
        print(*i)