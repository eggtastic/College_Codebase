#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main () {
    
    // -------------- machine problem 1 ----------------

    string movieName;
    int adultSold, childSold;
    double ticketPrice, adultPrice, childPrice, percentCharity, donatedCharity, ticketTotal, netSale, grossSale;

    cout << "Machine Problem 1: This is a system that will calculate the gross amount of a movie ticket's sales, and the amount to be donated to charity.";
    cout << "\nMovie Name: ";
    getline(cin, movieName);
    cout << fixed << setprecision(2);

    cout << "Adult Ticket Price: ";
    cin >> adultPrice;
    cout << "Child Ticket Price: ";
    cin >> childPrice;

    cout << "\nTickets sold to Adults: ";
    cin >> adultSold;
    cout << "Tickets sold to Children: ";
    cin >> childSold;

    grossSale = (adultPrice * adultSold) + (childPrice * childSold);

    cout << "\nInput percent to donate: ";
    cin >> percentCharity;
    donatedCharity = grossSale * (percentCharity / 100);

    netSale = grossSale - donatedCharity;

    cout << "\nYour amount donated to charity is: " << donatedCharity << ".";

    netSale = grossSale - donatedCharity;
    cout << "\nYour net sale is: " << netSale << ".\n";

    // -------------- machine problem 2 ----------------

    double hourlyRate, hoursWorked, taxHeld, netPay, grossPay, withheldPay;

    cout << "\nMachine Problem 2: Net Income System.\n";

    cout << "\nInput Hourly Pay Rate: ";
    cin >> hourlyRate;
    cout << "Input Hours Worked: ";
    cin >> hoursWorked;
    cout << "Input Tax Withheld: ";
    cin >> taxHeld;

    grossPay = hourlyRate * hoursWorked;
    withheldPay = grossPay * (taxHeld / 100.0);
    netPay = grossPay - withheldPay;

    cout << "Congratulations! Your gross pay is: " << grossPay << ".";
    cout << "\nAnd your withheld amount is: " << taxHeld << ".";
    cout << "\nAnd your net pay is: " << netPay << ".\n";

    // -------------- machine problem 3 ----------------

    int value1, value2, sum, diff, product;
    double quotient;

    cout << "Machine Problem 3: Calculating System.";
    
    cout << "\nInput first value: ";
    cin >> value1;
    cout << "Input second value: ";
    cin >> value2;

    sum = value1 + value2;
    diff = value1 - value2;
    product = value1 * value2;
    quotient = value1 / value2;

    cout << "\nThe sum of the two values is: " << sum << ".";
    cout << "\nThe difference of the two values is: " << diff << ".";
    cout << "\nThe product of the two values is: " << product << ".";
    cout << "\nThe quotient of the two values is: " << quotient << ".\n";

    // -------------- machine problem 4 ----------------

    double prelimGrade, midtermGrade, endtermGrade, finalGrade;

    cout << "\nMachine Problem 4: Grading System.";

    cout << "\nEnter Prelim Grade (30%): ";
    cin >> prelimGrade;
    cout << "Enter Midterm Grade (30%): ";
    cin >> midtermGrade;
    cout << "Enter Endterm Grade (40%): ";
    cin >> endtermGrade;

    finalGrade = (prelimGrade * .30) + (midtermGrade * .30) + (endtermGrade * .40);
    cout << "\nCongratulations! The final grade is: " << finalGrade << ".\n";

    // -------------- machine problem 5 ----------------

    double celsius, fahrenheit;

    cout << "\nMachine Problem 5: Conversion System.";

    cout << "\nInput temperature in celsius: ";
    cin >> celsius;

    fahrenheit = celsius * 1.8 + 32;

    cout << "The equivalent of Celsius to Fahrenheit is: " << fahrenheit << ".\n";

    // -------------- machine problem 6 ----------------

    double radius, diameter, circumference;
    
    cout << "\nMachine Problem 6: Measurement System.";

    cout << "\nEnter radius of circle: ";
    cin >> radius;

    diameter = radius * 2;
    circumference = diameter * 3.14;

    cout << "\nCongratulations! The equivalent to diameter is: " << diameter << ".";
    cout << "\nAnd equivalent to circumference is: " << circumference << ".\n";
    
    return 0;
}