saram = int(input())
list = sorted(list(map(int,input().split())))
time = 0
t_time = 0
for i in range(saram):
    time += list[i]
    t_time += time
print(t_time)
    


