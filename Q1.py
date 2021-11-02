from typing import ClassVar


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = "Red"

class Tree:
    def __init__(self):
        self.root = None
    
    def RB_insertNode(self,root,node):
        if ( self.root == None ):
            self.root = node
        else:
            
            if ( root.data < node.data ):
                if ( root.right == None ):
                    node.parent = root
                    root.right = node
                else:
                    self.RB_insertNode(root.right,node)
            elif( root.data > node.data ):
                if ( root.left == None ):
                    node.parent = root
                    root.left = node
                else:
                    self.RB_insertNode(root.left,node)
    
    def left_rotate(self,x):
        y = Node()
        y = x.right
        x.right = y.left
        if ( y.left != None ):
            y.left.parent = x
        y.parent = x.parent
        if( x.parent == None):
            self.root = y
        else:
            if( x == x.parent.left ):
                x.parent.left = y
            else:
                x.parent.right = y
        y.left = x
        x.parent = y
                
    def right_rotate(self,x):
        y = Node()
        y = x.left
        x.left = y.right
        if ( y.right != None ):
            y.right.parent = x
        y.parent = x.parent
        if( x.parent == None):
            self.root = y
        else:
            if( x == x.parent.right):
                x.parent.right = y
            else:
                x.parent.left = y
        y.right = x
        x.parent = y