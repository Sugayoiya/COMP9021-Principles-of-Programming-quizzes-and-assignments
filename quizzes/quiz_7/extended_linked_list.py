# Written by **** for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)
		
    def rearrange(self):
        if not self.head or not self.head.next_node:
            # print("no list")
            return
        current_node = self.head
        last_odd = None
        end_node = None
        while current_node.next_node:
            if current_node.value % 2 == 1:
                last_odd = current_node
            current_node = current_node.next_node
        if current_node.value % 2 == 1:
            last_odd = current_node
        end_node = current_node
        if not last_odd:
            return
        current_node = self.head
        pre_current_node = None
        end_flag = last_odd
        # print("current_node",current_node.value,"last_odd",last_odd.value,"end_node",end_node.value)
        while current_node.next_node and current_node != end_flag:
            # print("current_node",current_node.value)
            if current_node.value % 2 == 0:
                if current_node == self.head:
                    if last_odd == end_node:
                        next_current = current_node.next_node
                        current_node.next_node = None
                        last_odd.next_node = current_node
                        last_odd = current_node
                        current_node = next_current
                        self.head = current_node
                    else:
                        last_next = last_odd.next_node
                        next_current = current_node.next_node
                        current_node.next_node = None
                        last_odd.next_node = current_node
                        last_odd.next_node.next_node = last_next
                        last_odd = last_odd.next_node
                        current_node = next_current
                        self.head = current_node
                else:
                    if last_odd == end_node:
                        next_current = current_node.next_node
                        current_node.next_node = None
                        temp = current_node
                        pre_current_node.next_node = next_current
                        last_odd.next_node = temp
                        last_odd = last_odd.next_node
                        current_node = pre_current_node.next_node
                    else:
                        last_next = last_odd.next_node
                        next_current = current_node.next_node
                        current_node.next_node = None
                        temp = current_node
                        pre_current_node.next_node = next_current
                        last_odd.next_node = temp
                        last_odd.next_node.next_node = last_next
                        last_odd = last_odd.next_node
                        current_node = pre_current_node.next_node
            else:
                pre_current_node = current_node
                current_node = current_node.next_node
                # print("pre_current_node",pre_current_node.value)