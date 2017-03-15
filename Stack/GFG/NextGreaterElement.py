from algorithmic_toolb.Stack.Stack import Stack


# http://www.geeksforgeeks.org/next-greater-element/
class NextGreaterElement:
    def __init__(self):
        self.stack = Stack()
        self.arr = []
        self.dct={}

    def find_next_greater_elem(self, arr):
        stack = []
        for i in arr:
            while stack and i>stack[-1]:
                self.dct[stack.pop()] = i
            stack.append(i)


        print self.dct



nge = NextGreaterElement()
nge.find_next_greater_elem([9, 8, 7, 3, 2, 1, 6])
