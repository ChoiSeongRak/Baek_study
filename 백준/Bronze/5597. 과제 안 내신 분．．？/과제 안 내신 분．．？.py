student = [a for a in range(1,31)]
for _ in range(28):
    good = int(input())
    student.remove(good)
print(min(student))
print(max(student))