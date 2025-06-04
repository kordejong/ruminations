# Python

Topics related to using Python for model development.

(py-miniforge)=

## Use Miniforge

TODO

- [github.com/conda-forge/miniforge](https://github.com/conda-forge/miniforge)

(py-black)=

## Use Black

TODO

To not have to think about code formatting anymore you can use Pre-commit to run Black on your Python sources
each time you change them.

See also:

- [black.readthedocs.io](https://black.readthedocs.io)
- [](#py-mypy)
- [](#repo-pre-commit)

(py-mypy)=

## Use Mypy

TODO

See also:

- [mypy-lang.org](https://mypy-lang.org/)
- [](#py-black)
- [](#repo-pre-commit)

(py-debug)=

## Know about the debugger

In case weird things seem to happen when executing a Python script, one way to figure out what is going on is
to use the Python Debugger. The basics are very simple:

1. Insert this statement just above the place in the code where things become interesting:

   ```python
   breakpoint()
   ```

   This is a builtin function so there is no need to import anything for this to work.

1. Run the script and wait for the Python Debugger prompt (`(Pdb)`) to appear. Now you are in control of the
   interpreter:

   - You can tell it to execute the next line, by typing the `next` command. Python will stop at the next line
     in the current function.
   - You can tell it to execute the next line, by typing the `step` command. Python will stop at the next line
     in any function called.
   - You can tell it to continue executing, by typing the `continue` command. The interpreter will stop at any
     `breakpoint()` statement it encounters.

There are more things you can do while in the Python Debugger, for example printing the values of variables,
setting their values, etc. For more information see the Python Debugger [reference
page](https://docs.python.org/3/library/pdb.html).

(py-package)=

## Develop a package

A Python package is a collection of Python modules rooted at a single directory. By pointing the Python
interpreter to the directory containing this package directory, a Python package can be imported by client
code that wants to use its functionality. Python uses the environment variable `PYTHONPATH` to find 3rd party
packages.

Developing a model as a Python package instead of storing Python modules in some directory has the following
advantages:

- Once `PYTHONPATH` is set, client code, including unit tests, can easily import the package. Client modules
  does not have to be located in the same directory as the package modules.
- Less risk of naming conflicts between your model's modules and other modules. The package name, when well
  chosen, makes the names of your modules and sub-packages unique.
- Code that is tightly coupled can be put in a sub-package, while code that is loosely coupled can be put in
  another sub-package. This way, dependencies can be managed more easily. Also, by nesting sub-packages,
  abstraction layers can be easily defined.
- Creating an installable wheel file which can be installed using pip becomes more easily.

To create a package, just create a directory and make sure it contains a file called `__init__.py`, which can
be empty, e.g.:

```bash
source/
    my_model/
        __init__.py
```

Given this example, the Python interpreter can use code from the package like this:

```python
PYTHONPATH=source python -c "import my_model"
```

Modules in a package importing other modules from that same package should do so using relative imports. This
makes it easy to rename the whole package by just renaming the top level directory.

See also:

- [](#py-test)
- [](#py-wheel)
- <https://docs.python.org/3/reference/import.html#packages>
- <https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH>

(py-test)=

## Test the package

Tests are source code that verify that other source code behaves as expected. If you develop your model as a
Python package, then writing tests for your model code becomes easy to do. Just import your package and, for
example, verify that it provides the conventional `__version__` attribute:

```python
import unittest

import my_model


class PackageTest(unittest.TestCase):
    def test_version_attribute(self):
        self.assertTrue(hasattr(my_model, "__version__"))
        self.assertTrue(isinstance(my_model.__version__, str))
```

Code implementing tests can (should) be stored outside of the directory containing the package that is being
tested, e.g.:

```bash
source/
    test/
        __init__.py
```

A file called `__init__.py` is required for the test discovery code to be able to import the unit tests:

```bash
TODO
```

See also:

- [](#py-package)
- [](#py-wheel)

(py-wheel)=

## Release a wheel

TODO

See also:

- [](#py-package)
- [](#py-test)
