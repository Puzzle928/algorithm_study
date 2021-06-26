# 깊이우선탐색의 구조

#             a
#         b   c   d
#     e   f   g   h   i
# j   k   l  정답 n   o

# a 검사하고 b 검사하고 e 검사하고  j검사하고 k 검사하고 f 검사하고 l 검사하고 c 검사하고 g 하고 정답을 찾고 종료한다

# 스택을 활용하여 문제를 푼다

# 예시문제


stack = [[0,0]]
dest = [5,5]
maps = [[0,0,0,0,0,0],[1,0,1,1,1,0],[0,0,1,0,1,0],[0,1,1,0,0,0],[0,0,1,1,1,1],[1,0,0,0,0,0]]
hori = 6
verti = 6
while len(stack)>0:
    now = stack.pop()
    if now == dest:
        print(True) 
    x = now[1]
    y = now[0]
    if x - 1 > -1:
        if maps[y][x-1] == 0:
            stack.append([y,x-1])
            maps[y][x-1] = 2
    if x + 1 < hori:
        if maps[y][x+1] == 1:
            stack.append([y,x+1])
            maps[y][x+1] = 2
    if y - 1 > -1:
        if maps[y-1][x] == 1:
            stack.append([y-1,x])
            maps[y-1][x] = 2
    if y + 1 < verti:
        if maps[y+1][x] == 1:
            stack.append([y+1,x])
            maps[y+1][x] = 2
    print(False) 








