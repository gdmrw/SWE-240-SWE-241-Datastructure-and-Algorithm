########################################## BST part ##################################################
class BitTreeNode:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None

class BST:
    def __init__(self,li):
        self.root = None
        self.oplist = []
        if li:
            for val in li:
                self.insert_no_rec(val)

    def insert_no_rec(self,val):
        p = self.root
        if not p:           # empty tree
            self.root = BitTreeNode(val)
            return
        while True:                     # loop searching position
            if val < p.data:
                if p.lchild:            # have left move forward
                    p = p.lchild
                else:               # no left child add node
                    p.lchild = BitTreeNode(val)
                    p.lchild.parent = p
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BitTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return

    def in_order(self, root):   # in order traversal
        if root:
            self.in_order(root.lchild)
            self.oplist.append(root.data)
            # print(root.data,end=',')
            self.in_order(root.rchild)
########################################## BST part end ##############################################


########################################## heap part ##################################################
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class HeapBuilder:
    def __init__(self, values):
        self.values = values
        self.size = len(values)

    def _max_heapify(self, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        # not
        if left < self.size and self.values[largest] < self.values[left]:   # decide if swap needed and who will be swap
            largest = left
        if right < self.size and self.values[largest] < self.values[right]:
            largest = right

        if largest != i:   # swap occur when swap needed
            self.values[i], self.values[largest] = self.values[largest], self.values[i]
            self._max_heapify(largest)  # make sure  subtree with the root at largest also satisfies the max-heap property

    def _min_heapify(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < self.size and self.values[smallest] > self.values[left]:
            smallest = left
        if right < self.size and self.values[smallest] > self.values[right]:
            smallest = right

        if smallest != i:
            self.values[i], self.values[smallest] = self.values[smallest], self.values[i]
            self._min_heapify(smallest)

    def createHeap(self, heap_type):
        if heap_type == 'max':
            for i in range(self.size // 2 - 1, -1, -1):   # last non-leaf node index decresing order
                self._max_heapify(i)
        elif heap_type == 'min':
            for i in range(self.size // 2 - 1, -1, -1):   #
                self._min_heapify(i)

        return self.build_tree(0)

    def build_tree(self, i):
        if i >= self.size:
            return None
        node = Node(self.values[i])
        node.left = self.build_tree(2 * i + 1)
        node.right = self.build_tree(2 * i + 2)
        return node

    def createMaxHeap(self):
        return self.createHeap('max')

    def createMinHeap(self):
        return self.createHeap('min')

# Helper function to print the heap
def print_heap(heap):
    print(heap.values)

class BSTToHeapTransformer:
    def bst_to_min_heap(self,data):
        bst = BST(data)
        bst.in_order(bst.root)
        heap_builder = HeapBuilder(bst.oplist)
        print("bst to min heap result:")
        heap_builder.build_tree(bst.oplist[0])  # build tree directly
        print_heap(heap_builder)

    def bst_to_max_heap(self,data):
        bst = BST(data)
        bst.in_order(bst.root)
        heap_builder = HeapBuilder(data)
        heap_builder.createMaxHeap()
        print("bst to max heap result:")
        print_heap(heap_builder)






# Test cases
values = [1,3,6,5,9,8]
heap_builder = HeapBuilder(values)

print("Max Heap:")
max_heap = heap_builder.createMaxHeap()
print_heap(heap_builder)  # This will print the list representing the max heap

print("\nMin Heap:")
min_heap = heap_builder.createMinHeap()
print_heap(heap_builder)  # This will print the list representing the min heap


btm = BSTToHeapTransformer()
btm.bst_to_min_heap([2,3,6,9,7])
btm.bst_to_max_heap([2,3,6,9,7])



