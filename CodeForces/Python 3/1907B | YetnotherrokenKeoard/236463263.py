for _ in range(int(input())):
 
    s=input()
 
    su=list()
    sl=list()
 
    for i in range(len(s)):
 
        if s[i].isupper():
            if s[i]!='B':
                su.append((i,s[i]))
            else:
                if su:
                    su.pop()
        else:
            if s[i]!='b':
                sl.append((i,s[i]))
            else:
                if sl:
                    sl.pop()
    
    x=[i[1] for i in sorted(su+sl,key=lambda x:x[0])]
    print(''.join(x))