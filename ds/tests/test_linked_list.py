import unittest

from data_structures.linked_lists import Node
from data_structures.linked_lists import UnorderedList


class TestNode(unittest.TestCase):

    def setUp(self):
        self.input_list = [0, -4, 10, None, 'one']

    def test_object_creation(self):
        node_list = [Node(item)for item in self.input_list]
        for node in node_list:
            self.assertIsNotNone(node)

    def test_data_and_next(self):
        node_list = [Node(item)for item in self.input_list]
        for node, inp in zip(node_list, self.input_list):
            self.assertEqual(node.get_data(), inp)
            self.assertIsNone(node.get_next())

    def test_setting_next(self):
        node = Node([])
        node.set_next(Node(3))
        self.assertEqual(node.get_next().get_data(), 3)


class TestLinkedListCreation(unittest.TestCase):

    def test_list_creation(self):
        llist = UnorderedList()
        self.assertIsNotNone(llist)


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.llist = UnorderedList()
        self.input_list = [0, -4, 10, None, 'one']


    def populate_list(self):
        for item in self.input_list:
            self.llist.append(item)


    def node_spitter(self):
        node = self.llist.head
        while node:
            yield node
            node = node.get_next()


    def test_list_head(self):
        self.assertIsNone(self.llist.head)
        self.assertTrue(self.llist.is_empty())


    def test_add_and_length(self):
        self.populate_list()

        self.assertEqual(self.llist.length(), len(self.input_list))

        for i, j in zip(self.node_spitter(), self.input_list):
            self.assertEqual(i.get_data(), j)


    def test_index(self):
        self.populate_list()
        self.assertEqual(self.llist.index(0), 0)
        self.assertEqual(self.llist.index(-4), 1)
        self.assertEqual(self.llist.index(None), 3)
        self.assertEqual(self.llist.index('one'), 4)
        

    def test_return_last_node(self):
        self.assertIsNone(self.llist._return_last_node())
        self.populate_list()
        self.assertEqual(self.llist._return_last_node().get_data(), self.input_list[-1])


    def test_insert(self):
        self.populate_list()
        
        self.assertRaises(ValueError, self.llist.insert, -1, 5)
        self.assertRaises(ValueError, self.llist.insert, len(self.input_list)+2, 5)

        self.llist.insert(0, 'zeroth')
        result = [n.get_data() for n in self.llist.get_node_generator()]
        self.assertEqual(self.llist.head.get_data(), 'zeroth')
        self.assertEqual(result, ['zeroth', 0, -4, 10, None, 'one'])

        self.llist.insert(1, 'first')
        result = [n.get_data() for n in self.llist.get_node_generator()]
        self.assertEqual(result, ['zeroth', 'first', 0, -4, 10, None, 'one'])

        self.llist.insert(6, 'sixth')
        result = [n.get_data() for n in self.llist.get_node_generator()]
        self.assertEqual(result, ['zeroth', 'first', 0, -4, 10, None, 'sixth', 'one'])
        
        self.llist.insert(8, 'last')
        result = [n.get_data() for n in self.llist.get_node_generator()]
        self.assertEqual(result, ['zeroth', 'first', 0, -4, 10, None, 'sixth', 'one', 'last'])


    def test_pop(self):
        self.assertRaises(Exception, self.llist.pop)

        self.populate_list()

        result = []
        while not self.llist.is_empty():
            item = self.llist.pop()
            result.append(item)
            
        self.assertEqual(result, list(reversed(self.input_list)))


    def test_search(self):
        self.populate_list()

        self.assertTrue(self.llist.search(10))
        self.assertTrue(self.llist.search(None))
        self.assertFalse(self.llist.search(123))


    def test_remove(self):
        self.populate_list()

        self.llist.remove(10)
        result = [n.get_data() for n in self.llist.get_node_generator()]
        self.input_list.remove(10)
        self.assertEqual(result, self.input_list)

        self.llist.remove(None)
        result = [n.get_data() for n in self.llist.get_node_generator()]
        self.input_list.remove(None)
        self.assertEqual(result, self.input_list)

        self.llist.remove(0)
        result = [x.get_data() for x in self.llist.get_node_generator()]
        self.input_list.remove(0)
        self.assertEqual(result, self.input_list)


if __name__ == '__main__':
    unittest.main()
