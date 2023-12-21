for _ in range(int(input())):
 
    n=int(input())
    s=input()
    dic={i:s.count(i) for i in s}
    ans=0
    for i in dic:
        if dic[i]>=(26-90+ord(i)):
            ans+=1
    print(ans)