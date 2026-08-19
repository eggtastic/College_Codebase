#include <iostream>

using namespace std;

    enum Operations {
    ADD,
    SUBTRACT,
    MULTIPLY,
    DIVIDE,
};

class Calculator {
    private:
        int result;
    public:
        int get_result(){
            return result;
        };
        int operation(int a, int b, Operations c){
            switch(c){
                case ADD:
                    return a + b;
                case SUBTRACT:
                    return a - b;
                case MULTIPLY:
                    return a * b;
                case DIVIDE:
                    return a / b;
            }
        };
};

string PrintOperation(Operations op){
    switch(op){
            case ADD:
                return "Add.";
                break;
            case SUBTRACT:
                return "Subtract.";
                break;
            case MULTIPLY:
                return "Multiply.";
                break;
            case DIVIDE:
                return "Divide.";
                break;
        }
    };

int main()
{
    Operations op;
    Calculator calc;
    int choice, num1, num2;
    cout << "Choose Operation" << endl;
    cout << "1 - Addition" << endl;
    cout << "2 - Subtraction" << endl;
    cout << "3 - Multiplication" << endl;
    cout << "4 - Division" << endl;
    while (true){
    try {
        cout<<"\n Choose Operation: ";
        cin>>choice;
        if (choice>=1 && choice<=4){
            Operations op = static_cast<Operations>(choice-1);
            cout<<"CHOSEN: "<<PrintOperation(op)<<endl;
            break;
        } else {
            throw(choice);
        }
    } catch (int bad) {
        cout<<bad<<" is not a valid input, please try again"<<endl;
    };
    };
    cout<<"Please enter your first number: ";
    cin>>num1;
    while (true){
        try {
        cout<<"Please enter your second number: ";
        cin>>num2;
        if(op!=3){
            break;
        } else if (op==3 && num2!=0){
            break;
        } else {
            throw(num2);
        }
    } catch (int wrong) {
        cout<<"Cannot Divide By 0."<<endl;
    };
    };
    calc.operation(num1, num2, op);
    int result=calc.get_result();
    cout<<"Result: "<<result;
    return 0;
}
