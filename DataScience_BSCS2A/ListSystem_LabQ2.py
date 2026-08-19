print("-- LIST SYSTEM --")

list = []

while (True):
    tmp = [] # elem temp storage
    choice = input("> ")
    request = choice.split()

    match request[0]:
            case "help":
                print("show")
                print("add <value1,value2,...")
                print("swp <value1>,<value2>")
                print("dup")
                print("help")
                print("exit")
            case "show":
                if not list:
                    print("List is empty.")
                else:
                    print(list)
            case "add":
                if len(request) < 2 or request[1] == "":
                    print("ERROR! Added elements cannot be empty.")
                else:
                    tmp = request[1].split(",")

                    if any(item == "" for item in tmp):
                        print("ERROR! Please input valid elements.")
                    else:
                        list.extend(tmp)
                        print("Items added.")

            case "swp":
                if not list:
                    print("CAN'T SWAP! List is empty.")
                else:
                    tmp = request[1].split(",")
                    # num1 = list.index(tmp[0])
                    # num2 = list.index(tmp[1])

                    # list[num1], list[num2] = list[num2], list[num1]
                    # the first method i tried

                    num1 = tmp[0]
                    num2 = tmp[1]

                    if not num1 in list or not num2 in list:
                         print("ERROR: NOT FOUND. Please find/add elements to swap.")
                    else:
                        for i in range(len(list)):
                            if list[i] == num1:
                                list[i] = num2
                            elif list[i] == num2:
                                list[i] = num1

                        print("Elements swapped!")
            case "dup":
                if not list:
                    print("List is empty. Please add to check for duplicates.")
                else:
                    deleted =[]
                    duplicates =[]

                    for x in list:
                        if x not in deleted:
                            deleted.append(x)
                        elif x in deleted and x not in duplicates:
                            duplicates.append(x)
                    if duplicates != []:
                        while True:
                            to_delete =input(f"Duplicates found: {duplicates} \n Do you wish to delete? [y/n]: ")
                            if to_delete.lower() == "y":
                                list=deleted
                                print("Duplicates removed.")
                                break
                            elif to_delete.lower() == "n":
                                print("Duplicates kept.")
                                break
                            else:
                                print("ERROR: Please enter only 'Y' or 'N'.")
                    else:
                        print("No duplicates found.")
            case "exit":
                break
            case _:
              print("ERROR: Input outside of choices. Type 'help' to show choices.")
              continue