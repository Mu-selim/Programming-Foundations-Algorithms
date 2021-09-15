

# Node class
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_item(self):
        return self.value
    
    def set_item(self, value):
        self.value = value

    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next


# Linkedlist class
class Linkedlist(object):
    def __init__(self, head = None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, value):
        item = self.head
        while item != None:
            if item.get_item() == value:
                return item
            else:
                item = item.get_next()
        return None

    def delete_item_index(self, index):
        if index > self.count-1:
            return 

        if index == 0:
            self.head = self.head.get_next()
        else:
            temp = 0
            node = self.head
            while temp < index-1:
                node = node.get_next()
                temp += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def dump_list(self):
        tempnode = self.head
        while tempnode != None:
            print("Node :", tempnode.get_item())
            tempnode = tempnode.get_next()

# Creating a Linkedlist
linked_list = Linkedlist()
linked_list.insert(10)
linked_list.insert(39)
linked_list.insert(12)
linked_list.insert(15)
linked_list.insert(22)
linked_list.insert(20)
linked_list.dump_list()
print()

# check the Linkedlist items
print("Number of items =", linked_list.get_count())
print("Serching for an item:", linked_list.find(12))
print("Serching for an item:", linked_list.find(25))
print()

# delete an item
linked_list.delete_item_index(4)
print("Number of items =", linked_list.get_count())
print("Serching for an item:", linked_list.find(39))
print("Serching for an item:", linked_list.find(12))
print()
linked_list.dump_list()