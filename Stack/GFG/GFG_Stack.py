from algorithmic_toolb.Stack.Stack import Stack


class GFG_Stack(object):
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    # http://www.geeksforgeeks.org/queue-using-stacks/
    def __queue_using_two_stack(self):
        pass

    def add_to_queue(self, value):
        print value,"Added"
        self.stack1.push(value)

    def remove_from_queue(self):
        while self.stack1.size() != 0:
            self.stack2.push(self.stack1.pop())

        self.stack2.pop()

    def print_queue(self):
        self.stack2.print_stack()


gfg = GFG_Stack()
gfg.add_to_queue(10)
gfg.add_to_queue(20)
gfg.add_to_queue(30)
gfg.add_to_queue(40)
gfg.add_to_queue(50)
gfg.remove_from_queue()
gfg.print_queue()

