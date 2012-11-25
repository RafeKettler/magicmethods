##<a id="appendix1" href="#appendix1">Appendix 1: How to Call Magic Methods</a>##

Some of the magic methods in Python directly map to built-in functions; in this case, how to invoke them is fairly obvious. However, in other 
cases, the invocation is far less obvious. This appendix is devoted to exposing non-obvious syntax that leads to magic methods getting called.

Magic Method                       |  When it gets invoked (example)        | Explanation
----------------------             | ----------------------------------     | --------------------------------------------
`__new__(cls [,...])`              |  `instance = MyClass(arg1, arg2)`      |  `__new__` is called on instance creation
`__init__(self [,...])`            |  `instance = MyClass(arg1, arg2)`      |  `__init__` is called on instance creation
`__cmp__(self, other)`             |  `self == other`, `self > other`, etc. |  Called for any comparison
`__pos__(self)`                    |  `+self`                               |  Unary plus sign
`__neg__(self)`                    |  `-self`                               |  Unary minus sign
`__invert__(self)`                 |  `~self`                               |  Bitwise inversion
`__index__(self)`                  |  `x[self]`                             |  Conversion when object is used as index
`__nonzero__(self)`                |  `bool(self)`                          |  Boolean value of the object
`__getattr__(self, name)`          |  `self.name # name doesn't exist`      |  Accessing nonexistent attribute
`__setattr__(self, name, val)`     |  `self.name = val`                     |  Assigning to an attribute
`__delattr__(self, name)`          |  `del self.name`                       |  Deleting an attribute
`__getattribute__(self, name)`     |  `self.name`                           |  Accessing any attribute
`__getitem__(self, key)`           |  `self[key]`                           |  Accessing an item using an index
`__setitem__(self, key, val)`      |  `self[key] = val`                     |  Assigning to an item using an index
`__delitem__(self, key)`           |  `del self[key]`                       |  Deleting an item using an index
`__iter__(self)`                   |  `for x in self`                       |  Iteration
`__contains__(self, value)`        |  `value in self`, `value not in self`  |  Membership tests using `in`
`__call__(self [,...])`            |  `self(args)`                          |  "Calling" an instance
`__enter__(self)`                  |  `with self as x:`                     |  `with` statement context managers
`__exit__(self, exc, val, trace)`  |  `with self as x:`                     |  `with` statement context managers
`__getstate__(self)`               |  `pickle.dump(pkl_file, self)`         |  Pickling
`__setstate__(self)`               |  `data = pickle.load(pkl_file)`        |  Pickling

Hopefully, this table should have cleared up any questions you might have had about what syntax invokes which magic method.

##<a id="appendix2" href="#appendix2">Appendix 2: Changes in Python 3</a>##

Here, we document a few major places where Python 3 differs from 2.x in terms of its object model:

 - Since the distinction between string and unicode has been done away with in Python 3, `__unicode__` is gone and `__bytes__` (which behaves similarly to `__str__` and `__unicode__` in 2.7) exists for a new built-in for constructing byte arrays.
 - Since division defaults to true division in Python 3, `__div__` is gone in Python 3
 - `__coerce__` is gone due to redundancy with other magic methods and confusing behavior
 - `__cmp__` is gone due to redundancy with other magic methods
 - `__nonzero__` has been renamed to `__bool__`
