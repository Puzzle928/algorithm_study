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
from typing_extensions import Unpack


def solution(trump):
    for i in range(len(trump)): # 카드의 수만큼 반복 뒤집기
        if trump[i] == 8: # 뒤집다가 카드가 8이 나왔다면
            return i  # 그위치 값을 리턴한다.



# 재귀함수

# -동적 계획법


# - 백트래킹

# - 탐욕법

def solution(trump, loc):
    if trump[loc] == 8:
        return loc
    else:
        return solution(trump, loc+1)

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