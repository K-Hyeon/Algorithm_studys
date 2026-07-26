totalCaseNumber = int(input())
for _ in range(totalCaseNumber):
    testCaseNumber = int(input())
    scoreDistribution = list(map(int, input().split()))
   
    #성적 counting할 배열 성적은 0점이상 100점 이하 
    countingDist = [0]*101
    
    #계수 정렬의 1단계
    for score in scoreDistribution:
        countingDist[score] += 1
    
    #최빈수 찾기
    max_frequency = -1
    mode_score = -1
    
    for score in range(101):
        if countingDist[score] >= max_frequency:
            max_frequency = countingDist[score]
            mode_score = score
            
    print(f"#{testCaseNumber} {mode_score}")
    
    # 이 문제를 선택한 이유 
    # 최빈수를 찾는 것이 목표가 아니라 정렬이 목표였다면 counting_sort(계수 정렬)의 장점을 확인 할 수 있었을 문제였다고 생각합니다.
    # 