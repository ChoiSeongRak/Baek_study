import sys
time = int(sys.stdin.readline())
# a = 300sec b = 60sec c = 10sec
abc_time = [300, 60, 10]
count = 0
result = []

if time % 10 != 0:
    print(-1)
    
else:
    for i in abc_time:
        count = time // i
        result.append(count)
        time = time % i
        
    print(result[0],result[1],result[2])




