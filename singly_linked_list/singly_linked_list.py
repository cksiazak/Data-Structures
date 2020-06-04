class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def add_to_tail(self, value):
        node = ListNode(value)
        self.length += 1
        # if head doesn't exist
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            # if it does exist
            self.tail.next = node
            self.tail = node

    def contains(self, value):
        # get current node
        current_node = self.head
        # as long as current node exists
        while current_node is not None:
            # check the current node's value witht he value passed in
            if current_node.value == value:
                # if found, return true
                return True
            # set current node to next to iterate through all nodes
            current_node = current_node.next
        # if not found, reject
        return False

    def remove_head(self):
        # if self.head exists
        if self.head is not None:
            # set current node to the head
            current_node = self.head
            # check if self.head is self.tail
            if self.head == self.tail:
                # if so, set both to None
                self.head = None
                self.tail = None
                # return current_node's value
                return current_node.value
            # otherwise set self.head to the next node
            self.head = self.head.next
            # delete current node
            current_node.next = None
            # return the value
            return current_node.value

    def get_max(self):
        if self.head is None:
            return None
            
        if self.head == self.tail:
            return self.head.value

        # set current node to self.head
        current_node = self.head
        # establish an incremental value
        increment = 0
        # track the max value
        max_value = 0

        # use increment to mark our index in the length of list
        while increment < self.length:
            # add 1 to our increment
            increment += 1
            # if max_value is less than the current node's value
            if max_value < current_node.value:
                # set the max value to it
                max_value = current_node.value
            # then set current node to the next node and repeat
            current_node = current_node.next

        # once all nodes have been checked, return the max
        return max_value
