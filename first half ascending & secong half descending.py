num = int(input())
array = list(map(int,input().split()))
num = len(array)
array.sort()
for i in range(num//2):
	print(array[i],end=" ")
for j in range(num-1,num//2-1,-1):
	print(array[j],end=" ")


#output

8

0 1 2 3 9 8 7 6 
