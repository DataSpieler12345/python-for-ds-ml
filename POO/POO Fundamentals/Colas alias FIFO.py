class QueueError(Exception):
    # Derives from the Exception base class to create a new custom exception.
    pass


class Queue:
    def __init__(self):
        # We use a list to store the elements of the queue.
        self.__queueList = []

    def put(self, elem):
        # We add the element to the end of the list.
        self.__queueList.append(elem)

    def get(self):
        if len(self.__queueList) > 0:
            # We take the first element of the list and delete it.
            return self.__queueList.pop(0)
        else:
            # If the list is empty, we throw a custom exception.
            raise QueueError("The queue is empty")


que = Queue()
que.put(1) #output1
que.put("Dog") #output2
que.put(False)
try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error") #output3