class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
 
 
def in_order(tree):
    stack=[tree]
    present= tree
    while len(stack) > 0:
        if present:
            while present.left:
                stack.append(present.left)
                present = present.left
        pop_node = stack.pop()
        present = None
        if pop_node:
            print (pop_node.value)
            present = pop_node.right
            stack.append(present)



 
a=BinTreeNode(1)
b=BinTreeNode(2)
c=BinTreeNode(3)
d=BinTreeNode(4)

b.right = d
a.left=b
a.right=c

in_order(a)
