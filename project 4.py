n=int(input())
l=[]
for i in range(0,n):
    lst=list(input().split())
    if lst[0]=="insert":
        l.insert(int(lst[1]),int(lst[2]))
    if lst[0]=="print":
        print(l)
    if lst[0]=="remove":
        l.remove(int(lst[1]))
    if lst[0]=="append":
        l.append(int(lst[1]))
    if lst[0]=="sort":
        l.sort()
    if lst[0]=="pop":
        l.pop(len(l)-1)
    if lst[0]=="reverse":
        l.reverse()
        
        
        
