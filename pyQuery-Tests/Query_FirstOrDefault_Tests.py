import unittest
from TestObject import TestObject
from PyQuery.PyQuery import PyQuery


class Query_FirstOrDefault_Tests(unittest.TestCase):
    def setUp(self):
        self.test_data_primitives = [1, 2, 3, 4, 5, 6, 7, 8]
        self.test_data_objects = []

        self.test_data_first_or_default_object = TestObject("Fry", "Value", 1)

        self.test_data_objects.append(self.test_data_first_or_default_object)
        self.test_data_objects.append(TestObject("Fry1", "Value2", 2))
        self.test_data_objects.append(TestObject("Fry2", "Value3", 3))

    def test_first_or_default_primitive(self):
        first_or_default = PyQuery(self.test_data_primitives).first_or_default()
        self.assertEqual(first_or_default, 1)

    def test_first_or_default_primitive_predicate(self):
        first_or_default = PyQuery(self.test_data_primitives).first_or_default(lambda n: n > 3)
        self.assertEqual(first_or_default, 4)

    def test_first_or_default_primitive_predicate_none(self):
        first_or_default = PyQuery(self.test_data_primitives).first_or_default(lambda n: n > 13)
        self.assertEqual(first_or_default, None)

    def test_first_or_default_objects(self):
        first_or_default = PyQuery(self.test_data_objects).first_or_default()
        self.assertEqual(first_or_default.ID, 1)

    def test_first_or_default_objects_predicate(self):
        first_or_default = PyQuery(self.test_data_objects).first_or_default(lambda n: n.Name == "Fry2")
        self.assertEqual(first_or_default.ID, 3)

    def test_first_or_default_objects_predicate_reference(self):
        first_or_default = PyQuery(self.test_data_objects).first_or_default(lambda n:
                                                                            n == self.test_data_first_or_default_object)
        self.assertEqual(first_or_default.ID, 1)

    def test_first_or_default_objects_multiple_predicate(self):
        first_or_default = PyQuery(self.test_data_objects).first_or_default(lambda n: n.Name == "Fry2" and n.ID == 3)
        self.assertEqual(first_or_default.ID, 3)

    def test_first_or_default_objects_predicate(self):
        first_or_default = PyQuery(self.test_data_objects).first_or_default(lambda n: n.Name == "Fry5")
        self.assertEqual(first_or_default, None)


if __name__ == '__main__':
    unittest.main()
