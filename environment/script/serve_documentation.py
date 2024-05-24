#!/usr/bin/env python
from livereload import Server, shell

# https://pypi.org/project/livereload/
# TODO
# - Extend file list to include all files used for building documentation
# - Generalize, get rid of paths


source_prefix = "/home/kor/development/project/github/kordejong/ruminations"
build_prefix = "/home/kor/development/object/ruminations"
documentation_source_prefix = f"{source_prefix}/documentation"
documentation_build_prefix = f"{build_prefix}/documentation/_build/html"


server = Server()
server.watch(
    f"{documentation_source_prefix}/*.md",
    shell(f"cmake --build {build_prefix} --target documentation.html")
)
server.serve(root=documentation_build_prefix)
