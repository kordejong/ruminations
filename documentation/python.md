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


(py-write-tests)=
## Write tests

TODO

See also:

- https://docs.python.org/3/library/unittest.html


(py-develop-package)=
## Develop packages

Put the majority of your code in a package. In general, it is possible to put 99.999% of (model) code in a
package.

Developing a package is as easy as:

1. Create a directory named after the package
1. Add `__init__.py`
1. Add any other modules and sub packages

```bash
# Create a package containing a single function
mkdir my_package
echo 'def hello_world(): print("Hello World!")' > my_package/__init__.py

# Import the package and call the function
PYTHONPATH=. python -c "import my_package; my_package.hello_world()"
```

Developing packages has several advantages. Code that is part of a package is more convenient to test because
you can put the package in some directory and the test modules in some other directory. Expanding the
`PYTHONPATH` variable to include the path to the package directory is all that is needed to be able to `import
my_package` in test modules.

The API of code that is easier to test is easier to get right. For example, when writing a test for a function
you just wrote, you become the client of your own code. This will make you think about various factors that
affect the API of your package, like the name of the function, the order, type and names of the arguments, and
the order and type of the results. If things don't make sense, you will be the first one to suffer from it.

Part of designing a good API for a package involves grouping tightly related code in individual sub packages.
Nested sub packages can be used to group lower level abstractions and high level abstractions in different sub
packages. A package containing well thought out sub packages is easier to reason about and cheaper to
maintain. Also, it is likely that there will be code that is very dependent on the current use-case (e.g. a
model), but also support code that is less dependent on the current use-case. Having this code in a sub
package makes it easy to reuse in another context. Maybe the package can be turned into a body of code used in
the implementation of a set of models.

:::{note}
Always put a, possibly empty, file called `__init__.py` in your package and sub-packages. This is easy to
forget and will result in packages that cannot be found and imported.
:::

A client application (e.g. a model) can be implemented using three lines of code:

```python
"""
Wrapper script for the my_model command-line application
"""
#!/usr/bin/env python
import sys

# Assume there is a module called my_package/cli/my_model.py containing a main function implementing the logic
# for the command-line application, including parsing the command-line arguments
from my_package.cli.my_model import main

sys.exit(main())
```

See also:

- [](#py-write-tests)
- https://docs.python.org/3/tutorial/modules.html#packages


(py-relative-imports)=
## Prefer relative imports

When developing a package, use relative imports when referring to modules that are part of that same package.
This will allow you to rename the package later by just renaming the toplevel package directory.

```python
# Do this...
from .component import soil as soil_component

# ...instead of:
import my_package.component.soil as soil_component
```

See also:

- [](#py-develop-package)
