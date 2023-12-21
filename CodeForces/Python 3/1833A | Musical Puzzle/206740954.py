for i in range(int(input())):
    n=int(input())
    s=input()
    k=set()
    for i in range(n):
        if i+2<=n:
            k.add(s[i:i+2])
    print(len(k))