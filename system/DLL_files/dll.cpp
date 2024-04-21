#include "pch.h"
#pragma once
#include "dll.h"
#include <Windows.h>
#include "student_func.h"

extern "C" __declspec(dllexport) void test_case(void** params, void* result) {
*((string*)result) = print_grade(*(int*)params[0]);
}
