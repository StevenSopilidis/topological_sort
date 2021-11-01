from typing import NoReturn, overload


class Node:
    value = 0
    next_node = None
    
    def __init__(self,value) -> None:
        self.value = value

class LinkedList:
    root = Node(0)
    list_length = 0

    def __init__(self, value):
        self.list_length = 1
        self.root.value = value

    #inserts new node in list (at a given index)
    #it will insert it in the end if index > len(list)
    #if index = -1 insert at end
    #insertion is 0 based indexed
    @classmethod
    def insert(self, value, index = -1) -> None:
        self.list_length+=1
        
        node = self.root
        #insert at end
        if(index == -1):
            while(node.next_node != None):
                node = node.next_node
            node.next_node = Node(value)
            return

        #insert at beggining
        if(index == 0):
            tmp = node
            self.root = Node(value)
            self.root.next_node = node
            return

        #insert at the given index
        i = 1
        while(i < index and node.next_node != None):
            i += 1
            node = node.next_node
        if(node.next_node == None):
            node.next_node = Node(value)
            return
        tmp = node.next_node
        node.next_node = Node(value)
        node.next_node.next_node = tmp

    #checks if node exists
    @classmethod
    def exists(self, value) -> bool:
        node = self.root
        while(node.value != value and node.next_node != None):
            node = node.next_node
        if(node.value == value):
            return True
        return False

    #method to print elements of list
    @classmethod
    def print_els(self):
        node = self.root
        while(node != None):
            print(node.value)
            node = node.next_node

    #gets index for a give value
    #returns -1 if no element was found
    @classmethod
    def get_index(self, value):
        node = self.root
        index = 0
        while(node.value != value and node.next_node != None):
            index += 1
            node = node.next_node
        if(node.next_node == None):
            if(node.value == value):
                return index
            else:   
                return -1
        return index

    #swaps values between 2 nodes
    #does nothing if index1 or index2 are larger than length of list
    @classmethod
    def swap_values(self, index1, index2) -> None:
        if(self.list_length < index1 or self.list_length < index2):
            return
        #get the bigger index between 2 for while loop
        bigger_index  = 0
        if(index1 > index2):
            bigger_index = index1
        else:
            bigger_index = index2
        #loop through list and find the nodes
        i = 0
        node = self.root
        node1 = Node(0)
        node2 = Node(0)
        while(i <= bigger_index):
            if(i == index1):
              node1 = node
            elif(i == index2):
              node2 = node
            node = node.next_node
            i+=1
        #swap their values
        node1.value, node2.value = node2.value, node1.value