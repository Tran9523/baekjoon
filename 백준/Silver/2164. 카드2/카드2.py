N = int(input())

class CustomQueue:
    def __init__(self):
        self.data = []
        self.front_idx = 0

    def push(self, x):
        self.data.append(x)

    def empty(self):
        return self.front_idx >= len(self.data)

    def pop(self):
        if self.empty():
            return -1
        x = self.data[self.front_idx]
        self.front_idx += 1

        if self.front_idx > 100000:
            self.data = self.data[self.front_idx:]
            self.front_idx = 0

        return x

    def size(self):
        return len(self.data) - self.front_idx

    def front(self):
        if self.empty():
            return -1
        return self.data[self.front_idx]

cq = CustomQueue()
for i in range(1, N + 1):
    cq.push(i)

while cq.size() > 1:
    cq.pop()
    cq.push(cq.pop())

print(cq.front())
