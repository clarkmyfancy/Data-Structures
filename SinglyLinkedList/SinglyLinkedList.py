class SinglyLinkedList:

    def __init__(self, _head = None, _tail = None):
        self._head = _head
        self._tail = _tail

    def count(self):
        runner = self._head
        count = 0
        while(runner != None):
            count += 1
            runner = runner._next
        return count

    def push(self, node):
        if (self._head == None):
            self._head = node
            self._tail = node
        else:
            self._tail._next = node
            self._tail = node

    def pop(self):
        if (self._head == None):
            return
        else:    
            temp = self._head
            self._head = self._head._next
            temp._next = None
            del temp

    def pretty_print(self):
        runner = self._head
        legible_list = ""
        while (runner != None):
            if (runner._next == None):
                legible_list += ("|" + str(runner._value) + "|" + " ~")
            else:
                legible_list += ("|" + str(runner._value) + "|" + " -> ")
            runner = runner._next
        return legible_list