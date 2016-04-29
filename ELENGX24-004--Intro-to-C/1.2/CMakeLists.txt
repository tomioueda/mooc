cmake_minimum_required(VERSION 3.5)
project(1_2)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES hello.c)
add_executable(1_2 ${SOURCE_FILES})