configure_file(
    _config.yml.in
    _config.yml
    @ONLY
)

file(GLOB names_of_files_to_copy
    RELATIVE ${CMAKE_CURRENT_SOURCE_DIR}
    CONFIGURE_DEPENDS
    _toc.yml
    references.bib
    *.md
)
file(
    COPY
        ${names_of_files_to_copy}
    DESTINATION
        ${CMAKE_CURRENT_BINARY_DIR}
)

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
            ${names_of_files_to_copy}
)
