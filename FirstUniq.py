s=input().strip()
visited=set()
for i in range(len(s)):
    if s[i] not in visited:
        visited.add(s[i])
        if s.count(s[i])==1:
            print(i)
            quit()
            
print("-1")

# reduce running time :add in set and if not pres already check for first time 
# if pres in set no need to check bcoz there is no possib that the count is 1
# simply s.count(i) will give res but this red time complexity
        
