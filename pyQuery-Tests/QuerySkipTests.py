import unittest
from TestObject import TestObject
from PyQuery.PyQuery import PyQuery


class QuerySkipTests(unittest.TestCase):
    def setUp(self):
        self.test_data_primitives = [1, 2, 2, 4, 5, 6, 7, 8, 9, 10]
        self.test_data_objects = []

        self.test_data_first_object = TestObject("Fry", "Value", 1)

        self.test_data_objects.append(self.test_data_first_object)
        self.test_data_objects.append(TestObject("Fry1", "Value2", 2))
        self.test_data_objects.append(TestObject("Fry2", "Value3", 3))

    def test_skip_chained(self):
        result = PyQuery(self.test_data_primitives).skip(2).skip(2).to_list()

        self.self.assertTrue(len(result) == 6)

    def test_skip(self):
        result = PyQuery(self.test_data_objects).skip(1).to_list()
        first = PyQuery(result).first()
        last = PyQuery(result).last()

        self.self.assertTrue(len(result) == 2)
        self.self.assertTrue(first.ID == 2)
        self.self.assertTrue(last.ID == 3)

if __name__ == '__main__':
    unittest.main()
