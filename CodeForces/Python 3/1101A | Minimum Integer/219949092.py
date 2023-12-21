for _ in range(int(input())):
 
    l,r,d=[int(i) for i in input().split()]
    if (d<l and d<r) or (d>l and d>r):
        print(d)
    elif l==r==d:
        print(2*d)
    elif l==d or r==d:
        if r==d:
            print(2*d)
        else:
            print((r//d)*d+d)
    else:
        print((r//d)*d+d)