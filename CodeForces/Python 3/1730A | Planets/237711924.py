for _ in range(int(input())):
    n,c=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    ans=0
    dic={i:a.count(i) for i in a}
    for i in dic:
        ans+=min(c,dic[i])
    print(ans)