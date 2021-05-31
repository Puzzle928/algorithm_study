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
def solution(prices):
    answer = [0] * len(prices)  ## len(price)   
    for i in range(len(prices)): 
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

