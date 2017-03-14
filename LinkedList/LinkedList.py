from Node import Node


# http://www.geeksforgeeks.org/write-a-function-to-get-nth-node-in-a-linked-list/
# http://www.geeksforgeeks.org/given-only-a-pointer-to-a-node-to-be-deleted-in-a-singly-linked-list-how-do-you-delete-it/

class LinkedListWithoutTailPointer(object):
    def __init__(self):
        self.head = None

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count, "Size"

    def empty(self):
        self.head = None
        return self.head, "Emptied List"

    def value_at(self, index, zero_based_index=False):
        if index == 0:
            return "Index Starts from 1"
        else:
            current = self.head
            count = 0 if zero_based_index else 1
            val = None
            while current is not None:
                if count == index:
                    val = current.data
                    break
                else:
                    count += 1
                    current = current.next

            return val, "Data"

    def push_front(self, value):
        node = Node(value)

        if not self.head:
            node.next = None
            self.head = node
        else:
            next_p = self.head
            self.head = node
            node.next = next_p

    def pop_front(self):
        if self.head is None:
            return "Can't Pop, Already empty list"
        else:
            popped = self.head
            self.head = self.head.next
            return popped.data, "Popped Front"

    def push_back(self, value):
        current = self.head
        prev = None
        while current is not None:
            prev = current
            current = current.next
            if current is None:
                prev.next = Node(value)

    def pop_back(self):
        if self.head is None:
            return "Can't Pop, Already empty list"
        else:
            current = self.head
            prev = None
            while current.next is not None:
                prev = current
                current = current.next
                if current.next is None:
                    prev.next = None

    def front(self):
        return self.head.data, "FRONT"

    def back(self):
        current = self.head
        last_p = None
        while current is not None:
            last_p = current.data
            current = current.next
        return last_p, "Last"

    def insert(self, index, value):
        new_p = Node(value)

        if index > self.size():
            return "Index is higher than elements present"

        if index == 1:
            new_p.next = self.head
            self.head = new_p
            return

        count = 1
        current = self.head
        prev = None
        while current is not None and count != index:
            prev = current
            count += 1
            current = current.next

        prev.next = new_p
        new_p.next = current

    def erase(self, index):
        if index > self.size():
            return "Cannot erase since index greater than size"

        current = self.head
        prev = None
        count = 1
        while current is not None and count != index:
            prev = current
            count += 1
            current = current.next

        prev.next = current.next

    def value_n_from_end(self, n):
        pass

    def reverse(self):
        current = self.head
        prev = None
        next = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

    def remove_value(self):
        pass

    def print_list(self):
        current = self.head
        while current is not None:
            print current.data, " Element", current.next, " Next"
            current = current.next
    #http://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/
    def print_middle(self):
        ##1st Method

        fast_ptr =self.head
        slow_ptr = self.head
        while fast_ptr is not None and fast_ptr.next is not None:
            fast_ptr = fast_ptr.next.next
            slow_ptr=slow_ptr.next

        print slow_ptr.data

        ##Second Method
        count =0
        mid = self.head
        current = self.head

        while current is not None:
            if count & 1==1:
                mid = mid.next

            current = current.next
            count+=1
        print mid.data



p = LinkedListWithoutTailPointer()
p.push_front(10)
p.push_front(20)
p.push_front(30)
p.push_front(40)
p.push_front(50)
p.push_front(60)
p.push_front(70)
p.push_front(80)

# p.print_list()
# print p.size()
# print p.pop_front()
# print p.size()
# p.print_list()
# print p.front()
# print p.back()
# # # print p.empty()
# print p.value_at(1)
# print p.value_at(1, zero_based_index=True)
# p.push_back(1000)
# p.push_back(1200)
# p.print_list()
# p.pop_back()
# p.print_list()
# p.insert(2, 999)
# p.print_list()
# p.insert(1, 998)
# print "Printing list"
# p.print_list()
# p.erase(2)
# p.print_list()
# p.erase(4)
# p.print_list()
# print p.size()
# p.erase(3)
# p.print_list()
# print p.size()
# p.reverse()
# p.print_list()
p.print_middle()
