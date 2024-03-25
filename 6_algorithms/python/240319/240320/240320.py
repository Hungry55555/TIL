# 1. 그래프를 코드로 표현
# - 인접 행렬
#  - - V x V 배열을 활용해서 표현
# - 갈수 없다면 0, 있다면 1(가중치)을 저장
# - 장점
#   - 노드간의 연결 정보를 한 방에 확인 가능
#   - 간선이 많을수록 유리
# - 단점
#   - 노드 수가 커지면 메모리가 낭비된다.
#       - 연결이 안된 것도 저장
#   -> s노드 수+ 메모리 제한 반드시 확인!

# 특징: 양방향 그래프는
#       중앙 우하단 대각선 기준으로 대칭됨

graph = [
    [0,1,0,1,0],    # 0 번은 1과 3으로 갈 수 있따는 의미
    [1,0,1,0,1], 
    [0,1,0,0,0],
    [1,0,0,0,1],
    [0,1,0,1,0],
]
# 인접 리스트
#   - V 개의 노드가 갈 수 있는 정보만 저장
# - 장점
#   - 메모리 사용량이 적다
#   - 탐색할 때 갈 수 있는 곳만ㅎ 확인하기 때문
#      시간적으로 효율
# - 단점
#   0 
graph = [
    [1,3],
    [0,2,4],
    [1],
    [0,4],
    [1,3],
]