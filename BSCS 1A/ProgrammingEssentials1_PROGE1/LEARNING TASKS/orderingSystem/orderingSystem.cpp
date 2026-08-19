#include <iostream>

using namespace std;

int main()
{
    // note: main opt is if else, then sub-opt is switch case, then desserts make up ur own

    int bfast, desserts, chooseMenu, price, cash, change, quantity;
    char chooseSub;

    cout<<"--- MENU ---"<<endl;
    cout<<"1. Breakfast."<<endl;
    cout<<"2. Desserts."<<endl;
    cout<<"3. Drinks."<<endl;
    cout<<"Please Choose: ";
    cin>>chooseMenu;

    if (chooseMenu == 1) {
        cout<<"\n--- BREAKFAST ---"<<endl;
        cout<<"a. Fried Chicken w/ rice - P50."<<endl;
        cout<<"b. Porkchop w/ rice - P45."<<endl;
        cout<<"Please Choose: ";
        cin>>chooseSub;

        switch(chooseSub) {
            case 'A':
            case 'a': {
                cout <<"\nYour order is Fried Chicken w/ rice P50."<<endl;
                cout<<"Enter Quantity: ";
                cin >> quantity;
                price = 50 * quantity;
                cout << quantity << " Fried Chicken w/ Rice is: P" << price<<endl;
                cout << "Please enter your cash: ";
                cin >> cash;
                if (cash > price) {
                    change = cash - price;
                    cout<< "Your change is: " << change <<"."<<endl;
                }
                else {
                    cout<<"Insufficient cash. We're sorry!";
                }
            }

            break;

            case 'B':
            case 'b': {
                cout <<"\nYour order is Porkchop w/ Rice P45."<<endl;
                cout<<"Enter Quantity: ";
                cin >> quantity;
                price = 45 * quantity;
                cout << quantity << " Porkchop w/ Rice is: P" << price<<endl;
                cout << "Please enter your cash: ";
                cin >> cash;
                if (cash > price) {
                    change = cash - price;
                    cout<< "Your change is: " << change <<"."<<endl;
                }
                else {
                    cout<<"Insufficient cash. We're sorry!";
                }
            }

            break;

            default:
                cout<<"Invalid input. Please try again.";
                return 0;

        }
    }
    else if (chooseMenu == 2) {
        cout<<"\n--- DESSERTS ---"<<endl;
        cout<<"a. Chocolate Cake - P25."<<endl;
        cout<<"b. Ice Cream - P50."<<endl;
        cout<<"Please Choose: ";
        cin>>chooseSub;

        switch(chooseSub) {
            case 'A':
            case 'a': {
                cout <<"\nYour order is Chocolate Cake P25."<<endl;
                cout<<"Enter Quantity: ";
                cin >> quantity;
                price = 25 * quantity;
                cout << quantity << " Chocolate Cake is: P" << price<<endl;
                cout << "Please enter your cash: ";
                cin >> cash;
                if (cash > price) {
                    change = cash - price;
                    cout<< "Your change is: " << change <<"."<<endl;
                }
                else {
                    cout<<"Insufficient cash. We're sorry!";
                }
            }

            break;

            case 'B':
            case 'b': {
                cout <<"\nYour order is Ice Cream P50."<<endl;
                cout<<"Enter Quantity: ";
                cin >> quantity;
                price = 50 * quantity;
                cout << quantity << " Chocolate Cake is: P" << price<<endl;
                cout << "Please enter your cash: ";
                cin >> cash;
                if (cash > price) {
                    change = cash - price;
                    cout<< "Your change is: " << change <<"."<<endl;
                }
                else {
                    cout<<"Insufficient cash. We're sorry!";
                }
            }

            break;

            default:
                cout<<"\nInvalid input. Please try again.";
                return 0;
        }
    }
    else if (chooseMenu == 3) {
        cout<<"\n--- DRINKS ---"<<endl;
        cout<<"a. Coke P18."<<endl;
        cout<<"b. Sprite - P20."<<endl;
        cout<<"Please Choose: ";
        cin>>chooseSub;

        switch(chooseSub) {
            case 'A':
            case 'a': {
                cout <<"\nYour order is Coke P18."<<endl;
                cout<<"Enter Quantity: ";
                cin >> quantity;
                price = 18 * quantity;
                cout << quantity << " Chocolate Cake is: P" << price<<endl;
                cout << "Please enter your cash: ";
                cin >> cash;
                if (cash > price) {
                    change = cash - price;
                    cout<< "Your change is: " << change <<"."<<endl;
                }
                else {
                    cout<<"Insufficient cash. We're sorry!";
                }
            }

            break;

            case 'B':
            case 'b': {
                cout <<"\nYour order is Sprite P20."<<endl;
                cout<<"Enter Quantity: ";
                cin >> quantity;
                price = 20 * quantity;
                cout << quantity << " Chocolate Cake is: P" << price<<endl;
                cout << "Please enter your cash: ";
                cin >> cash;
                if (cash > price) {
                    change = cash - price;
                    cout<< "Your change is: " << change <<"."<<endl;
                }
                else {
                    cout<<"Insufficient cash. We're sorry!";
                }
            }

            break;

            default:
                cout<<"\nInvalid input. Please try again.";
                return 0;
        }
    }
    else {
        cout<<"\nInvalid input. Please try again.";
        return 0;
    }

    cout<<"\nThank you for ordering!";

    return 0;
}
