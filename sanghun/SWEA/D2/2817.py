
T = int(input())

def dfs(idx, current_sum):
  global count 

  # 가지치기: 이미 K를 초과한 경우 탐색 중단
  if current_sum > K:
    return 
  
  # 목표 K 에 도달한 경우 
  if current_sum == K:
    count += 1
    return
  
  # 모든 원소를 다 탐색한 경우 종료
  if idx == N:
    return

  # 1. 현재 원소 A[idx]를 포함하는 경우
  dfs(idx + 1, current_sum + A[idx])

  # 2. 현재 원소를 포함하지 않는 경우
  dfs(idx + 1, current_sum)


for tc in range(1, T+1):

  N, K = map(int, input().split())
  A = list(map(int, input().split()))
  count = 0
  # 개수 조합은 많아도 상관없다 
  # 따라서 이거는 그냥 왼쪽부터 순회하면서, 더해가면서 만들어지면 

  dfs(0, 0)

  print(f"#{tc} {count}")
