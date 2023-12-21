for _ in range(int(input())):
    s=input()
    if len(s)%2!=0:
        if len(set(s[:len(s)//2]))==1:
            print('NO')
        else:
            print('YES')
    else:
        if len(set(s[:len(s)//2]))==1:
            print('NO')
        else:
            print('YES')