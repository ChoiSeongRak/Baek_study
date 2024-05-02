N = int(input())
def calc(N):
    s = 0
    if N == 3 or N == 5:
        print('1')
    elif N == 4:
        print('-1')
    else:
        while N >= 0:
            if N % 5 == 0:
                s += N//5
                print(s)
                break
            N -= 3
            s += 1
            
            if N < 0:
                print(-1)
calc(N)