
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data
    
def insert(temp,data):
   que = []
   que.append(temp)
   while (len(que)):
      temp = que[0]
      que.pop(0)
      if (not temp.left):
         temp.left = Node(data)
         break
      else:
         que.append(temp.left)
      if (not temp.right):
         temp.right = Node(data)
         break
      else:
         que.append(temp.right)

def make_tree(data_list):
    Tree = Node(data_list[0])
    if len(data_list) > 1:
        for val in data_list[1:]:
            insert(Tree, val )
    return Tree

def pre_order(Tree):
    if Tree:
        if Tree.val != None:
            print(Tree.val)
        pre_order(Tree.left)
        pre_order(Tree.right)

def in_order(Tree):
    if Tree:
        in_order(Tree.left)
        if Tree.val != None:
            print(Tree.val)
        in_order(Tree.right)

def post_order(Tree):
    if Tree:
        post_order(Tree.left)
        post_order(Tree.right)
        if Tree.val != None:
            print(Tree.val)

Tree = make_tree([10,5,15,2,7,None,20])

pre_order(Tree)
print("#"*10)
in_order(Tree)
print("#"*10)
post_order(Tree)