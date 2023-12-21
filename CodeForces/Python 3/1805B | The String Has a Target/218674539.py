for _ in range(int(input())):
 
    n=int(input())
    s=input()
    cur=s[0]
    g=0
    for i in range(1,n):
        if cur>=s[i]:
            g=i
            cur=s[i]
    if cur<=s[0]:
        s=s[g]+s[:g]+s[g+1:]
        print(s)
    else:
        print(s)