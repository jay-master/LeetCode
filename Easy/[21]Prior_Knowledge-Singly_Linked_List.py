"""
Python Data Structure: Singly linked list

"""

# Node class
class Node:
    def __init__(self, val=0, next = None):
        self.val = val  # value of a node
        self.next = next    # variable pointing the next node

# Singly linked list class:
class SList:
    def __init__(self):
        self.head = None    # Linked list has nothing at the beginning
        self.size = 0   # To check the size of the list

    # Check the size of the list
    def listsize(self):
        return self.size

    # Check whether the list is empty or not
    def isempty(self):
        if self.size == 0:
            return True
        else:
            return False

    # Select a specific node using index (index starts from 0)
    def selectnode(self, idx):
        if idx >= self.size:
            print("Index Error")
            return None
        if idx == 0:
            return self.head
        else:
            selected = self.head
            for cnt in range(idx):
                selected = selected.next
            return selected

    # Append a new node on the right side of the list
    def append(self, val):
        if self.head == None:   # If the node to be added is the first node, the new node will be the 'head'
            self.head = Node(val)
        else:
            curlast = self.head # curlast: current last node
            while curlast.next != None:
                curlast = curlast.next
            newtail = Node(val)
            curlast.next = newtail
        self.size += 1

    # Append a new node on the lest side of the list
    def appendleft(self,val):
        if self.head == None:   # If the node to be added is the first node, the new node will be the 'head'
            self.head = Node(val)
        else:
            self.head = Node(val, self.head)
        self.size += 1

    # Insert a new node at the specific index of the list
    def insert(self, val, idx):
        if self.isempty():  # If the list is empty, the new node will be the 'head'
            self.head = Node(val)
        elif idx == 0:
            self.head = Node(val, self.head)
        else:
            beforeinsert = self.selectnode(idx-1)   # beforeinsert: the node before the new node to be inserted
            if beforeinsert == None:
                return  # Return None, if the new node should be inserted index 'i+2', and the last index of the list is 'i'.
            newnode = Node(val)
            afterinsert = beforeinsert.next # afterinsert: the node after the new node to be inserted (the shifted node due to the new node)
            beforeinsert.next = newnode
            newnode.next = afterinsert
            self.size += 1

    # Delete a specific node using index (index starts from 0)
    def delete(self, idx):
        if self.isempty():
            print('Underflow: Empty Linked List Error')
            return
        elif idx >= self.size:   # I think >= is correct (in original code: > )
            print('Overflow: Index Error')
            return
        elif idx == 0:
            target = self.head
            self.head = target.next
            del(target)
        # I think latter is correct, but both run smoothly. Why?
        # else:
        #     beforedel = self.selectnode(idx-1)   # beforedel: the node before the new node to be deleted
        #     beforedel.next = beforedel.next.next
        #     deltarget = beforedel.next
        #     del(deltarget)
        else:
            beforedel = self.selectnode(idx-1)   # beforedel: the node before the new node to be deleted
            deltarget = beforedel.next
            beforedel.next = beforedel.next.next
            del(deltarget)
        self.size -= 1  # Not included in original code, but it should be here.

    # Print the list
    def printlist(self):
        target = self.head
        while target:
            if target.next != None:
                print(target.val, '-> ', end='')
                target = target.next
            else:
                print(target.val)
                target = target.next



# Test
mylist = SList()
mylist.append('A')
mylist.printlist()
mylist.append('B')
mylist.printlist()
mylist.append('C')
mylist.printlist()
mylist.insert('D', 1)
mylist.printlist()
mylist.appendleft('E')
mylist.printlist()
print(mylist.listsize())
mylist.delete(0)
mylist.printlist()
mylist.delete(3)
mylist.printlist()
mylist.delete(0)
mylist.printlist()
mylist.appendleft('A')
mylist.printlist()
print(mylist.listsize())