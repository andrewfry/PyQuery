import unittest
from TestObject import TestObject
from PyQuery.PyQuery import PyQuery


class Query_Contains_Tests(unittest.TestCase):
    def setUp(self):
        self.test_data_primitives = [1, 2, 2, 4, 5, 6, 7, 8, 9, 10]
        self.test_data_objects = []

        self.test_data_first_object = TestObject("Fry", "Value", 1)

        self.test_data_objects.append(self.test_data_first_object)
        self.test_data_objects.append(TestObject("Fry1", "Value2", 2))
        self.test_data_objects.append(TestObject("Fry2", "Value3", 3))

    def test_contains_primitive(self):
        result = PyQuery(self.test_data_primitives).contains(2)

        self.assertEqual(result, True)

    def test_contains_primitive_false(self):
        result = PyQuery(self.test_data_primitives).contains(156)

        self.assertEqual(result, False)

    # TODO investigate this error
    def test_contains_objects(self):
        result = PyQuery(self.test_contains_objects).where(lambda n: n.ID == self.test_data_first_object.ID)

        result = PyQuery(self.test_contains_objects).contains(self.test_data_first_object)

        self.assertEqual(result, True)

    def test_contains_objects_false(self):
        result = PyQuery(self.test_contains_objects).skip(1).contains(self.test_data_first_object)

        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
