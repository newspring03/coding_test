N = int(input())
array = list(map(int, input().split()))
max_num = -1000000
min_num = 1000000

for i in range(N):
    if array[i] < min_num:
        min_num = array[i]
print(min_num, end=' ')
for i in range(N):
    if array[i] > max_num:
        max_num = array[i]
print(max_num)