from collections import deque
import sys
class BitTreeNode:
    def __init__(self, student_number, last_name, department, program, year):
        self.student_number = student_number
        self.last_name = last_name.upper()  # Make case-insensitive by converting to upper case
        self.department = department
        self.program = program
        self.year = year
        self.lchild = None
        self.rchild = None
        self.parent = None

class BST:
    def __init__(self):
        self.root = None

    # def insert(self,node,val):
    #     if not node:
    #         node = BitTreeNode(val)
    #     elif val < node.data:
    #         node.lchild = self.insert(node.lchild,val)
    #         node.lchild.parent = node
    #     elif val > node.data:
    #         node.rchild = self.insert(node.rchild, val)
    #         node.rchild.parent = node
    #     return node

    def insert_no_rec(self, student_number, last_name, department, program, year):
        new_node = BitTreeNode(student_number, last_name, department, program, year)
        p = self.root
        if not p:           # empty tree
            self.root = new_node
            return
        while True:                     # loop searching position
            if new_node.last_name < p.last_name:        # Use the last name for comparison
                if p.lchild:            # have left move forward
                    p = p.lchild
                else:               # no left child add node
                    p.lchild = new_node
                    p.lchild.parent = p
            elif new_node.last_name > p.last_name:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = new_node
                    p.rchild.parent = p
                    return
            else:
                return

    # def search(self,node, val):
    #     if not node:
    #         return None
    #     if node.data < val:
    #         return self.search(node.rchild, val)
    #     elif node.data > val:
    #         return self.search(node.lchild, val)
    #     else:
    #         return node

    def search_no_rec(self, current_last_name):
        p = self.root
        current_last_name = current_last_name.upper() # Case-insensitive search
        while p:
            if p.last_name < current_last_name:
                p = p.rchild   #target val less than current node val, put right forward
            elif p.last_name > current_last_name:
                p = p.lchild    #target val more than current node val, put left forward
            else:
                return p        # find the target and return the node
        return None             # not find any target return None

    def delete(self,current_last_name):
        if self.root: # make sure this is not empty tree
            node = self.search_no_rec(current_last_name)
            if not node:
                # no need to delete if there is no node exist
                return False
            if not node.lchild and not node.rchild:
                self.__delete_node_leaf(node)
            elif not node.rchild:
                # no rchild mean must have left child
                self.__delete_node_with_only_left_child(node)
            elif not node.lchild:
                # no lchild mean must have right child
                self.__delete_node_with_only_right_child(node)
            else:
                # finish the status when node have both 2 child
                # if you want to delete the child have 2 child,
                # replace the current node with the right smallest child from its right tree
                min_node = node.rchild
                while min_node.rchild:
                    if min_node.lchild:   # check if the min_node still have any left child
                        min_node = min_node.lchild  # if yes move forward
                    else:
                        break                       # if no break
                node.data = min_node.data
                # delete min node
                if min_node.rchild:
                    # check if its min node have right child,
                    # since min node is the end of left child,
                    # no need to consider left child situation
                    self.__delete_node_with_only_right_child(min_node)
                else:
                    # leaf
                    self.__delete_node_leaf(min_node)
        return False # this false return is for empty tree

    def __delete_node_leaf(self, node):
        """
        only use when delete node is leaf(no child)
        :param node:
        :return:
        """
        if not node.parent:  # only one node in tree node are root
            self.root = None
        if node == node.parent.lchild:  #check left or right child
            node.parent.lchild = None
            # node.parent = None
        else:
            node.parent.rchild = None

    def __delete_node_with_only_left_child(self, node):
        if not node.parent:
            # if node is root
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:
            # if node on the left side of its parent child
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
            node.lchild = None
        else:
            # if node on the right side of its parent child
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __delete_node_with_only_right_child(self, node):
        if not node.parent:
            # if node is root
            self.root = node.rchild
            node.rchild.parent = None
        elif node == node.parent.lchild:
            # if node on the left side of its parent child
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:
            # if node on the right side of its parent child
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    # def pre_order(self,root):  # pre order traversal
    #     if root:
    #         print(root.data,end=',')
    #         self.pre_order(root.lchild)
    #         self.pre_order(root.rchild)

    def in_order(self, root, file):   # in order traversal
            if root:
                self.in_order(root.lchild,file)
                file.write(f"last name:{root.last_name},  student id: {root.student_number},  department:{root.department},  program:{root.program},  year:{root.year}\n")
                self.in_order(root.rchild,file)

    def level_order(self,root, file):    # level order traversal
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            node = queue.popleft()
            file.write(f"last name:{node.last_name},  student id: {node.student_number},  department:{node.department},  program:{node.program},  year:{node.year}\n")
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)

    def process_file(self):
        with open("tree-input.txt", 'r') as file:
            for line in file:
                op_code = line[0]
                student_number = line[1:8]
                last_name = line[8:33].strip()
                department = line[33:37]
                program = line[37:41]
                year = line[41]

                if op_code == 'I':
                    self.insert_no_rec(student_number, last_name, department, program, year)
                elif op_code == 'D':
                    self.delete(last_name)


bst = BST()
bst.process_file()

with open("tree-input.txt","a") as file:
    file.write("\n\n")
    file.write("below are output from BST in order traversal:\n")
    bst.in_order(bst.root,file)
    file.write("\n")
    file.write("below are output from BST level order traversal:\n")
    bst.level_order(bst.root,file)














