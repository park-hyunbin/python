class LinkedStack :
    def __init__(self) :
        self.head = None
class Node :
    def __init__(self,elem,link=None) :
        self.data =elem
        self.link = link

    def isEmpty(self) : return self.head == None
    def clear(self) : self.head = None
    def size(self): 
        node = self.head
        count = 0 
        while not node == None :
            node = node.link
            count += 1 
        return count

    def display(self,msg='DoublyLinkedList :'): 
        print(msg,end='')
        node = self.head
        while not node == None :
            print(node.data, end = '')
            node= node.link
        print()
    def getNode(self, pos):
        if pos<0 : return None 
        node = self.head
        while pos > 0 and node != Node :
            node = node.link
            pos -=1
        return node

    def insert(self,pos,elem):
        before = self.getNode(pos-1)
        if before == None :
            self.head = Node(elem, self.head)
        else : 
            node = Node(elem, before.link)
            before.link = node
    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None : 
            if self.head is not None : 
                self.head = self.head.link
            elif before.link != None :
                before.link = before.link.link 

