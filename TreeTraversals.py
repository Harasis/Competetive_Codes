class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self,root):
        self.root = Node(root)
        
    def recursive_preorder(self,root):
        if root is None:
            return []
        return [root.val]+self.recursive_preorder(root.left)+self.recursive_preorder(root.right)
    
    def iterative_preorder(self,root):
        if root is None:
            return []
        stack = [root]
        result=[]
        while stack!=[]:
            root = stack.pop()
            result.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
        return result
    
    def recursive_inorder(self,root):
        if root is None:
            return []
        return self.recursive_inorder(root.left)+ [root.val]+self.recursive_inorder(root.right)
    
    def iterative_inorder(self,root):
        stack = []
        result = []
        while root is not None or stack !=[]:
            while root is not None:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            result.append(root.val)
            root = root.right
                
        return result
    
    def recursive_postorder(self,root):
        if root is None:
            return []
        return self.recursive_postorder(root.left)+self.recursive_postorder(root.right)+[root.val]
    
    
    def iterative_postorder(self,root):
        stack = []
        result = []
        while root is not None or stack!=[]:
            while root is not None:
                stack.append(root)
                root = root.left
                
            temp = stack[-1].right
            if temp is not None:
                root = temp
            else:
                temp = stack.pop()
                result.append(temp.val)
                while stack!=[] and temp == stack[-1].right:
                    temp = stack.pop()
                    result.append(temp.val)
        return result
    
    
    def levelorder(self,root):
        if root is None:
            return []
        
        queue = [root]
        next_queue = []
        level = []
        result = []
        
        while queue != []:
            for root in queue:
                level.append(root.val)
                if root.left is not None:
                    next_queue.append(root.left)
                if root.right is not None:
                    next_queue.append(root.right)
            result.append(level)
            level = []
            queue = next_queue
            next_queue = []
        return result
    
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.recursive_preorder(tree.root))
print(tree.iterative_preorder(tree.root))

print(tree.recursive_inorder(tree.root))
print(tree.iterative_inorder(tree.root))

print(tree.recursive_postorder(tree.root))
print(tree.iterative_postorder(tree.root))

print(tree.levelorder(tree.root))











