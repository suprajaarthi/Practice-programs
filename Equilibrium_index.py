Sum of elements in Left == Sum of elem in Rght
https://ide.geeksforgeeks.org/v3rGdL6b7a

l=list(map(int,input().split()))
ls,rs=0,0
n=len(l)
for i in range(n):
    ls,rs=0,0
    for j in range(i):
        ls+=l[j]
        
    for j in range(i+1,n):
        rs+=l[j]
        
    if(ls==rs):
        print(i)
print("-1")
