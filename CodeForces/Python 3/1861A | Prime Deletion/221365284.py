for _ in range(int(input())):
    n=input()
    if len(n)>2:
        if n[0]=='1':
            print(13)
        elif n[0]=='2':
            print(23)
        elif n[0]=='3':
            print(31)
        elif n[0]=='4':
            print(41)
        elif n[0]=='5':
            print(53)
        elif n[0]=='6':
            print(67)
        elif n[0]=='7':
            print(71)
        elif n[0]=='8':
            print(89)
        else:
            print(97)
    else:
        print(-1)