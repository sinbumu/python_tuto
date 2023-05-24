def solution(targets):
    # 타겟 리스트가 비어있을 경우 0을 반환
    if not targets:
        return 0
    
    # 타겟을 x좌표를 기준으로 오름차순으로 정렬
    targets.sort(key=lambda x: x[0])  # 시작점을 기준으로 오름차순 정렬
    
    # 최소 요격 미사일 수를 나타내는 변수
    missile_count = 0
    
    # 이전 요격 미사일의 끝점을 저장하는 변수
    prev_end = float('-inf')
    
    # 타겟 리스트를 순회하며 요격 미사일 수 계산
    for target in targets:
        # 현재 타겟의 시작점이 이전 요격 미사일의 끝점보다 크다면
        # 새로운 요격 미사일이 필요하므로 미사일 수를 1 증가시키고
        # 이전 요격 미사일의 끝점을 현재 타겟의 끝점으로 갱신
        if target[0] > prev_end:
            missile_count += 1
            prev_end = target[1]
        # 현재 타겟의 시작점이 이전 요격 미사일의 끝점보다 작거나 같다면
        # 이전 요격 미사일의 끝점을 현재 타겟의 끝점과 비교하여 갱신
        else:
            prev_end = min(prev_end, target[1])
    
    return missile_count

targets = [[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]

result = solution(targets)
print(result)
