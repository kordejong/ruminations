cmake_minimum_required(
    VERSION 3.26)
project(Ruminations
    LANGUAGES NONE
    VERSION 0.0.1
    DESCRIPTION "Ruminations on setting up and maintaining model development projects"
    HOMEPAGE_URL "https://github.com/computationalgeography/ruminations"
)

set(RUMINATIONS_TITLE "Ruminations on model development")
set(RUMINATIONS_AUTHOR "Computational Geography R&D Team")
set(RUMINATIONS_BOOK_BASENAME "ruminations-${CMAKE_PROJECT_VERSION}")

list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/environment/cmake)

find_package(JupyterBook)

add_subdirectory(documentation)
