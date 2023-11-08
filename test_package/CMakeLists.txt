cmake_minimum_required(VERSION 3.15)
project(test_package)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)


find_package( efsw CONFIG REQUIRED)

add_executable(test_package main.cpp)
target_link_libraries( test_package efsw::efsw )
