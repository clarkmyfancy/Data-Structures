import unittest
from SinglyLinkedList import SinglyLinkedList
from SinglyLinkedList import Node

class TestSinglyLinkedList(unittest.TestCase):

    def setUp(self):
	    self.List = SinglyLinkedList()

    def tearDown(self):
	    del self.List

    def test_WhenAddedZeroItems_ListIsEmpty(self):
        self.assertEqual(0, self.List.count())

    def test_AfterPush1Node_ListHas1Node(self):
        n = Node()
        self.List.push(n)
        self.assertEqual(1, self.List.count())
    
    def test_AfterPush2Nodes_ListHas2Nodes(self):
        n1 = Node()
        n2 = Node()
        self.List.push(n1)
        self.List.push(n2)
        self.assertEqual(2, self.List.count())

    def test_After1PushAnd1Pop_ListIsEmpty(self):
        n = Node()
        self.List.push(n)
        self.List.pop()
        self.assertEqual(0, self.List.count())

    def test_AfterAttemptToPopFromEmtpyArray_ListRemainsEmpty(self):
        self.List.pop()
        self.assertEqual(0, self.List.count())

    def test_AfterPush1Node_PrintsPrettily(self):
        n = Node(15)
        self.List.push(n)
        self.assertEqual("|15| ~", self.List.pretty_print())

    def test_AfterPush2Nodes_PrintsPrettily(self):
        n0 = Node(12342342)
        n1 = Node(-123)
        self.List.push(n0)
        self.List.push(n1)
        self.assertEqual("|12342342| -> |-123| ~", self.List.pretty_print())

if (__name__ == '__main__'):
	unittest.main()