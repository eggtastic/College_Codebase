print("-- STUDENT INFORMATION --")

menu = ["Add Product", "Display Product", "Edit Product","Exit"]
display_menu = ["Display All", "Search Product"]
edit_menu = ["Update Product", "Remove Product"]
edit_options = ["Update Price", "Update Stock"]

product = {}

def show_menu():
    for i in range(len(menu)):
        print((i+1), "-", menu[i])
def show_display():
    for i in range(len(display_menu)):
        print((i+1), "-", display_menu[i])
def show_edit():
    for i in range(len(edit_menu)):
        print((i+1), "-", edit_menu[i])
def show_edit_options():
    for i in range(len(edit_options)):
        print((i+1), "-", edit_options[i])
def show_products():
    if not product:
        print("No data exists... yet?")
    else:
        for key, value in product.items():
            print(key)
            for sub_key, sub_value in value.items():
                print(f"{sub_key}: {sub_value}")
    print()

while (True):
    show_menu()
    choice = int(input("Enter choice: "))
    match choice:
            case 1:
                print("\nADDING...")
                add_name = input("Enter Product Name: ").lower()

                while True:
                    add_price = int(input("Enter Price: "))
                    if add_price > 0:
                        break
                    else:
                        print("Price must be higher than 0.")

                while True:
                    add_stock = int(input("Enter Stock: "))
                    if add_stock >= 0:
                        break
                    else:
                        print("Stock cannot be negative.")


                product.update({
                    add_name: {
                        "price": add_price,
                        "stock": add_stock
                    }
                })

            case 2:
                print("\nDISPLAYING...")
                show_display()

                while True:
                    choice_display = int(input("Please enter choice: "))
                    if (choice_display > 0 and choice_display < 3):
                        break
                    else:
                        print("Choice INVALID! Please choose again.")
                        continue

                match choice_display:
                    case 1:
                        print("\n--- DISPLAY PRODUCTS ---")

                        show_products()
                    case 2:
                        if len(product) == 0:
                            print("Sorry, product list is empty.")
                        else:
                            search_name = input("Enter product name to search: ")

                            search_updated = search_name.lower()

                            if search_updated in product:
                                print(f"\n{search_updated}")
                                for sub_key, sub_value in product[search_updated].items():
                                    print(f"{sub_key}: {sub_value}")
                            else:
                                print("Product not found.")
            case 3:
                print("\nEDITING...")

                if not product:
                    print("No products available.")
                else:
                    search = input("Please enter the product you are looking for: ").lower()

                    if search in product:
                        updated = search

                        show_edit()

                        while True:
                            choice_edit = int(input("Please enter your choice: "))
                            if 1 <= choice_display <= 2:
                                break
                            else:
                                print("Invalid Option.")

                        match choice_edit:
                            case 1:
                                show_edit_options()

                                while True:
                                    edit_option = int(input("Please enter your choice: "))
                                    if (edit_option > 0 and edit_option < 3):
                                        break
                                    else:
                                        print("Invalid Option.")

                                match edit_option:
                                    case 1:
                                        new_price = int(input("Enter new price: "))
                                        product[updated]["price"] = new_price
                                        print("Price updated successfully.")

                                    case 2:
                                        new_stock = int(input("Enter new stock: "))
                                        product[updated]["stock"] = new_stock
                                        print("Stock updated successfully.")

                            case 2:
                                del product[updated]
                                print("Product removed successfully.")

                    else:
                        print("Product not found.")
            case 4:
                print("\nEXITING...")
                print("Program ended.")
                break

    print()
