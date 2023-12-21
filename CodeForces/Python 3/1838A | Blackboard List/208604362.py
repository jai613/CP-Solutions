for i in range(int(input())):
    n=int(input())
    s=[int(i) for i in input().split()]
    s.sort()
    print(s[0] if s[0]<0 else s[-1])