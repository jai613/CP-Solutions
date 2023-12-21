for i in range(int(input())):
    s=[int(i) for i in input().split()]
    n,k=s[0],s[1]
    print(f'1\n{n}' if n%k else f'2\n{n-1} 1')