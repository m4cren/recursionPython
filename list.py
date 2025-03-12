class Node:
     def __init__(self, data):
          self.data = data
          self.next = None
          
class LinkedList:
     def __init__(self):
          self.head = None

     def insert(self, data):
          new_node = Node(data)

          if not self.head:
               self.head = new_node
               return
          
          last = self.head

          while last.next:
               last = last.next

          
          last.next = new_node

     def print_recursion(self, node):
          if node is None:
               return
          
          print(node.data)

          self.print_recursion(node.next)

     def start_recursion_traversal(self):
          self.print_recursion(self.head)

list = LinkedList()

listKO = ['Apple', 'Banana', 'Mika', 'Dates', 'Carabao', 'Birthday']

for i in range(len(listKO)):
     list.insert(listKO[i])


print('Linked List')
list.start_recursion_traversal()