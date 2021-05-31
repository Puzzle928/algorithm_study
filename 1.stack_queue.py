from queue import Queue

# stack 은 쌓다 라는 개념

## 비커 개념 !!!! 


##  push,       peek ,       pop  의 개념을 정리해볼 수 있다.


# python 직접 구현

class Stack(list):
    push = list.append

    def peek(self):
        return self[1]
        

# push 넣다라는 개념 자료를 넣으면 

s = Stack()

s.push(1)
s.push(5)
s.push(10)




# peek 보다 맨 나중에 넣은 값을 보는것

def peek(self):
    return self[-1]


s= []
s.append(1)
s.append(5)
s.append(10)
#print(s)   ## 1, 5, 10
s.pop()  ## 10
#print(s)  ## [1.5]



## Queue  일이 처리되기를 기다리는 리스트의 의미
## 선착순 방식을 고수

##         put,   peek,   get      구조


class Queue(list):
    put = list.append

    def peek(self):
        return self[0]

    def get(self):
        return self.pop(0)


q  = Queue()

q.put(1)
q.put(5)
#print(q)  # 1,5
q.get() # 1
#print(q) # 5
q.peek()  # 5

d = []

d.append(1)
d.append(2)
d.append(3)
#print(d) # 1, 2, 3
d.pop(0) # 2,3
d[0]


# 프로그래머스 주식가격 풀이    input 값 prices = [1,2,3,2,3]
# 주식시장에서 초당 가격의 변화값을 리스트로 입력해 그 가격이 하락할때까지 버틴 시간을 계산하는 문제
# 요점은 시간!!
def solution(prices):
    answer = [0] * len(prices)  #len(prices)는 값의 길이 여기서는 개수 결과값 ## [0,0,0,0,0]
    for i in range(len(prices)): #len(prices) 값은 5 따라서 range5는 0~4의 값을 갖는다
        for j in range(i+1, len(prices)): #len(prices)= 5 i는 0부터시작하므로 1,5부터시작 j값은 1~4의 값을 갖는다.
            if prices[i] <= prices[j]: # i가 0이고 j= 1,2,3,4 i가 1일때 j가 1,2,3,4값 대입
                answer[i] += 1 #answer[0] = 첫째자리의미 i가 0일때  조건식 반복 
            else:              # i 가 j 보다 작아질때까지 반복후 작아지면 마지막1을 플러스하고 break
                answer[i] += 1 # 이후 i가 1일경우에 loop를 반복 인덱스값들이 정해진다.
                break
    return answer

# 할 수 있다..
