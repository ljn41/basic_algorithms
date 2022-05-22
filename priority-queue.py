# Queue is first in first out
# Property of Priority Queue :
# An element with high priority is dequeued before an element with low priority.
# thus, in Priority Queue, element based on highest priority is dequeued.
class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ','.join([str(i) for i in self.queue])

    def insert(self,data):
        self.queue.append(data)

    def delete(self):
        max_priority = 0
        for i in range(0,len(self.queue)):
            if self.queue[i] > self.queue[max_priority]:
                max_priority = i

        del self.queue[max_priority]


if __name__ == '__main__':
    new_pq = PriorityQueue()
    new_pq.insert(4)
    new_pq.insert(2)
    new_pq.insert(1)
    new_pq.insert(8)
    new_pq.insert(3)
    print(new_pq)
    new_pq.delete()
    print(new_pq)