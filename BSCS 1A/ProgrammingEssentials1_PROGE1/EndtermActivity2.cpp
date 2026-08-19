#include <iostream>

using namespace std;

class Person {
    private:
        string name;
    public:
    // constructor 
        Person(const string& n) : name(n) {}

        string getName() const {
            return name;
        }

        virtual void introduce() {
            cout << "I am a job named name in year."<<endl;
        }
};
class Student : public Person {
    private:
        int grade;
    public:
    // constructor 
        Student (const string&n, int g) : Person(n), grade(g) {}

        void introduce() override {
            cout << "I am a student named "<< getName()<<" in year "<< grade <<"."<<endl;
        }
};

class Teacher : public Person {
    private:
        string subject;
    public:
    // constructor 
        Teacher(const string&n, string s) : Person(n), subject(s) {}

        void introduce() override {
            cout << "I am a teacher named "<< getName()<<" and I teach "<< subject <<"."<<endl;
        }
};


int main()
{
    Person* person;
    Student student1("Lynx", 12);
    Teacher teacher1("Sharyl", "English");

    person = &student1;
    person->introduce();

    person = &teacher1;
    person->introduce();

    return 0;
}
