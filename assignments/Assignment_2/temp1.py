if not self.head:
    print("jugde none")
    return
current_node = self.head
print(type(current_node),"head")
while current_node:
    if current_node.value % 2 == 1:
        current_node =current_node.next_node
        print(current_node,current_node.value,"odd")
    else:
        pre_next_odd = current_node
        next_odd_node =current_node.next_node
        while next_odd_node:
        	if next_odd_node.value % 2 == 1:
        		print(next_odd_node,next_odd_node.value,"odd")
        		pre_next_odd.next_node = next_odd_node.next_node
        		next_odd_node.next_node = current_node
        		next_odd_node = pre_next_odd.next_node
        	elif next_odd_node.next_node:
        		next_odd_node = next_odd_node.next_node
        		pre_next_odd = pre_next_odd.next_node
        	else:
        		return
return




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
        first_odd = None
        first_even = None
        while current_node.next_node :
            if current_node.value % 2 == 1 and not first_odd:
                first_odd = current_node
            if current_node.value % 2 == 0 and not first_even:
                first_even = current_node
            current_node = current_node.next_node
        if current_node.value % 2 == 1:
            first_odd = current_node
        else:
            first_even = current_node
        if first_odd and not first_even:
            # print("no even")
            return
        if first_even and not first_odd:
            # print("no odd")
            return
        # gets end node
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        end_node = current_node
        final_node = end_node
        # make first node odd
        current_node = self.head
        while current_node.value % 2 == 0:
            # print(current_node.value,"current_node")
            next_current = current_node.next_node
            current_node.next_node = None
            final_node.next_node = current_node
            self.head = next_current
            current_node = self.head
            final_node = final_node.next_node
        #
        current_node = self.head.next_node
        link = self.head
        # print(self.head.value,"self.head")
        flag = 0
        while current_node != end_node:
            # print(link.value,"link",current_node.value,"loop",end= ' ')
            if current_node.value % 2 == 0:
                next_current = current_node.next_node
                current_node.next_node = None
                final_node.next_node = current_node
                link.next_node = next_current
                final_node = final_node.next_node
                flag = 1
            if flag == 1:
                current_node = link.next_node
                flag = 0
            else:
                link = link.next_node
                current_node = link.next_node
        if end_node.value % 2 == 0:
            next_current = end_node.next_node
            end_node.next_node = None
            link.next_node = next_current
            final_node.next_node = end_node




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

