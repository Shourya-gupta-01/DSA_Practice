class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
        
class DLL:
    def __init__(self,start=None):
        self.start=start
        
    def is_empty(self):
        return self.start==None
    
    def insert_at_first(self,data):
        n=Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start=n 
        
    def insert_after(self,data,num=None):
        if self.is_empty():
            self.insert_at_first(data)
        else:
            temp=self.start
            while temp is not None:
                if temp.item==num and temp.next==None:
                    self.insert_at_Last(data)
                elif temp.item==num:
                    n=Node(temp.item,data,temp.next)
                    temp.next.prev=n
                    temp.next=n
                    break
                temp=temp.next
            
    def insert_at_Last(self,data):
        temp=self.start
        if self.start!=None:
            while temp.next is not None:
                temp=temp.next
        n=Node(temp.item,data,None)
        temp.next=n
        
    def search(self,ele):
        temp=self.start
        c=0
        while temp is not None:
            if temp.item==ele:
                return f"The Element is Found at index {c}"
            temp=temp.next
            c+=1
        else:
            return f"The Element is not Found"
        
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
            if self.start is not None:
                self.start.prev=None
                
    def delete_lst(self):
        if self.start==None:
            pass
        elif self.start.next==None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next!=None:
                temp=temp.next
            temp.next=None
            
    def delete_item(self,num=None):
        if self.is_empty():
            pass
        else:
            temp=self.start  
            while temp is not None:
                if num==self.start.item and num==temp.item:
                    self.delete_first()
                    break
                elif temp.item==num and temp.next==None:
                    self.delete_lst()
                    break
                elif temp.item==num:
                    temp.prev.next=temp.next
                    temp.next.prev=temp.prev
                    break
                temp=temp.next
            else:
                print("Element not Found")
                             
    def __iter__(self):
        return DLLIterator(self.start)
                    
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
            
    def print_node(self):
        temp=self.start
        while temp!=None:
            print(temp.prev,temp.item,temp.next)
            temp=temp.next

class DLLIterator:
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
            
a=DLL()
a.insert_at_first(5)
a.insert_at_first(4)
a.insert_at_first(3)
a.insert_at_first(2)
a.insert_at_first(1)
a.insert_at_first(0)
a.insert_at_Last(6)
a.insert_at_Last(7)
a.delete_item(6)
a.print_list()