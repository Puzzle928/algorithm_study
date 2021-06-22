# 1.두 정수 사이의 합
# 두 정수 a,b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수,solution을 완성하세요.
# 예를 들어 a = 3. b = 5인 경우, 3+4+5 = 12 이므로 12를 리턴합니다.

# a = int(input())
# b = int(input())

# answer = 0
# for i in range(min(a,b),max(a,b)+1):
#     answer += i


# print(answer)


# 2. 수박수박수?
# 길이가 n 수박수박수박을 반복하게끔하라
# n 이 4 이면 수박수박
# n 이 3 이면 수박수 리턴하게끔하라..


# n = int(input())

# watermellon = []

# for i in range(1,n+1):
#     if i % 2 != 0:
#         watermellon.append("수")
#     else: # 짝수
#         watermellon.append("박")
# # [수,박,수]
# for e in watermellon:
#     print(e, end ="")
    # 수박수

# 서울에서 김서방 찾기

# String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요.
# seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

# seoul = ["Jane", "Kim"]
# for i,j in enumerate(seoul):
#     if j == "Kim":
#         print(j ,"의 위치는", i , "입니다")


# 약수의 합

# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

# n = int(input())
# g = []

# for i in range(1,n+1):
#     if n % i == 0:
#         g.append(i)
#         g.append(n/i)

# g = set(g)
# print(sum(g))


# 문자열 내 p와 y의 개수

# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요.
#  'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

# 예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

# s = "pPoooyY" # 문자열입력
# p_count = 0
# y_count = 0
# # print(s[1])
# for i in s:
#     if i == 'p' or i == 'P':
#         p_count += 1
#     if i == 'y' or i == 'Y':
#         y_count += 1
# if p_count == y_count:
#     print(True)
# else:
#     print(False)




# 같은 숫자 는 싫어!!
# 배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 예를 들면,

# arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
# arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
# 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.


# arr = [1, 1, 3, 3, 0, 1, 1]
# arr2 = [4, 4, 4, 3, 3]
# nosame = []
# nosame.append(arr[0])
# for i in range(len(arr)):    
#     if arr[i] != nosame[len(nosame)-1]:
#         nosame.append(arr[i])
# print(nosame)



# 가운데 글자 가져오기
# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 
# 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

# s = "abcde"

# if len(s) % 2 == 0:
#     print(s[len(s)//2] , s[len(s)//2 + 1])
# if len(s) % 2 != 0:
#     print(s[len(s)//2])




# x만큼 간격이 있는 n개의 숫자

# 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

# x = int(input())
# n = int(input())
# answer = []
# for i in range(1,n+1):
#     answer.append(x*i)
# print(answer)




# 직사각형 별찍기
# 이 문제에는 표준 입력으로 두 개의 정수 n 과 m 이 주어집니다.
# 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m 인 직사각형 형태를 출력해보세요.

# n, m = map(int,input().split())
# w = "*" * n
# d = [w] * m

# for i in d:
#     print(i)




# 평균 구하기
# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

# arr = [1,2,3,4]

# avg = sum(arr) / len(arr)

# print(avg)





# 행렬의 덧셈              ---------------------------------------------------------------미완---------------------------------

# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
#  2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

# arr1 = [[1,2],[2,3]]

# arr2 = [[3,4],[5,6]]

# return1 = [[0]* len(arr1[0])] * len(arr1)
# print(return1) = [[0,0],[0,0]]       # arr에 맞게 틀을 만들어냄


# p = int(len(arr1[0]))  # 행렬안에 있는 갯수!!

# for i in range(p):
#     for j in range(p):
#         return1[i][j] = arr1[i][j] + arr2[i][j]
    
    

# print(return1)


# 짝수와 홀수
# 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

# def solution(num):
#     if num % 2 == 0:
#         return "Even"
#     if num % 2 != 0:
#         return "Odd"


# 자릿수 더하기


# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

# n = input()
# d = list(str(n))
# l = []
# for i in d:
#     l.append(int(i))

# print(sum(l))

최대공약수와 최소공배수

# answer = []
#     a = []
#     for i in range(1,min(n,m)+1)
#         if n % i == 0 and m % i == 0 :
#             a.append(i)
#     a = set(a)


ㅇㅇ






























     
    
    
    


    
    











        




