list = []
for _ in (range(10)):
    num = int(input())
    if num%42 not in list:
            list.append(num%42)
print(len(list))