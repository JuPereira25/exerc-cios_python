# Implementar uma fila usando lista

from collections import deque

queue = deque([10, 12, 15])
queue.append(18)
queue.append(21)
queue.popleft()
queue.popleft()
print(queue)