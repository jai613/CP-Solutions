for _ in range(int(input())):
 
    n=int(input())
    s=input()
    if '...' in s:
        print(2)
    else:
        print(s.count('.'))