# 1. Brute Force(완전 탐색)
# 컴퓨터의 빠른 계산 성능을 활용하여 가능한 모든 경우의 수를 탐색하는 효울성 관점에서 최악의 방법
'''
구현방법

반복문

뒤집혀 있는 트럼프 카드 8장 

하트 8이 알고 싶다

아무 카드나 뒤집어본다 

내가 원하는 카드를 찾기 위해서는 카드가 많아 질때마다 확률이 낮아진다.

그래서 첫번쨰 부터 순서대로 찾는다

다 뒤집어보다보면 찾는 수가 나온다 종료..
'''
# from typing_extensions import Unpack


# def solution(trump):
#     for i in range(len(trump)): # 카드의 수만큼 반복 뒤집기
#         if trump[i] == 8: # 뒤집다가 카드가 8이 나왔다면
#             return i  # 그위치 값을 리턴한다.



# 재귀함수

# -동적 계획법


# - 백트래킹

# # - 탐욕법

# def solution(trump, loc):
#     if trump[loc] == 8:
#         return loc
#     else:
#         return solution(trump, loc+1)

'''
이분 탐색

updown 게임

1 ~~ 1000 기회는 8번

500 Up
750  -> 확률을 줄여간다
'''


def solition(trump):
    left = 0
    right = len(trump)-1
    while(left <= right):
        mid = (left + right) // 2
        if trump[mid] == 8:
            return mid
        elif trump[mid] < 8:
            left = mid + 1
        elif trump[mid] > 8:
            left = mid - 1
    return mid


# 모의고사
answer = list(input())
p1 = [1,2,3,4,5,1,2,3,4,5]

p2 = [2,1,2,3,2,4,2,5,2,1,2,3,2,4,2,5]

p3 = [3,3,1,1,2,2,4,4,5,5,3,3,1,1,2,2,4,4,5,5]

giveup = [p1, p2, p3]

score = [0,0,0]

winner = []


for x,i in enumerate(p1):
    for y,j in enumerate(answer):
        if x == y and i == j:
            score[0]+= 1

# for x,i in enumerate(p2):
#     for y,j in enumerate(answer):
#         if x == y and i == j:
#             score[1]+= 1

# for x,i in enumerate(p3):
#     for y,j in enumerate(answer):
#         if x == y and i == j:
#             score[2]+= 1

# for i,s in enumerate(score):
#     if s == max(score):
#         winner.append(i+1)
    
print(winner)

# 소수찾기


















#숫자카드2

# card = int(input())

# n = input().split()

# answer = int(input())

# k = input().split()

# g = [0] * answer

# for i in n:
#     for x,j in enumerate(k):
#         if i == j:
#             g[x] += 1
# for x in g:
#     print(x, end = ' ')







