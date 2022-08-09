class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def insert(temp,data):
    que = []
    que.append(temp)
    while (len(que)):
        temp = que[0]
        que.pop(0)
        if (not temp.left):
            temp.left = TreeNode(data)
            break
        else:
            que.append(temp.left)
        if (not temp.right):
            temp.right = TreeNode(data)
            break
        else:
            que.append(temp.right)

def make_tree(elements):
    Tree = TreeNode(elements[0])
    for element in elements[1:]:
        insert(Tree, element)
    return Tree

# inorder tree
#          10
#       5     15
#     2   7     20

root = make_tree([10,5,15,2,7,None,20])