#include <iostream>
using namespace std;

class Person {
private:
    string name;
    int age;
public:
    void setName(string n){
        name = n;
    }

    string getName(){
        return name;
    }

    void setAge(int a){
        if (a > 0) {
            age = a;
        } else {
            cout << "WRONG INPUT. Terminating program...";
            exit(1);
        }
    }

    int getAge(){
        return age;
    }
};

class Student : public Person {
private:
    int grade;
public:
    void setGrade(int g){
        if (g >= 1 && g <= 12) {
            grade = g;
        } else {
            cout << "WRONG INPUT. Terminating program...";
            exit(1);
        }
    }

    int getGrade(){
        return grade;
    }
};

class Info : public Student {
public:
    void displayInfo(){
        cout << "\n--STUDENT INFO--" << endl;
        cout << "Student Name: " << getName() << endl;
        cout << "Student Age: " << getAge() << endl;
        cout << "Student Grade Level: " << getGrade() << endl;
    }
};

int main()
{
    Info info;

    string nameInput;
    int ageInput;
    int gradeInput;

    cout << "-- PRACTICE --" << endl;

    cout << "Enter Student Name: ";
    cin >> nameInput;

    cout << "Enter Age: ";
    cin >> ageInput;

    cout << "Enter Grade Level (1-12): ";
    cin >> gradeInput;

    info.setName(nameInput);
    info.setAge(ageInput);
    info.setGrade(gradeInput);

    info.displayInfo();

    return 0;
}
