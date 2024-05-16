baguni = []
n,m = map(int,input().split())
for _ in range(1,n+1):
    baguni.append(_)

for a in range(m):
    i,j = map(int,input().split())
    swap_baguni = baguni[i-1:j]
    baguni[i-1:j] = swap_baguni[::-1]
print(' '.join(map(str,baguni)))

