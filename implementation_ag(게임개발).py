# N, M을 공백으로 입력받기

n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화

d = [[0] * m for _ in range(n)]

#현재 캐릭터의 X좌표, Y좌표, 방향을 입력받기

x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

#전체 맵 정보를 입력받기 #N값만큼 반복하여 입력하는 방법 // 아무것도 없는 빈 리스트를 작성하고 거기다가 append 함수를 이용하여 맵을 넣는 방법

array = []
for i in range(n):
    array.append(list(map(int, input().split())))


# 북, 동, 남, 서 방향 정의

dx = [-1, 0, 1, 0] #수직으로 이동방향
dy = [0, -1, 0, 1] #수평으로 이동방향

# 왼족으로 회전 // 북쪽이 0, 동쪽이 1, 이고 서쪽이 3이기 때문에 북쪽에서 왼쪽으로 돌때 즉 0 → -1(3)으로 간다는 것을 함수로 표현 함수밖에서도 작동할 수 있도록 글로벌 변수 사용

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작

count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 이경우 방향을 한번 만 심어주면 한칸만 이동 예를들어 서쪽(3)이라고 했을때 나머지 북(0), 동(1), 남(2)은 더해지지 않는다.

    #  회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0: # d = 좌표와 이동을 위한 리스트 // # array 는 입력 받은 좌표 둘을 대조하여 array 상에 또는 d 상에 이동을 나타낼 수 있다, 즉 한곳에 좌표의 이동과 데이터 변화를 기록하는 것이 아님
        d[nx][ny] = 1 # 지나가버리면 1로 바꾸어버리는 것
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    # 만약 4방향 모두 갈 수 없는 경우 → 한칸 뒤로 이동하거나, 거기서 멈추거나를 나타낼때는 if 갈수없다면, if 뒤로가는곳이 0이라 갈수 있다면, 그렇지 못하다면 Stop

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기 // 바라보는 방향을 유지하고 한 칸 뒤로간다는 것은 입력받은 direction의 반대방향 즉 그만큼을 빼주는것이 뒤로 가는것
        if array[nx][ny] == 0:
            x = nx
            y = ny

    # 뒤가 바다로 막혀 있는경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)