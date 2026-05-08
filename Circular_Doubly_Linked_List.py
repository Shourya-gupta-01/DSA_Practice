class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
        
class CDLL:
    def __init__(self,start=None):
        self.start=start
        
    def is_empty(self):
        return self.start is None
    
    def insert_at_first(self,data):
        n=Node(data)
        if self.start is None:
            n.next=n
            n.prev=n
            self.start=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n.item
            self.start.prev=n
            self.start=n
            
    def inser_at_last(self,data):
        n=Node(data)
        if self.start is None:
            n.next=n
            n.prev=n
        else:
            n.prev=self.start.prev
            n.next=self.start
            self.start.prev.next=n
            self.start.prev=n
            
    def print_list(self):
        temp=self.start
        if temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
            while temp is not self.start:
                print(temp.item,end=' ')
                temp=temp.next
        else:
            print("None")
            
a=CDLL()
print(a.is_empty())
a.insert_at_first(2)
a.insert_at_first(1)
a.print_list()