#include <iostream>
#include <thread>
#include<conio.h>
using namespace std;

int main () {
    string res, email, pass, yesno, chat, chosen;
    char c;
    int topic;
    char cmate;

    cout<<"--= YeheeY Chat System =--"<<endl;
    cout<<"-------------------------------"<<endl;
    cout<<"--= VERSION #1 =--\n"<<endl;

    cout<<"Email: ";
    cin>>email;
    cout<<"Password: ";
    do{
        c = getch();
        switch(c){
        case 0:
            getch();
            break;
        case 13:
            cout<<endl;
            break;
        case 8:
            if(res.length()>0){
                res.erase(res.end()-1);
                cout<<c<<' '<<c;
            }
            break;
        default:
            res += c;
            cout<<'*';
            break;
        }
    }while(c!=13);

    std::string s = "\nLoading... ";

    for (const auto c : s) {
        std::cout << c << std::flush;
        std::this_thread::sleep_for(std::chrono::milliseconds(350));
    }
    std::cout << std::endl;

    cout<<"Welcome, Ana.\n"<<endl;

    selectmate:
        cout<<"Users Online:"<<endl;
        cout<<"A.) Ben"<<endl;
        cout<<"B.) Geli"<<endl;
        cout<<"Users Offline:"<<endl;
        cout<<"1. Perla"<<endl;
        cout<<"2. Carla"<<endl;

        cout<<"Select Chatmate: ";
        cin>>cmate;

    switch(cmate) {
        case '1': {
            cout<<"Sorry, Perla is not online at the moment..."<<endl;
            cout<<"Do you want to chat someone else? ";
            cin>>yesno;

            if (yesno == "Yes" || yesno == "yes") {
                goto selectmate;
            }
            else if (yesno == "No" || yesno == "no") {
                cout << "Thank you for choosing YeheeY Chat System! Have a great day."<<endl;
                return 0;
            }

            break;
        }
        case '2': {
            cout<<"Sorry, Carla is not online at the moment..."<<endl;
            cout<<"Do you want to chat someone else? ";
            cin>>yesno;

            if (yesno == "Yes" || yesno == "yes") {
                goto selectmate;
            }
            else if (yesno == "No" || yesno == "no") {
                cout << "Thank you for choosing YeheeY Chat System! Have a great day."<<endl;
                return 0;
            }
            else {
                cout<<"ERROR: Input. Please try again."<<endl;
                goto selectmate;
            }

            break;
        }
        case 'A':
        case 'a': {
            chosen = "Ben: ";
            cout<<"You are now chatting: Ben.\n"<<endl;

            cout<<"Ana: Care to chat?"<<endl;
            cout<<"Ana: Are you single?"<<endl;
            cout<<"Ben: ";
            getline(cin >> ws, chat);
            cout<<"Ana: I don't care."<<endl;
            cout<<"Ana: What topic would you like us to talk about?\n"<<endl;

            benTopics:
                cout<<"TOPICS:"<<endl;
                cout<<"1.) Global Warming."<<endl;
                cout<<"2.) Horror."<<endl;
                cout<<"3.) My personal background.\n"<<endl;

                cout<<"[BEN] Please Select: ";
                cin>>topic;

            if (topic == 1) {
                cout<<"Ana: Do you believe global warming is real?"<<endl;
                cout<<"Ben: ";
                cin>>chat;

                if (chat == "Yes" || chat == "yes") {
                    cout<<"Ana: Good, at least you know the truth."<<endl;
                }
                else if (chat == "No" || chat == "no") {
                    cout<<"Ana: Oh, come on, don’t be that guy."<<endl;
                }
                else if (chat == "idk" || chat == "Idk" || chat == "I dont know" || chat == "I don't know") {
                    cout<<"Ana: Huh? Maybe you should read more."<<endl;
                }
            }
            if (topic == 2) {
                cout<<"Ana: Do you like horror?"<<endl;
                cout<<"Ben: ";
                cin>>yesno;

                if (yesno == "Yes" || yesno == "yes") {
                    cout<<"Ana: Same! I love the thrill."<<endl;
                }
                else if (yesno == "No" || yesno == "no") {
                    cout<<"Ana: Aww, you’re no fun."<<endl;
                }
                else {
                    cout<<"Ana: Er, did you say english just now?"<<endl;
                }
            }
            if (topic == 3) {
                int age, birthYear;
                cout<<"Ana: How old are you?"<<endl;
                cout<<"Ben: ";
                cin>>age;

                if (age >= 60) {
                    cout<<"Ana: Ohh!!! Ohh, How come you are still alive?"<<endl;
                }
                else if (age >= 19 && age <= 59) {
                    cout<<"Ana: Cool."<<endl;
                }
                else if (age < 18) {
                    cout<<"Ana: Oh, no way you're that young."<<endl;
                }
                else {
                    cout << "Ana: Huh, I don't think that's your real age..."<<endl;
                    goto end;
                }

                birthYear = 2025 - age;
                cout<<"Ana: So I assume you were born in " << birthYear << "?" <<endl;

                cout<<"Ana: Where do you live?"<<endl;
                cout<<"Ben: ";
                cin>>chat;

                if (chat == "Talisay" || chat == "talisay") {
                    cout<<"Ana: was was bugsay talisay"<<endl;
                }
                else if (chat == "Bacolod" || chat == "bacolod") {
                    cout<<"Ana: Oh, I live there too!"<<endl;
                }
                else if (chat == "Cadiz" || chat == "cadiz") {
                    cout<<"Ana: Omg, that's a very nice city."<<endl;
                }
                else {
                    cout<<"Ana: Ah, sorry, I don't know that one."<<endl;
                }
            }

            break;
        }
        case 'B':
        case 'b': {
            chosen = "Geli: ";
            cout<<"You are now chatting: Geli.\n"<<endl;

            cout<<"Ana: Hi, what's your name?"<<endl;
            cout<<"Geli: ";
            getline(cin >> ws, chat);
            cout<<"Ana: Trick question, lol. Your name is right there."<<endl;
            cout<<"Ana: What topic would you like us to talk about?\n"<<endl;

            geliTopics:
                cout<<"TOPICS:"<<endl;
                cout<<"1.) Music."<<endl;
                cout<<"2.) Food."<<endl;
                cout<<"3.) Dreams.\n"<<endl;

                cout<<"[GELI] Please Select: ";
                cin>>topic;

            if (topic == 1) {
                cout<<"Ana: What kind of music do you like?"<<endl;
                cout<<"Geli: ";
                cin>>chat;

                if (chat == "Pop" || chat == "pop") {
                    cout<<"Ana: Nice, I love catchy songs too!"<<endl;
                }
                else if (chat == "Rock" || chat == "rock") {
                    cout<<"Ana: Whoa, headbanger!"<<endl;
                }
                else if (chat == "Classical" || chat == "classical") {
                    cout<<"Ana: Wow, classy taste."<<endl;
                }
                else {
                    cout<<"Ana: Oh, I didn't know that was a real thing."<<endl;
                }
            }
            if (topic == 2) {
                cout<<"Ana: What’s your favorite food?"<<endl;
                cout<<"Geli: ";
                cin>>chat;

                if (chat == "Pizza" || chat == "pizza") {
                    cout<<"Ana: Can’t go wrong with that."<<endl;
                }
                else if (chat == "Ice cream" || chat == "ice cream" || chat == "Chocolate" || chat == "chocolate") {
                    cout<<"Ana: Haha, sweet tooth!"<<endl;
                }
                else if (chat == "Vegetables" || chat == "vegetables" || chat == "fruits" || chat == "Fruits") {
                    cout<<"Ana: Ohh, healthy choice!"<<endl;
                }
                else {
                    cout<<"Ana: Very nice, I think?"<<endl;
                }
            }
            if (topic == 3) {
                cout<<"Ana: What do you want to be someday?"<<endl;
                cout<<"Geli: ";
                cin>>chat;

                if (chat == "Doctor" || chat == "doctor") {
                    cout<<"Aww, that’s so noble."<<endl;
                }
                else if (chat == "Teacher" || chat == "teacher") {
                    cout<<"Ana: Wow, that’s inspiring."<<endl;
                }
                else if (chat == "Rich" || chat == "rich") {
                    int money;
                    cout<<"Ana: Hahaha, who doesn’t want that?"<<endl;
                    cout<<"Ana: How much do you want to start with?"<<endl;
                    cout << "Geli: ";
                    cin >> money;
                    cout << "Ana: If you double that, you’d have " << (money * 2) << "!" << endl;
                }
                else {
                    cout<<"Ana: Awesome !!!"<<endl;
                }
            }
            else {
                cout<<"ERROR: Input."<<endl;
                return 0;
            }

            break;
        }
        default: {
            cout<<"ERROR: Input. Please try again."<<endl;
            goto selectmate;
        }
    }

    end:
        cout<<"Ana: Do you still wanna talk with me?"<<endl;
        cout<<chosen;
        cin>>yesno;

        if (yesno == "Yes" || yesno == "yes" && chosen == "Ben: ") {
            goto benTopics;
        }
        else if (yesno == "Yes" || yesno == "yes" && chosen == "Geli: ") {
            goto geliTopics;
        }
        else if (yesno == "No" || yesno == "no") {
            cout << "CHAT END."<<endl;
            cout << "\nThank you for choosing YeheeY Chat System! Have a great day."<<endl;
            return 0;
        }
        else {
            cout<<"ERROR: Input. Chat adjourned."<<endl;
            return 0;
        }

    return 0;
}