# Dependencies

Topics related to handling dependencies between generated files and their sources.


(deps-cmake)=
## Use CMake

Often, a repository contains source files that are used to generate other files. For example, you may generate
documentation from input text files or documented source code. To generate the documentation you can type in
the command that does that, or put the command in a shell script and run that. A better way to handle this is
using a tool that will do "whatever is needed" to update generated files. This has several advantages:

- Files are only generated when needed
- Generating files works on all popular development environments and platforms. Collaborators may not use the
  same development environment or platform as you use.
- How to generate files is documented
- It is easy to separate the directory containing the generated files from the directory containing the source
  files

Other tools exist with which you can achieve something similar as CMake. In the domain of software development
CMake is the most popular dependency management tool. Alternatives that may work better for you are GNU Make,
Snakemake, Meson. Each of them has its own set of advantages and disadvantage. When in doubt, just use
CMake. It is also available as a Python Wheel package (`pip install cmake`) and as a Conda package (`conda
install cmake`).

See also:

- [cmake.org](https://cmake.org)
- [](#deps-generate-documentation)
- [](#deps-separate-source-build)


(deps-generate-documentation)=
## Automatically generate documentation

TODO

- [sphinx-doc.org](https://www.sphinx-doc.org)


(deps-separate-source-build)=
## Put generated files in a separate directory

TODO


Additionally, it can be convenient to group the build directories of all repositories within a root build and
keep this directory tree seperate from the directory tree containing the repositories. Within the build tree,
you could organize the directories similar to the repository tree. One advantage of this is that if you need
more disk space, you can easily remove a selection of the build directories.

See also:

- [](#repo-organize)
