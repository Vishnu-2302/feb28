l=[]
l1=[]
l2=[]
l3=[]
x=input()
l=x.split()
for i in l:
	if i not in l1:
		l1.append(i)
		l2.append(l.count(i))
n=len(l1)
for i in range(n):
	if l2[i]==1:
		l3.append(l1[i])
print(l3)