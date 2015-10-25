from Exceptions import SequenceError
from Exceptions import LookUpError


class PyQuery:
    def __init__(self, data_set):
        self.__data_set = data_set
        self.__predicates = []
        self.__skip = 0
        self.__take = None

    def where(self, predicate):
        self.__predicates.append(predicate)
        return self

    def contains(self, x):
        for item in self.get_from_predicates(True):
            if item == x:
                return True

        return False

    def any(self, predicate=lambda n: n):
        for item in self.get_from_predicates(True):
            if predicate(item):
                return True

        return False

    def single_or_default(self, predicate=lambda n: n):
        return_item = None
        count = 0

        for item in self.get_from_predicates(True):
            if predicate(item):
                count += 1
                return_item = item

        if count > 1:
            raise SequenceError("The item exists more than one in the query.", item)

        return return_item

    def single(self, predicate=lambda n: n):
        item = self.single_or_default(predicate)

        if item is not None:
            return item

        raise LookUpError("Can not find the item.", item)

    def last_or_default(self, predicate=lambda n: n):
        for item in self.get_from_predicates(False):
            if predicate(item):
                return item
        return None

    def last(self, predicate=lambda n: n):
        item = self.last_or_default(predicate)

        if item is not None:
            return item

        raise LookUpError("Can not find the item.", item)

    def first_or_default(self, predicate=lambda n: n):
        for item in self.get_from_predicates():
            if predicate(item):
                return item
        return None

    def first(self, predicate=lambda n: n):
        item = self.first_or_default(predicate)

        if item is not None:
            return item

        raise LookUpError("Can not find the item.", item)

    def skip(self, number):
        self.__skip += number
        return self

    def take(self, number):
        self.__take = number
        return PyQuery(self.to_list())

    def as_enumerable(self):
        return self.get_from_predicates()

    def to_list(self):
        return_list = []

        for item in self.get_from_predicates():
            return_list.append(item)

        return return_list

    def get_from_predicates(self, forward=True):
        if forward:
            start = 0 + self.__skip
            stop = len(self.__data_set)
            step = 1
        else:
            start = len(self.__data_set) - 1 + (self.__skip * -1)
            stop = -1
            step = -1

        count = 0

        for i in xrange(start, stop, step):
            add = True
            val = self.__data_set[i]

            for predicate in self.__predicates:
                if not predicate(val):
                    add = False
                    break

            if add:
                count += 1
                yield val

            if self.__take is not None:
                if self.__take == count:
                    break
