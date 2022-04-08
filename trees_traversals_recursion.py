#binary search trees, traversals and recursion
# you are tasked with developing a fast in-memory data structure to manage profile information (username, name and email) for 100 million users. It should allow the following operations to be performed:

# Insert: Loop through the list and add the new user at a position that keeps the list sorted.
# Find: Loop through the list and find the user object with the username matching the query.
# Update: Loop through the list, find the user object matching the query and update the details
# List: Return the list of user objects.

class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
    
    def __repr__(self):
        return f"\nUser(Username={self.username}, name={self.name}, email={self.email})\n"
    
    def __str__(self):
        return self.__repr__()

Hans = User('hans', 'Hans Folkesson', 'hans.hans@gmail.com')
Jans = User('jans', 'Jans Folkesson', 'jans.jans@gmail.com')
Alex = User('alex', 'Alex Alexander', 'alex.alex@gmail.com')
Axel = User('axel', 'Axel Alexander', 'axel.axel@gmail.com')
Jack = User('jack', 'Jack McPackage', 'jack.jack@gmail.com')
Wack = User('wack', 'Wack MyPackage', 'wack.wack@gmail.com')

class UserDatabase:
    def __init__(self):
        self.users = []
    
    def insert(self, user):
        i = 0
        while i < len(self.users):
            if user.username < self.users[i].username:
                break
            i += 1
        self.users.insert(i, user)
    
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
    
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email
        
    def list_all(self):
        return self.users

# database = UserDatabase()
# database.insert(Hans)
# database.insert(Jans)
# database.insert(Alex)
# database.insert(Axel)
# database.insert(Jack)
# database.insert(Wack)

# print(database.users)

# user = database.find('wack')
# print(user)

# database.update(User('jack', 'Jacques Package','tiny.pack@gmail.com'))
# print(database.list_all())

#---------------------------------------------------------------------------------------------------------------------------------#

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


    def traverse_inorder(self):
        if self is None:
            return []
        return TreeNode.traverse_inorder(self.left) + [self.key] + TreeNode.traverse_inorder(self.right)
    
    def traverse_preorder(self):
        if self is None:
            return []
        return [self.key] + TreeNode.traverse_preorder(self.left) + TreeNode.traverse_preorder(self.right)

    def traverse_postorder(self):
        if self is None:
            return []
        return TreeNode.traverse_postorder(self.left) + TreeNode.traverse_postorder(self.right) + [self.key]

    def tree_height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.tree_height(self.right), TreeNode.tree_height(self.left))

    def tree_size(self):
        if self is None:
            return 0
        return 1 + TreeNode.tree_size(self.right) + TreeNode.tree_size(self.left)

    def display_keys(self, space='\t', level=0):
        # if the node is empty
        if self is None:
            print(space*level + '∅')
            return
        # if the node is a leaf
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return
        # if the node has children
        TreeNode.display_keys(self.left, space, level+1)
        print(space*level + str(self.key))
        TreeNode.display_keys(self.right, space, level+1)

    # WRITE A FUNCTION TO CHECK IF A BINARY TREE IS A BINARY SEARCH TREE
    def is_bst(self):# node needs to be compared with its children. should be greater than right child and less than left child
                     # compartison should be made once both the left and right child of a node have been accessed
                     # WRITE A TEST METHOD TO SEE IF AND HOW YOU CAN UNPACK A NODE


    @staticmethod
    def parse_tuple(data):
            if isinstance(data, tuple) and len(data) == 3:
                node = TreeNode(data[1])
                node.left = TreeNode.parse_tuple(data[0])
                node.right = TreeNode.parse_tuple(data[2])
            elif data is None:
                node = None
            else:
                node = TreeNode(data)
            return node
    
    

result = TreeNode.parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
print(result.left.key)

in_order = TreeNode.traverse_inorder(result)
print(in_order)
pre_order = TreeNode.traverse_preorder(result)
print(pre_order)
post_order = TreeNode.traverse_postorder(result)
print(post_order)

height = TreeNode.tree_height(result)
print(height)
size = TreeNode.tree_size(result)
print(size)

keys = TreeNode.display_keys(result)
print(keys)

# def traverse_inorder(node):
#     if node is None:
#         return []
#     return traverse_inorder(node.left) + [node.key] + traverse_inorder(node.right)

# in_order = traverse_inorder(result)
# print(in_order)

# def traverse_preorder(node):
#     if node is None:
#         return []
#     return [node.key] + traverse_preorder(node.left) + traverse_preorder(node.right)

# pre_order = traverse_preorder(result)
# print(pre_order)

# def traverse_postorder(node):# left to right traversal, root nodes are added right after their children
#     if node is None:
#         return []
#     return traverse_postorder(node.left) + traverse_postorder(node.right) + [node.key]

# post_order = traverse_postorder(result)
# print(post_order)

# def tree_height(node):
#     if node is None:
#         return 0
#     return 1 + max(tree_height(node.right), tree_height(node.left))

# height = tree_height(result)
# print(height)

# def tree_size(node):
#     if node is None:
#         return 0
#     return 1 + tree_size(node.left) + tree_size(node.right)

# size = tree_size(result)
# print(size)