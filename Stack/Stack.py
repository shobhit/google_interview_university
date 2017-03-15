class Stack(object):
    def __init__(self):
        self._size = 0
        self.head = None
        self.arr = []

    def pop(self):
        if self._size==0:
            print "Cannot pop,already 0"
            return

        self._size-=1
        self.head=self.arr[0]
        popped_val = self.arr.pop(0)
        return popped_val

    def push(self, value):
        self.arr.insert(0, value)
        self._size+=1
        self.head=value

    def peek(self):
        print "Top is=>",self.head
        return self.head

    def size(self):
        return self._size

    def clear(self):
        self.arr=[]
        self._size=0
        self.head=None
        return self.arr

    def clone(self):
        pass

    def to_array(self):
        return [i for i in self.arr]

    def print_stack(self):
        if self.size()==0:
            print "Nothing in Stack"
            return
        print "printing Stack"
        for i in self.arr:
            print "|",i,"|"
        print "------"


# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# stack.push(40)
# stack.print_stack()
# stack.size()
# stack.peek()
# print stack.to_array()
# stack.pop()
# stack.size()
# print stack.to_array()
# stack.clear()
# stack.size()
# stack.peek()