import unittest
from TestObject import TestObject
from PyQuery.PyQuery import PyQuery


class QuerySingleTests(unittest.TestCase):
    def setUp(self):
        self.test_data_primitives = [1, 2, 2, 4, 5, 6, 7, 8]
        self.test_data_objects = []

        self.test_data_first_object = TestObject("Fry", "Value", 1)

        self.test_data_objects.append(self.test_data_first_object)
        self.test_data_objects.append(TestObject("Fry1", "Value2", 2))
        self.test_data_objects.append(TestObject("Fry2", "Value3", 3))

    @unittest.expectedFailure
    def test_single_primitive_fail(self):
        PyQuery(self.test_data_primitives).single()

    @unittest.expectedFailure
    def test_single_primitive_lambda_fail(self):
        PyQuery(self.test_data_primitives).single(lambda n: n == 2)

    def test_single_primitive(self):
        one_in_list = [1]
        single_return = PyQuery(one_in_list).single()
        self.assertTrue(1 == single_return)

    def test_single_primitive_lambda(self):
        single_return = PyQuery(self.test_data_primitives).single(lambda n: n == 4)
        self.assertTrue(4 == single_return)

if __name__ == '__main__':
    unittest.main()
