import sys

a = list(sys.stdin.readline().strip())
b = list(sys.stdin.readline().strip())

# (len(a)+1) x (len(b)+1) 크기의 2차원 리스트로 초기화
LCS = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(max(map(max, LCS)))
