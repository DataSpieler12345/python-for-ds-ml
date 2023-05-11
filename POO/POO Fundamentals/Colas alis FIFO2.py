class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.insert(0, elem)

    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError("The queue is empty")

    def isempty(self):
        # Returns True if the queue is empty, otherwise it returns False..
        return len(self.queue) == 0


class SuperQueue(Queue):
    pass


que = SuperQueue()
que.put(1)
que.put("Dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Empty queue")