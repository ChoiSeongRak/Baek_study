A,B = map(int,(input().split(' ')))


def calc(A,B):

    if A > B:
        print('>')
    elif A < B:
        print('<')
    else:
        print('==')
    
calc(A,B)