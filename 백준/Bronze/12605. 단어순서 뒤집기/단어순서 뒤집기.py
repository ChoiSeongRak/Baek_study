n = int(input())
for i in range(n):
    case = str(input()).split(" ")
    re_cases = case[::-1]
    print(f'Case #{i+1}: {" ".join(re_cases)}')