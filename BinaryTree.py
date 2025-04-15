
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        

class BT:
    def __init__(self):
        self._root = None
        
    def create(self, value):
        node = Node(value)
        
        if self._root == None:
            self._root = node
            
            return self
        
        else:
            self._insertNode(self._root,node)
            
            return self
    
    def find(self, value):
        current = self._root
        
        if current.value == value:
            return current
        
        if value < current.value:
            return self._findNode(current.left, value)
        
        else:
            return self._findNode(current.right, value)
        
    def findMaxNode(self,):
        current = self._root
        
        return self._findMaxNode(current)
        
        
        
    def findMinNode(self):
        current = self._root
        
        return self._findMinNode(current)
    
    def _findMaxNode(self, current):
        if current.right != None:
            if current.value < current.right.value:
                return self._findMaxNode(current.right)
            else:
                return current
            
        else:
            return current
    
    def _findMinNode(self, current):
        if current.left != None:
            if current.left.value < current.value:
                return self._findMinNode(current.left)
            else:
                return current
            
        else:
            return current
            
            
    
    def _findNode(self, currentNode, value):
        
        if currentNode.value == value:
            return currentNode
        
        elif(value < currentNode.value and currentNode.left != None):
            return self._findNode(currentNode.left, value)

        elif(value > currentNode.value and currentNode.right != None):
            return self._findNode(currentNode.right, value)

        return None
        
    def _insertNode(self, current,node):
        if(node.value < current.value):
            if current.left != None:
                self._insertNode(current.left, node)
            else:
                current.left = node
        
        else:
            if current.right != None:
                self._insertNode(current.right, node)
            else:
                current.right = node
                
                
    
    
tree = BT()
tree.create(20).create(25).create(100).create(15).create(0).create(1000).create(-2000)
print(tree.findMaxNode().value)
print(tree.findMinNode().value)


