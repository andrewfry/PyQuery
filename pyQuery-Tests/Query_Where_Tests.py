import unittest
from TestObject import TestObject
from PyQuery.PyQuery import PyQuery


class Query_Where_Tests(unittest.TestCase):
    def setUp(self):
        self.test_data_primitives = [1, 2, 2, 4, 5, 6, 7, 8, 9, 10]
        self.test_data_objects = []

        self.test_data_first_object = TestObject("Fry", "Value", 1)

        self.test_data_objects.append(self.test_data_first_object)
        self.test_data_objects.append(TestObject("Fry1", "Value2", 2))
        self.test_data_objects.append(TestObject("Fry2", "Value3", 3))

    def test_where_single(self):
        result = PyQuery(self.test_data_primitives).where(lambda n: n == 6).single()
        self.assertEqual(result, 6)

    def test_large_list_where(self):
        test_list = []

        for x in xrange(0, 200000):
            test_list.append(x)

        test_list = PyQuery(test_list).where(lambda n: n == 19999).single()

        self.assertEqual(test_list, 19999)

    def test_chained_where_statements(self):
        test_list = PyQuery(self.test_data_primitives).where(lambda n: n > 2).where(lambda n: n < 6).to_list()

        self.assertEqual(len(test_list), 2)


if __name__ == '__main__':
    unittest.main()
