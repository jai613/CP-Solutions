def solve():
    st=input()
    w=len(set(st))
    m=list(set(st))
    if w==1: print(-1)
    elif w==2:
        if st.count(m[0])==2 or st.count(m[1])==2:print(2+2)
        else: print(3+3)
    else: print(4)
 
t=int(input())
while t:
    solve()
    t-=1