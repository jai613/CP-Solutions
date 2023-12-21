n=int(input())
new=''
if n==9:
    print(9)
else:
    o=str(n)
    for i in range(len(o)):
        if i==0 and o[i]=='9':
            new+='9'
            continue
        if (i!=0 and o[i]=='9') or 9-int(o[i])<int(o[i]):
            new+=str(9-int(o[i]))
        else:
            new+=o[i]
    print(new)