for _ in range(int(input())):
    s=input()
    if len(set(s[:len(s)//2]))==1:
        print('NO')
    else:
        print('YES')