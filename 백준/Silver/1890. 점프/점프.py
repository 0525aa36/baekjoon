import sys

N = int(sys.stdin.readline())
게임판 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [[-1]*N for _ in range(N)]

def 점프(i, j):
    way = 0  #경로수 세는 것이니 그냥 way 늘려주면 됨
    jump = 게임판[i][j] 

    #도착성공하면 1
    if i == N-1 and j == N-1:
        return 1
    
    #종착점 0
    if 게임판[i][j] == 0:
        return 0

    #이미 지나갔을때
    if visited[i][j] != -1:
        return visited[i][j]

    #오른쪽 점프
    if j + jump < N:
        #점프한데서 또 쩜프
        way += 점프(i, j + jump)

    #아래 점프
    if i + jump < N:
        #점프한데서 또 쩜프
        way += 점프(i + jump, j)

    #중복 못하게 경로에 넣어
    visited[i][j] = way
    return way

print(점프(0, 0))
