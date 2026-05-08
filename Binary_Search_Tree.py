class Node:
    def __init__(self, item = None, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right
        
class BST:
    def __init__(self, root = None):
        self.root = root
        
    def insert(self, value):
        self.root = self.rinsert(self.root, value)
        
    def rinsert(self, root, value):
        if root is None:
            return Node(value)
        if value < root.item:
            root.left = self.rinsert(root.left, value)
        else:
            root.right = self.rinsert(root.right, value)
        return root
    
    def search(self, value):
        temp = self.root
        search_node = self.rsearch(temp, value)
        return search_node
        
    def rsearch(self, root, value):
        while root:
            if value == root.item:
                return root.item
            elif value < root.item:
                root = root.left
            else:
                root = root.right
        return None
    
    def inorder_display(self):
        res = []
        self.rinorder(self.root, res)
        return res
    
    def rinorder(self, root, res):
        if root:
            self.rinorder(root.left, res)
            res.append(root.item)
            self.rinorder(root.right, res)
            
    def preorder_display(self):
        res = []
        self.rpreorder(self.root, res)
        return res
    
    def rpreorder(self, root, res):
        if root:
            res.append(root.item)
            self.rpreorder(root.left, res)
            self.rpreorder(root.right, res)
            
    def postorder_display(self):
        res = []
        self.rpostorder(self.root, res)
        return res
    
    def rpostorder(self, root, res):
        if root:
            self.rpostorder(root.left, res)
            self.rpostorder(root.right, res)
            res.append(root.item)
            
    def min_node(self):
        temp = self.root
        while temp.left:
            temp = temp.left
        return temp.item
    
    def max_node(self):
        temp = self.root
        while temp.right:
            temp = temp.right
        return temp.item
    
    def del_node(self, value):
        self.root = self.rdelete(self.root, value)
        
    def rdelete(self, root, value):
        if root is None:
            return root
        if value < root.item:
            root.left = self.rdelete(root.left, value)
        elif value > root.item:
            root.right = self.rdelete(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item = self.min_node(root.right)
            self.rdelete(root.right, root.item)
        return root
    
    def size(self):
        return len(self.inorder_display())
        
            
bst1 = BST()
bst1.insert(10)
bst1.insert(20)
bst1.insert(5)
bst1.insert(6)
print(bst1.min_node())
print(bst1.max_node())
print(bst1.search(20))
bst1.del_node(20)
print(bst1.inorder_display())
print(bst1.size())