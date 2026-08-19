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
                print("Items added.")

                tmp = request[1].split(",")
                list.extend(tmp)
            case "swp":
                if not list:
                    print("CAN'T SWAP! List is empty.")
                else:
                    tmp = request[1].split(",")
                    num1 = list.index(tmp[0])
                    num2 = list.index(tmp[1])

                    list[num1], list[num2] = list[num2], list[num1]
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