#include "check_result.h"

using json = nlohmann::json;

std::string variantToString(const std::variant<int, float, std::string>& value) {
    if (std::holds_alternative<int>(value)) {
        return std::to_string(std::get<int>(value));
    }
    else if (std::holds_alternative<float>(value)) {
        return std::to_string(std::get<float>(value));
    }
    else if (std::holds_alternative<std::string>(value)) {
        return std::get<std::string>(value);
    }
    return "";
}

std::vector<int> parseArrayFromJSON(const std::string& jsonArrayStr) {
    std::vector<int> result;
    std::string arrayStr = jsonArrayStr.substr(1, jsonArrayStr.size() - 2); // Удаляем квадратные скобки
    arrayStr.erase(std::remove_if(arrayStr.begin(), arrayStr.end(), ::isspace), arrayStr.end()); // Удаляем пробелы

    std::istringstream ss(arrayStr);
    std::string token;

    while (std::getline(ss, token, ',')) {
        result.push_back(std::stoi(token));
    }

    return result;
}

template <typename T>
bool check_result(T result, T expected_result) {
    return result == expected_result;
}

int main(int argc, char** argv) {
    setlocale(LC_ALL, "ru");
    int selected_task_index = 2;
    std::string path_to_interface_and_tasks = "C:\\Users\\falearn\\source\\repos\\the_func";
    std::string tests_for_function;
    std::size_t pos;
    std::string interface_of_functions = "\\Interface_of_functions.json";
    //C:\\Users\\falearn\\source\\repos\\the_func
    if (argc >= 0) {
       //selected_task_index = std::stoi(argv[1], &pos, 10);
      // path_to_interface_and_tasks = argv[2];
       interface_of_functions = path_to_interface_and_tasks + interface_of_functions;
       //if (!isFileInDirectory(interface_of_functions, path_to_interface_and_tasks)) {
       //    std::cout << "Error: file with interface of functions doesn't exist in this directory" << std::endl; 
       //    return -1;
       //}
    }
    /*else {
        std::cout << "Erorr: Input task index and path to your files: " << std::endl;
        std::cin.get();
        return -1;
    } */
    
    switch (selected_task_index) {
    case 0:
        tests_for_function = "\\read_and_calculate_average.json";
        tests_for_function = path_to_interface_and_tasks + tests_for_function;
        break;
    case 1: 
        tests_for_function = "\\min_element_in_massive.json";
        tests_for_function = path_to_interface_and_tasks + tests_for_function;
     /*   if (!isFileInDirectory("min_element_in_massive.json", path_to_interface_and_tasks)) {
            std::cout << "Error: file with test 'min_element_in_massive.json' doesn't exist in this directory" << std::endl;
            return -1;
        }*/
        break;
    case 2:
        tests_for_function = "\\print_grade.json";
        tests_for_function = path_to_interface_and_tasks + tests_for_function;
        break;
    case 3:
        tests_for_function = "\\sum_element_in_massive.json";
        tests_for_function = path_to_interface_and_tasks + tests_for_function;
    default:
        std::cout << "This task index is not exist... Please try again " << std::endl;
    }
    int int_result;
    unsigned int uint_result;
    float float_result;
    std::string string_result;

    int expected_int_result;
    unsigned expected_uint_result;
    float expected_float_result;
    std::string expected_string_result;

    int number_of_successful_tests = 0;
    int number_of_failed_tests = 0;
    
    HINSTANCE hDll = LoadLibrary(L"C:\\Users\\falearn\\source\\repos\\my_dll_1\\x64\\Release\\my_dll_1.dll");
    test_case_t lpFunc = (test_case_t)GetProcAddress((HMODULE)hDll, "test_case");
    if (hDll == NULL) {
        std::cout << "Error: Library don't founded..." << std::endl;
        return 0;
    }
    
    if (lpFunc == nullptr) {
        std::cout << "Erorr: Function was not found in DLL..." << std::endl;
        return 0;
    }
    std::ifstream file(interface_of_functions);
    json data;
    file >> data;   
    auto selected_task =  data[selected_task_index];
    file.close();
    
    void** params = nullptr;
    
    std::string name = selected_task["name"];
    std::string return_val = selected_task["return_val"];
    std::cout << return_val << std::endl;
    return_space::ReturnType return_val_for_switch = return_space::type_name_to_type_index[return_val];
    std::vector<std::string> params_type_list = selected_task["params_type_list"];

    //TODO данные с тестами будут приходить из вне. подумать как их принимать
    std::ifstream file_with_tests(tests_for_function);
    json data_tests;
    file_with_tests >> data_tests;
    file_with_tests.close();

    std::vector<std::variant<int, float, std::string>> tests_outputs;

    std::vector<int> tests;
    for (int i = 0; i < data_tests.size(); i++) {

        // check! testCase["stimulus"].size() == params_type_list.size();
        // for(index = 0; index < params_type_list.size(); index++) {
        //     params[index] = new ... 
        //     params[index] <- parse_param_string(testCase["stimulus"][index], params_type_list[index]);
         //}
        params = new void* [params_type_list.size()];
        if (data_tests[i]["stimulus"].size() != params_type_list.size())
        {
            std::cout << "data_tests[].size() != params_type_list.size()" << std::endl << std::flush;
            std::cin.get();
            return -1;
        }
        for (int index = 0; index < params_type_list.size(); index++) {
            if (params_type_list[index] == "int*") {
                std::vector<int> stimulus_array = parseArrayFromJSON(data_tests[i]["stimulus"][index].get<std::string>());
                params[index] = new int[stimulus_array.size()];
                std::copy(stimulus_array.begin(), stimulus_array.end(), static_cast<int*>(params[index]));
            }
            else if (params_type_list[index] == "int") {
            params[index] = new int[1];
            *((int*)params[index]) = std::stoi(data_tests[i]["stimulus"][index].get<std::string>());
            }
            else if (params_type_list[index] == "float") {
            params[index] = new float[1];
            *((float*)params[index]) = std::stof(data_tests[i]["stimulus"][index].get<std::string>());
            }
        }
        
        if (return_val_for_switch == return_space::INT) {
            expected_int_result = std::stoi(data_tests[i]["reactus"].get<std::string>());
        }
        else if (return_val_for_switch == return_space::UINT) {
            expected_uint_result = std::stoul(data_tests[i]["reactus"].get<std::string>());
        }
        else if (return_val_for_switch == return_space::FLOAT) {
            expected_float_result = std::stof(data_tests[i]["reactus"].get<std::string>());
        }
        else if (return_val_for_switch == return_space::STRING) {
            expected_string_result = data_tests[i]["reactus"].get<std::string>();
        }
        
        switch (return_val_for_switch) {
        case return_space::INT:
            lpFunc(params, (void*)&int_result);

            if (check_result(int_result, expected_int_result) == 0) {
                number_of_failed_tests += 1;
                tests.push_back(i);
                tests_outputs.push_back(int_result);
            }
            else if (check_result(int_result, expected_int_result) == 1) {
                number_of_successful_tests += 1;
            }
            break;
        case return_space::UINT:
            lpFunc(params, (void*)&uint_result);
            break;
        case return_space::FLOAT:
            lpFunc(params, (void*)&float_result);

            if (check_result(float_result, expected_float_result) == 0) {
                number_of_failed_tests += 1;
                tests.push_back(i);
                tests_outputs.push_back(float_result);
            }
            else if (check_result(float_result, expected_float_result) == 1) {
                number_of_successful_tests += 1;
            }
            break;
        case return_space::STRING:
            lpFunc(params, (void*)&string_result);
            if (name == "print_grade") {
                if (string_result.find(expected_string_result) != std::string::npos) {
                    number_of_successful_tests += 1;
                }
                else {
                    number_of_failed_tests += 1;
                    tests.push_back(i);
                    tests_outputs.push_back(string_result);
                }
            }
            break;
        default:
            std::cout << "Unknown return type." << std::endl << std::flush;
            return -1;
        }

        for (int index = 0; index < params_type_list.size(); index++) {
            if (params_type_list[index] == "int*") {
                delete[] static_cast<int*>(params[index]);
            }
            else if (params_type_list[index] == "int") {
                delete static_cast<int*>(params[index]);
            }
            else if (params_type_list[index] == "float") {
                delete static_cast<float*>(params[index]);
            }
            else if (params_type_list[index] == "string") {
                delete static_cast<std::string*>(params[index]);
            }
        }
        delete[] params;
    }
    std::cout << "The number of tests: " << data_tests.size() << std::endl <<std::flush;
    std::cout << "The number of failed tests: " << number_of_failed_tests << std::endl<<std::flush;
    std::cout << "The number of succesful tests: " << number_of_successful_tests << std::endl<<std::endl<< std::flush;

    for (int i = 0; i < tests.size(); i++) {
        std::cout << "List of incorrect tets" << std::endl;
        std::cout << "Input: " << data_tests[i]["stimulus"] << ", Output: " << data_tests[i]["reactus"] << ", Your output: " << variantToString(tests_outputs[i])<< std::endl;
    }

    FreeLibrary(hDll);
    std::cout << "Press Enter for exit..." << std::endl;
    std::cin.get();
    return 0;
}

