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
