# 1.두 정수 사이의 합
# 두 정수 a,b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수,solution을 완성하세요.
# 예를 들어 a = 3. b = 5인 경우, 3+4+5 = 12 이므로 12를 리턴합니다.

a = int(input())
b = int(input())
print(max(a,b))
answer = 0
for i in range(min(a,b),max(a,b)+1):
    answer += i


print(answer)




