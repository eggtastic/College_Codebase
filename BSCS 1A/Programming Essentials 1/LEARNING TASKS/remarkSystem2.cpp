#include <iostream>
using namespace std;

int main () 
{ 
    int grade; 

    cout<<"\n--- REMARK SYSTEM ---\n"<< endl;

    cout<<"Enter Grade: ";
    cin>>grade; 

    if (grade > 100) {
        cout << "Remark: Overflow.";
    }
    else if (grade >= 95 && grade <= 100) {
        cout << "Remark: Excellent!";
    }
    else if (grade >= 90 && grade <= 94) {
        cout << "Remark: Very Good.";
    }
    else if (grade >= 85 && grade <= 89) {
        cout << "Remark: Good.";
    }
    else if (grade >= 80 && grade <= 84) {
        cout << "Remark: Satisfactory.";
    }
    else if (grade >= 75 && grade <= 79) {
        cout << "Remark: Needs Improvement.";
    }
    else if (grade >= 60 && grade <= 74) {
        cout << "Remark: Failed.";
    }
    else if (grade >= 1 && grade <= 54) {
        cout << "Remark: Invalid Input.";
    }
    else {
        cout << "Remark: ERROR. Please try again.";
    }
    

    return 0;
}