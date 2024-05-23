n,k = map(int,input().split())
coin = []
count = 0
for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)

for i in coin:
    if k >= i:
        count += k//i
        k = k % i
        
print(count)
