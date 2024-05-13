import sys

n = int(sys.stdin.readline())
list = list(map(int,sys.stdin.readline().split(' ')))
find = int(sys.stdin.readline())
count = 0

for i in list:
    if i == find:
        count += 1
print(count)
    