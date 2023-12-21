for _ in range(int(input())):
 l,r=[int(i) for i in input().split()]
 print(min(r-l,r%(r//2+1)))