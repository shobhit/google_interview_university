from Node import Node

#Implement Queue using linked-list, with tail pointer:
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def print_head(self):
        print "Head is =>", self.head.data

    def print_tail(self):
        print "Tail is =>", self.tail.data

    def enqueue(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            print "Added=>", node.data
            self.tail.next = node
            node.next = None
            self.tail = node

    def dequeue(self):
        if self.head is not None:
            node = self.head
            if self.head.next is None:
                print "Removed=>", self.head.data
                print "No element left in list"
                self.head = None
                self.tail = None
            else:
                print "Removed=>", node.data
                next_node = node.next
                self.head = next_node

    def print_list(self):
        current = self.head
        if current is None:
            print "Nothing to print"
            return 0

        print "++++Printing List+++"
        while current is not None:
            print current.data
            current = current.next
        print "+++End list++++"


linked_list = LinkedList()
linked_list.enqueue(10)
linked_list.enqueue(20)
linked_list.enqueue(30)
linked_list.enqueue(40)
linked_list.print_list()
linked_list.print_head()
linked_list.print_tail()
linked_list.dequeue()
linked_list.print_list()
linked_list.dequeue()
linked_list.print_list()
linked_list.dequeue()
linked_list.print_list()
linked_list.dequeue()
linked_list.print_list()
