h,m = map(int, input().split())
c = int(input())
def calc(h,m,c):
    h += c // 60
    m += c % 60
    
    if m >= 60:
        h += 1
        m -= 60
        
    if h >= 24:
        h -= 24
    print(h,m)
calc(h,m,c)
    
    
