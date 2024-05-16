n = int(input())
score = list(map(int,input().split()))
m = max(score)
total = sum(score)

print(total * 100 / m / n)


