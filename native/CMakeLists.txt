cmake_minimum_required(VERSION 3.20)
project(dfesp_injector LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_library(dfesp_injector SHARED injector.cpp)
target_compile_definitions(dfesp_injector PRIVATE WIN32_LEAN_AND_MEAN NOMINMAX)
target_link_libraries(dfesp_injector PRIVATE kernel32 user32)