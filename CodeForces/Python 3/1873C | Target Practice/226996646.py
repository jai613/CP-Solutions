Final=[[1,1,1,1,1,1,1,1,1,1],
       [1,2,2,2,2,2,2,2,2,1],
       [1,2,3,3,3,3,3,3,2,1],
       [1,2,3,4,4,4,4,3,2,1],
       [1,2,3,4,5,5,4,3,2,1]
        ]
Final=Final+Final[::-1]
for i in range(int(input())):
    X=[]
    for i in range(10):
        X.append(list(input()))
    ans=0
    for i in range(10):
        for j in range(10):
            if X[i][j]=="X":
                ans+=Final[i][j]
    print(ans)