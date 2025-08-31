N, M = map(int, input().split())

array = [0]*N
for _ in range(M):
    i,j,k = map(int, input().split())
    array[i-1:j] = [k]*(j-i+1)
print(' '.join(map(str, array)))