project(test_package)
cmake_minimum_required(VERSION 3.11)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(${PROJECT_NAME} main.cpp)
target_include_directories(${PROJECT_NAME} PRIVATE ${CONAN_INCLUDE_DIRS})
target_link_directories(${PROJECT_NAME} PRIVATE ${CONAN_LIB_DIRS})
target_link_libraries(${PROJECT_NAME} PRIVATE ${CONAN_LIBS})
