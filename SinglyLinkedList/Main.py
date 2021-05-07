from SinglyLinkedList import SinglyLinkedList
from Node import Node

def main():
    x = SinglyLinkedList()
    n0 = Node(123542634263)
    n1 = Node(-1)
    n2 = Node(0)
    n3 = Node()
    n4 = Node(312.2134)
    
    x.push(n0)
    x.push(n1)
    x.push(n2)
    x.push(n3)
    x.push(n4)

    print(x.pretty_print())



if __name__ == "__main__":
    main()