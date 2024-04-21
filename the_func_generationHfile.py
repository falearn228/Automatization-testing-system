import re

student_function_file = r"C:\Users\falearn\source\repos\test_dll\test\student_func.cpp"   # файл откуда записывать, то есть функция студента

cpp_file_path = "C:\\Users\\falearn\\source\\repos\\my_dll_1\\student_func.cpp"  #файл куда записать функцию студента, dll, место записи .cpp
header_file_path = "C:\\Users\\falearn\\source\\repos\\my_dll_1\\student_func.h"  #файл куда записать функцию студента, dll, место записи .h

test_cpp_file = r"C:\Users\falearn\source\repos\my_dll_1\dll.cpp"   # функция, которая вызывает функцию студента test_case

with open(student_function_file, 'r') as student_file:
    student_content = student_file.read()
    pattern = re.compile(r'\s*\b(?:int|void|float|unsigned int|string)\s+(\w+)\s*\(')
    match = pattern.search(student_content)
    if match:
        function_name = match.group(1)
        start_index = match.start()
        end_index = student_content.rfind("}", start_index)
        end_index_for_h_file = student_content.find(")", start_index)
        if end_index != -1 and end_index_for_h_file != -1:
            function_declaration = student_content[start_index:end_index + 1]
            function_declaration_for_h_file = student_content[start_index:end_index_for_h_file + 1]
            # Изменение возвращаемого типа функции на string, если название функции "print_grade"
            if function_name == "print_grade":
                function_declaration = function_declaration.replace(function_declaration.split()[0], "string", 1)
                function_declaration_for_h_file = function_declaration_for_h_file.replace(
                    function_declaration_for_h_file.split()[0], "string", 1)

                # Добавление кода в начало и конец тела функции
                function_body_start = function_declaration.find("{") + 1
                function_body_end = function_declaration.rfind("}")
                function_body = function_declaration[function_body_start:function_body_end].strip()
                new_function_body = f"\n    stringstream output;\n    streambuf* oldCoutBuffer = cout.rdbuf(output.rdbuf());\n\n    {function_body}\n\n    cout.rdbuf(oldCoutBuffer);\n    return output.str();\n"
                function_declaration = function_declaration[:function_body_start] + new_function_body + function_declaration[function_body_end:]
            #function_declaration = function_declaration.replace('\n', ' ')

            # Удаление символов новой строки из function_declaration_for_h_file
            #function_declaration_for_h_file = function_declaration_for_h_file.replace('\n', ' ')
            with open(cpp_file_path, 'w') as cpp_file:
                cpp_file.write('#include "student_func.h" \n')
                cpp_file.write('#include "pch.h" \n')
                cpp_file.write(f'extern "C" __declspec(dllexport) {function_declaration}')
            cpp_file.close
            with open(header_file_path, 'w') as header_file:
                header_file.write('#include "pch.h" \n')
                header_file.write("#pragma once \n")
                header_file.write(f'extern "C" __declspec(dllexport) {function_declaration_for_h_file};')
            header_file.close

            # Запись названия функции в другой файл
            with open(test_cpp_file, 'w') as test_cpp:
                test_cpp.write('#include "pch.h"\n#pragma once\n#include "dll.h"\n#include <Windows.h>\n#include "student_func.h"\n\n')
                test_cpp.write('extern "C" __declspec(dllexport) void test_case(void** params, void* result) {\n')
                if function_name == 'min_element_in_massive':
                    test_cpp.write('*((int*)result) = min_element_in_massive((int*)params[0], *((int*)params[1]));\n')
                elif function_name == 'sum_element_in_massive':
                    test_cpp.write('*((int*)result) = sum_element_in_massive((int*)params[0], *((int*)params[1]));\n')
                elif function_name == 'read_and_calculate_average':
                    test_cpp.write('*((float*)result) = read_and_calculate_average(*((int*)params[0]), *((int*)params[1]), *((int*)params[2]), *((int*)params[3]), *((int*)params[4]));\n')
                elif function_name == 'print_grade':
                    test_cpp.write('*((string*)result) = print_grade(*(int*)params[0]);\n')
                elif function_name == 'sum_element_in_massivesssss':
                    test_cpp.write('*((int*)result) = min_element_in_massive_ptr((int*)params[0], *((int*)params[1]));\n')
                test_cpp.write('}')