class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
    
class SLL:
    def __init__(self,start=None):
        self.start=start
        self.size=0
        
    def is_empty(self):
        return self.start==None
    
    def insert_at_first(self,data):
        n=Node(data,self.start)
        self.start=n
        self.size+=1
        
    def insert_at_last(self,data): 
        n=Node(data) 
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
            self.size+=1
        else:  
            self.start=n
            self.size+=1
        
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    
    def insert_after(self,num,data):
        temp=self.start
        while temp.item!=num:
            temp=temp.next
        n=Node(data,temp.next)
        temp.next=n
        self.size+=1
            
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
            
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
            self.size-=1
            
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
            self.size-=1
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
            self.size-=1
    
    def delete_item(self,data):
        if self.start is None:
            pass 
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
                self.size-=1
        else:
            temp=self.start
            if temp.item==data:
                self.start=temp.next
                self.size-=1
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
                self.size-=1
                    
    def sizeof(self):
        return self.size
    
    def reverse(self):
        try:
            curr=self.start
            prev=self.start.next
            nxt=None
            while prev is not None:
                curr.next=nxt
                nxt=curr
                curr=prev
                prev=prev.next
            curr.next=nxt
            nxt=curr
            self.start=nxt
        except:
            print("The given linked list is empty")
    
    def __iter__(self):
        return SLLIterator(self.start)
    
class SLLIterator:
    def __init__(self,start):
        self.current=start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data
                
if __name__=="__main__": 
    mylist=SLL()
    mylist.insert_at_first(5)
    mylist.insert_at_first(4)
    mylist.insert_at_first(3)
    mylist.insert_at_first(2)
    mylist.print_list()