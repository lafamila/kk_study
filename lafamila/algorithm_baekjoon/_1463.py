import sys
N = int(sys.stdin.readline().strip())
MAP = {1: 0, 2: 1}
for num in range(3, N+1, 1):
    candidates = [num-1]
    if num%3 == 0:
        candidates.append(num//3)
    if num%2 == 0:
        candidates.append(num//2)
    MAP[num] = min(map(lambda x: MAP[x], candidates)) + 1
print(MAP[N])
