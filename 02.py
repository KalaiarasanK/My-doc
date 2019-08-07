from itertools import combinations
A,B=map(int,input().split())
a=len(str(A))
b=list(combinations(str(A),a-B))
b=sorted(b)
print(*b[0],sep="")
