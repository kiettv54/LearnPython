class node():
    def __init__(self,data=None):
        self.data=data
        self.next = None
class Linhked_List():
    def __init__(self):
        self.head = node()
    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next !=None:
            cur = cur.next
        cur.next = new_node
    def lenght(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)
my_list = Linhked_List()
my_list.display()
my_list.append([1,2,3,4])
my_list.display()
