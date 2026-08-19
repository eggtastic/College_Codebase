#include <iostream>
using namespace std;

int a, b;

void operations() {
    cout<<"--- ALL OPERATIONS. ---"<<endl;
}

int addition(int a, int b){
    return a+b;
}
int sub(int a, int b){
    return a-b;
}
int multi(int a, int b){
    return a*b;
}
float division(float a, float b){
    return a/b;
}

int main () 
{ 
    cout<<"-- HELLO! WELCOME TO THE PROGRAM. --\n"<<endl;

    cout<<"Enter Argument #1: ";
    cin>>a;
    cout<<"Enter Argument #2: ";
    cin>>b;
    int sum = addition(a, b);
    int diff = sub(a, b);
    int prod = multi(a, b);
    float quo = division(a, b);

    operations();

    cout<<"\nThe sum is: "<<sum<<endl;
    cout<<"The difference is: "<<diff<<endl;
    cout<<"The product is: "<<prod<<endl;
    cout<<"The quotient is: "<<quo<<endl;

    return 0;
}