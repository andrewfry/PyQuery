import unittest
from TestObject import TestObject
from PyQuery.PyQuery import PyQuery


class QueryTakeTests(unittest.TestCase):
    def setUp(self):
        self.test_data_primitives = [1, 2, 2, 4, 5, 6, 7, 8, 9, 10]
        self.test_data_objects = []

        self.test_data_first_object = TestObject("Fry", "Value", 1)

        self.test_data_objects.append(self.test_data_first_object)
        self.test_data_objects.append(TestObject("Fry1", "Value2", 2))
        self.test_data_objects.append(TestObject("Fry2", "Value3", 3))

    def test_take(self):
        result = PyQuery(self.test_data_primitives).take(2)

        self.assertTrue(len(result) == 2)

    def test_chained_take(self):
        result = PyQuery(self.test_data_primitives) \
            .where(lambda n: n > 2).take(3) \
            .where(lambda n: n > 4).take(2).to_list()

        self.assertTrue(len(result) == 2)

    def test_take_objects(self):
        result = PyQuery(self.test_data_objects).take(2)

        self.assertTrue(len(result) == 2)

if __name__ == '__main__':
    unittest.main()
