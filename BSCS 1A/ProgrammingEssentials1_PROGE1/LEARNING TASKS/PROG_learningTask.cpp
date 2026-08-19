#include <iostream>
using namespace std;

int main() {
    string customerItem;
    int itemPrice, itemQuantity, initialtoBePaid, finaltoBePaid, cashOnHand, customerChange;
    double itemDiscount, discountPercent, discountAmount;

    cout << "Hello! This is a sales system. We will compute the customer exchange.";

    cout << "\nInput customer item: \n";
    cin >> customerItem;
    cout << "Please enter the item's tag price: \n";
    cin >> itemPrice;
    cout << "Please enter item quantity: \n";
    cin >> itemQuantity;
    cout << "Please enter the item discount: \n";
    cin >> discountPercent;
    cout << "Please enter customer's current cash on hand: \n";
    cin >> cashOnHand;
    
    initialtoBePaid = itemPrice * itemQuantity;
    itemDiscount = (initialtoBePaid * discountPercent) / 100.0;
    finaltoBePaid = initialtoBePaid - itemDiscount;
    cout <<  "\nCongratulations! For the " << customerItem << ", the customer's amount to be paid is: " << finaltoBePaid << ".\n";
    customerChange = cashOnHand - finaltoBePaid;
    cout << "The customer's change is: " << customerChange << ".";

    return 0;
}
