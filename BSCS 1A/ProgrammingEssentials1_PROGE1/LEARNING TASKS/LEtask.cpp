#include <iostream>

using namespace std;

int main()
{
    int choose, grade, val1, val2;
    double answer;
    char operation;

    cout << "--= GRADING  SYSTEM. CHOOSE ! =--\n"<<endl;
    cout << "1. Remark System." << endl;
    cout << "2. Mathematical Operator System." << endl;
    cout << "Please Choose: ";
    cin >> choose;

    if (choose == 1) {
        cout << "\n--- REMARK SYSTEM ---\n" << endl;

        cout << "Enter Grade: ";
        cin >> grade;

        if (grade >= 75) {
            cout << "Remark is: Passed."<<endl;
        }
        else {
            cout << "Remark is: Failed."<<endl;
        }

        return 0;
    }
    else if (choose = 2) {

        cout << "\n--- MATHEMATICAL OPERATOR SYSTEM ---\n" << endl;

        cout << "Enter 1st Value: ";
        cin>>val1;
        cout << "Enter 2nd Value: ";
        cin>>val2;

        cout << "a. Addition(+)"<<endl;
        cout << "b. Subtraction (-)"<<endl;
        cout << "c. Multiplication (*)"<<endl;
        cout << "d. Division(/)"<<endl;

        cout << "Please choose the operator above: ";
        cin >> operation;

        if (operation == 'A' || operation == 'a') {
            answer = val1 + val2;
            cout << val1 << " + " << val2 << " = " << answer;
        }
        else if (operation == 'B' || operation == 'b') {
            answer = val1 - val2;
            cout << val1 << " - " << val2 << " = " << answer;
        }
        else if (operation == 'C' || operation == 'c') {
            answer = val1 * val2;
            cout << val1 << " * " << val2 << " = " << answer;
        }
        else if (operation == 'D' || operation == 'd') {
            answer = val1 / val2;
            cout << val1 << " / " << val2 << " = " << answer;
        }
        else {
            cout << "ERROR. Invalid input."<<endl;
        }

        return 0;
    }
    else {
        cout << "ERROR. Invalid input."<<endl;
        return 0;
    }
    
}

