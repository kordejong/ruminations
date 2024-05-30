# Dependencies

Topics related to handling dependencies between generated files and their sources.


(deps-manage-deps)=
## Consider managing dependencies using a tool

Often, a repository contains source files that are used to generate other files. For example, you may generate
documentation ([](#deps-generate-documentation)) from input text files or documented source code. To generate
the documentation you can type in the command that does that, or put the command in a shell script and run
that. A better way to handle this is using a tool that will do "whatever is needed" to update generated files.
This has several advantages:

- Files are only generated when needed
- Depending on the tool, generating files works on all popular development environments and platforms
- How to generate files is documented
- Depending on the tool used, it is easy to separate the directory containing the generated files from the
  directory containing the source files ([](#deps-separate-source-build).


(deps-generate-documentation)=
## Automatically generate documentation

TODO


(deps-separate-source-build)=
## Put generated files in a separate directory

TODO
