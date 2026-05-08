class Queue:
    def __init__(self):
        self.q=[None]*5
        self.front=0
        self.size=0
    def is_empty(self):
        return self.size==0
    def capacity(self):
        return len(self.q)
    def resize(self,cap):
        old=self.q
        self.q=[None]*cap
        walk=self.front
        for i in range(self.size):
            self.q[i]=old[walk]
            walk=(walk+1)%len(old)
        self.front=0
    def enqueue(self,n):
        if self.size==len(self.q):
            self.resize(2*len(self.q))
        avail=(self.front+self.size)%len(self.q)
        self.q[avail]=n
        self.size+=1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        elif 0<self.size<(len(self.q)//4):
            self.resize(len(self.q)//2)
        ans=self.q[self.front]
        self.q[self.front]=None
        self.size-=1
        self.front=(self.front+1)%len(self.q)
        return ans

class Stack:
    def __init__(self):
        self.s=[]
    def is_empty(self):
        return len(self.s)==0
    def top(self):
        if self.is_empty():
            raise IndexError
        return self.s[-1]
    def push(self,data):
        self.s.append(data)
    def pop(self):
        if self.is_empty():
            raise IndexError
        x=self.s.pop()
        return x