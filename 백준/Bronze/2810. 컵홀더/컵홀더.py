n = int(input())
seat = input().upper()
couple = seat.count('LL')

if couple == 0:
    print(n)
elif couple == 1:
    print(n)
else:
    print(n - couple + 1)