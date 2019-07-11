n=int(input("Enter the no of elements:"))
l=[]
for i in range(n):
    l.append(input())
a=[]
for i in l:
    if i not in a:
        a.append(i)
print(a)
