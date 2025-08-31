max_val = 0
array = []
for i in range(9):
    N = int(input())
    array.append(N)
    if N > max_val:
        max_val = N
print(max_val)
for i in range(9):
    if max_val == array[i]:
        print(i+1)