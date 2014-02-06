# -*- coding: utf-8 -*-

import sys

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


class Tree():
    
    def __init__(self):
        self.stack = Stack()
        
        self.lchild = ''
        self.data = ''
        self.rchild = ''



if __name__ == '__main__':
    tree = Tree()
