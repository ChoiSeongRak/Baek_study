H, M = map(int,input().split())
def calc(H,M):
    if M < 45:
        if H == 0:
            H = 23
            M += 60
        else:
            H -= 1
            M += 60
    print(H, M-45)
calc(H,M)