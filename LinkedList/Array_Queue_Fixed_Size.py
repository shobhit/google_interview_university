import sys
import random


class FSQueue(object):
    def __init__(self, size=None):
        if size is None:
            size = 50  # Taking 50 as random input
        elif size < 0:
            print "Size cannot be in Negative"
            sys.exit(0)

        self.array = [None for i in range(size)]
        self.index = 0
        self.max_size = 0 if size == 0 else size - 1

    def enqueue(self, value):
        if self.max_size==0:
            print "Queue has 0 size so cannot input anything"
            return

        if self.index == self.max_size:
            print "Queue is full. dequeue first"
            return
        else:
            self.array[self.index] = value
            self.index += 1

    def dequeue(self):
        if self.max_size==0:
            print "Mothing to dequeue"
        else:
            self.array.pop(0)
            self.index-=1

    def print_queue(self):
        print "+++Printing Queue+++"
        for i in self.array:
            if i is None:
                return
            else:
                print i


fs_queue = FSQueue(10)

for i in range(random.randint(5,12)):
    fs_queue.enqueue(random.randint(1, 40))

fs_queue.print_queue()
print "Index=>", fs_queue.index
fs_queue.dequeue()
fs_queue.dequeue()
fs_queue.dequeue()
fs_queue.print_queue()
print "Index=>", fs_queue.index