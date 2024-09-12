#deque - double ended queue

#FIFO

from collections import deque

#create deque
#d=deque()

d=deque([1,2,3])
print(d)

d.append(4)
print(d)

d.appendleft(0)
print(d)

d.extend([5])
print(d)
print(d.pop())

print(d.popleft())

d.reverse()
print(d)