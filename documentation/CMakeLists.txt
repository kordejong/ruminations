configure_file(
    _config.yml.in
    _config.yml
    @ONLY
)

foreach(name IN ITEMS
    _toc.yml
    changelog.md
    code.md
    dependencies.md
    index.md
    python.md
    references.bib
    repository.md
)
    configure_file(${name} ${name} COPYONLY)
endforeach()

add_custom_target(documentation.html
    VERBATIM
    COMMAND
        ${JupyterBook_EXECUTABLE} build --builder html
        --warningiserror --nitpick --keep-going
        ${CMAKE_CURRENT_BINARY_DIR}
)

add_custom_target(documentation.pdf
    VERBATIM
    COMMAND
        ${JupyterBook_EXECUTABLE} build --builder pdflatex
        ${CMAKE_CURRENT_BINARY_DIR}
)

set_property(
    DIRECTORY
        ${CMAKE_CURRENT_SOURCE_DIR}
    PROPERTY
        ADDITIONAL_CLEAN_FILES
            _build  # jupyter-book
            _config.yml
)
