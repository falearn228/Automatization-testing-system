#include "student_func.h" 
#include "pch.h" 
extern "C" __declspec(dllexport) 
string print_grade(int score) {
    stringstream output;
    streambuf* oldCoutBuffer = cout.rdbuf(output.rdbuf());

    if (score >= 90 && score <= 100) {
        cout << "Great" << endl;
    }
    else if (score >= 75 && score < 90) {
        cout << "Good" << endl;
    }
    else if (score >= 60 && score < 75) {
        cout << "Satisfactory" << endl;
    }
    else if (score >= 0 && score < 60) {
        cout << "Unsatisfactory" << endl;
    }
    else {
        cout << "Incorrect" << endl;
    }

    cout.rdbuf(oldCoutBuffer);
    return output.str();
}