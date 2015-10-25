# PyQuery
An extension class for lists providing features found in .NET's LINQ Library.

## Features
The library provides the following features for lists in Python

* **first** - gets the first in the list or throws an exception
* **first_or_default** - gets the first in the list or returns None if not found
* **single** - returns the item if its the only instance in the list otherwise it will throw an exception
* **single_or_default** - returns the item if its the only instance or return None if it can not find any instance in the list
* **take** - limit the lists contents by a certain number
* **skip** - skip n number of items in the list
* **where** - create a query using lambdas
* **any** - determine if any items match the lambda provide
* **contains** - determine if the instance is in the list
* **last** - return the last item in the list or throw an exception
* **last_or_default** - return the last item in the list or return None
* **to_list** - flatten the queries to a new list
* **as_enumerable** - return a yield to iterate through the list

## License
MIT
