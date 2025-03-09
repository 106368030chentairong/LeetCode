class TreeNode(object):
    def __init__(self, val=0,left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

def list2treenode(node_list):
    if not node_list :
        return None
    
    nodes = []
    for val in node_list:
        if val != None:
            nodes.append(TreeNode(val))
        else:
            nodes.append(None)
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
                node.right = kids.pop()
    return root


node_list = [1,2,3,4,5,6,7]
root_node = list2treenode(node_list)

def preorder(treenode):
    if not treenode:
        return []
    
    resulst = []
    stack = [treenode]

    while stack:
        node = stack.pop()
        if node :
            resulst.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return resulst

print("pre-order ",preorder(root_node))

def preorder2(treenode):
    if not treenode:
        return []
    return [treenode.val]+preorder2(treenode.left)+preorder2(treenode.right)

print("pre-order2 ",preorder2(root_node))

def inorder(treenode):
    if not treenode:
        return []
    return inorder(treenode.left)+[treenode.val]+inorder(treenode.right)

print("in-order ",inorder(root_node))

def post_order(treenode):
    if not treenode:
        return []
    return post_order(treenode.left)+post_order(treenode.right)+[treenode.val]
print("post-order ",post_order(root_node))