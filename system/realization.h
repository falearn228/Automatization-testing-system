#pragma once
#include <iostream>
#include <fstream>
#include <Windows.h>
#include <vector>
#include "C:\Users\falearn\source\repos\my_dll_1\dll.h"
#include "json.h"
#include <string>
#include <sstream>
#include <map>
#include <variant>

namespace return_space {
    enum ReturnType {
        INT,
        FLOAT,
        UINT,
        STRING
    };

    std::map<std::string, return_space::ReturnType> type_name_to_type_index{
    {"int", return_space::INT},
    {"float", return_space::FLOAT},
    {"unsigned int", return_space::UINT},
    {"string", return_space::STRING},
    };
}

typedef void(*test_case_t)(void** params, void* result);


