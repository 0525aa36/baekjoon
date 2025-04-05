import sys
S = sys.stdin.readline().strip().split('-') 
A = []
for i in S: # 
    cnt = 0
    for j in i.split('+'): # + 요소들 더해줘
        cnt += int(j) 
    A.append(cnt) 

result = A[0]
for i in A[1:]:
    result -= i
print(result)
