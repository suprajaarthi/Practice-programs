# Replace Entire Row or Column which has 0

https://ide.geeksforgeeks.org/m38F9h3SVX 
    
    
n,m=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
x,y=[],[]    
for i in range(n):
    for j in range(m):
        if l[i][j]==0:
            x.append(i)
            y.append(j)
for i in range(n):
    for j in range(m):
        if i in x or j in y:
            print(0,end=" ")
        else:
            print(l[i][j],end=" ")
    print()     

IP

3 3
1 2 3 
4 5 0
7 0 9

OP 

1 0 0 
0 0 0 
0 0 0 
