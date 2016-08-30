from collections import deque
queue = deque(['1', '2', '3', '4'])
queue.append('5')
queue.popleft()
print(queue)
queue1 = deque({'qi', 'xiao', 'song'})
print(queue1)
queue2 = deque({'1': 'qi', '2': 'xiao', '3': 'song'})
print(queue2)
