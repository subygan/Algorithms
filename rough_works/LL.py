class Node:
    def __init__(self, data=None):
        self.item = data
        self.ref = None
        self.pos = 11


class SLinkedList:
    def __init__(self):
        self.start_node = None
        self.pos = 0

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            print("<<<====>>")
            while n is not None:
                print("item  :",n.item, " position :", n.pos)
                n = n.ref

    def insert_at_start(self, data):

        new_node = Node(data)
        new_node.ref = self.start_node
        new_node.pos = self.pos+1
        self.start_node = new_node
        self.pos += 1


if __name__ == "__main__" :

    LL = SLinkedList()
    n = input()
    while n!="done":
        LL.insert_at_start(n)
        n = input()
    LL.traverse_list()