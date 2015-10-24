import unittest
from TestObject import TestObject
from pyQuery.PyQuery import PyQuery

class Query_First_Tests(unittest.TestCase):
    def setUp(self):
        self.test_data_primitives = [1,2,3,4,5,6,7,8]
        self.test_data_objects = []

        self.test_data_first_object = TestObject("Fry", "Value", 1)

        self.test_data_objects.append(self.test_data_first_object)
        self.test_data_objects.append(TestObject("Fry1", "Value2", 2))
        self.test_data_objects.append(TestObject("Fry2", "Value3", 3))

    def test_first_primitive(self):
        first = PyQuery(self.test_data_primitives).first()
        self.assertEqual(first, 1)

    def test_first_primitive_predicate(self):
        first = PyQuery(self.test_data_primitives).first(lambda n: n > 3)
        self.assertEqual(first, 4)

    @unittest.expectedFailure
    def test_first_primitive_predicate_fail(self):
        PyQuery(self.test_data_primitives).first(lambda n: n > 13)

    def test_first_objects(self):
        first = PyQuery(self.test_data_objects).first()
        self.assertEqual(first.ID, 1)

    def test_first_objects_predicate(self):
        first = PyQuery(self.test_data_objects).first(lambda n: n.Name == "Fry2")
        self.assertEqual(first.ID, 3)

    def test_first_objects_predicate_reference(self):
        first = PyQuery(self.test_data_objects).first(lambda n: n == self.test_data_first_object)
        self.assertEqual(first.ID, 1)

    def test_first_objects_multiple_predicate(self):
        first = PyQuery(self.test_data_objects).first(lambda n: n.Name == "Fry2" and n.ID == 3)
        self.assertEqual(first.ID, 3)

    @unittest.expectedFailure
    def test_first_objects_predicate(self):
        PyQuery(self.test_data_objects).first(lambda n: n.Name == "Fry5")

if __name__ == '__main__':
    unittest.main()