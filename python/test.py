# -*- coding: utf-8 -*-

import sys

# 스택
class Stack():
    
    def __init__(self):
        self.top = -1
        self.stack = []
    
    def pop(self):
        if self.isEmpty() == 1:
            print 'Stack is Empty!'
            sys.exit()
        else:
            temp = self.stack[self.top]
            self.top -= 1
            return temp
    
    def push(self, data):
        if self.isOverflow() == 1:
            print 'Stack Over Flow!'
            sys.exit()
        self.top += 1
        self.stack.append(data)
        return 0
    
    def isOverflow(self):
        if self.top >= len(self.stack):
            return 1
        else:
            return 0
    
    def isEmpty(self):
        if self.top < 0:
            return 1
        else:
            return 0


# 이진 트리
class Tree():
    
    def __init__(self, data, lchild = None, rchild = None):
        #self.stack = Stack()
        
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

    def getData(self):
        return self.data
    
    def getLeftSubTree(self):
        return self.lchild
    
    def getRightSubTree(self):
        return self.rchild
    
    def insert(self, data):
        if data < self.data:
            if self.lchild is None:
                self.lchild = Tree(data)
            else:
                self.lchild.insert(data)
        else :
            if self.rchild is None:
                self.rchild = Tree(data)
            else:
                self.rchild.insert(data)
    
    
    def delete(self, data):
        # http://www.laurentluce.com/posts/binary-search-tree-library-in-python/
        pass
    
    
    def lookup(self, data, parent = None):
        if data < self.data:
            if self.lchild is None:
                return None, None
            else:
                return self.lchild.lookup(data, self)
        elif data > self.data:
            if self.rchild is None:
                return None, None
            else:
                return self.rchild.lookup(data, self)
        else:
            return self, parent
            
    
    # 전위순회
    def preorderTraverse(self, Tree):
        if Tree == None:
            return
        
        print Tree.getData()
        Tree.preorderTraverse(Tree.getLeftSubTree())
        Tree.preorderTraverse(Tree.getRightSubTree())

    
    # 중위순회
    def inorderTraverse(Tree):
        if Tree == None:
            return
        
        inorderTraverse(Tree.getLeftSubTree())
        print Tree.getData()
        inorderTraverse(Tree.getRightSubTree())

        
    # 후위순회
    def postorderTraverse(Tree):
        if Tree == None:
            return

        postorderTraverse(Tree.getLeftSubTree())
        postorderTraverse(Tree.getRightSubTree())
        print Tree.getData()




if __name__ == '__main__':
    
    
    
    root = Tree(8)
    root.insert(3)
    root.insert(10)
    root.insert(1)
    root.insert(6)
    
    root.preorderTraverse(root)
    
    
    node, parent = root.lookup(10)
    print node.getData()
    print parent.getData()
    
    
    