a=int(input())
b=[]
for i in range(0,a):
	c=input()
	b.append(c) 
	e=[]
for i in zip(*b):
	if(i.count(i[0])==len(i)):
		e.append(i[0])
	else:
		break
print("".join(e))
