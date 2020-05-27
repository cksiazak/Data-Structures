"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if current node's value is more than passed in value
        if self.value > value:
            # check if left tree has a value
            if self.left is None:
                # if not, create a node with the value
                self.left = BSTNode(value)
            else:
                # if it does have a value
                # insert it into that node
                self.left.insert(value)

        # if self.value is less than or equal to the passed in value
        if self.value <= value:
            # attach to the right
            # check if right has a value
            if self.right is None:
                # if not, create a node
                self.right = BSTNode(value)
            else:
                # if it does have a value - insert the value into that node
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if self.value is equal to target
        if self.value == target:
            # return true
            return True
        
        # if self.value is more than target
        if self.value > target:
            # check left node, which if it is None - reject
            if self.left is None:
                return False
            # otherwise, check that left node
            else:
                return self.left.contains(target)
        
        # if self.value is less than target
        if self.value < target:
            # check the right branch, and it if is None - reject
            if self.right is None:
                return False
            else:
                # otherwise, check that right node
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # as we're searching for the max, we'll check the right side of the tree
        # check if right branch exists
        if self.right is None:
            # if it doesn't, return current value
            return self.value
        else:
            # if the right branch does exist
            # run this method again on that branch
            return self.right.get_max()
            

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
