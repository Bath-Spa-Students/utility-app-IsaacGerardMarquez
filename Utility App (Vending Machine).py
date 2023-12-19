
# Define class named IsaacMarquezVendingMachine that is representing a vending machine.
class IsaacMarquezVendingMachine:
    # The __init__ method is the constructor of the class. 
    # It is used to initialize the vending machine's categories, items, user's money, selected items, and selected item's name.
    def __init__(self):
         # Creating a Dictionary of categories with corresponding category codes.
        self.categories = {
            "1": "Snacks",
            "2": "Drinks",
            "3": "Chocolate",
            "4": "Water",
            "5": "Hot Drink",
            "6": "Bread",
        }
        # Creating a Dictionary of items with item codes and details (which includes the Name, Price, Stock, and Category).
        self.items = {
            # Snacks
            "SNACK1": {"Name": "Doritos", "Price": 7, "Stock": 8, "Category": "Snacks"},
            "SNACK2": {"Name": "Piatos", "Price": 5, "Stock": 9, "Category": "Snacks"},
            "SNACK3": {"Name": "Cheetos", "Price": 7, "Stock": 7, "Category": "Snacks"},
            "SNACK4": {"Name": "Takis", "Price": 6, "Stock": 4, "Category": "Snacks"},
            "SNACK5": {"Name": "Lays", "Price": 8, "Stock": 1, "Category": "Snacks"},

            # Drinks
            "DRINK1": {"Name": "Coca Cola", "Price": 3, "Stock": 3, "Category": "Drinks"},
            "DRINK2": {"Name": "Pepsi", "Price": 3, "Stock": 6, "Category": "Drinks"},
            "DRINK3": {"Name": "Sprite", "Price": 3, "Stock": 4, "Category": "Drinks"},
            "DRINK4": {"Name": "Mountain Dew", "Price": 3, "Stock": 3, "Category": "Drinks"},
            "DRINK5": {"Name": "Fanta", "Price": 3, "Stock": 1, "Category": "Drinks"},

            # Chocolates
            "CHOCO1": {"Name": "Toblerone", "Price": 5, "Stock": 6, "Category": "Chocolate"},
            "CHOCO2": {"Name": "Kit Kat", "Price": 3, "Stock": 5, "Category": "Chocolate"},
            "CHOCO3": {"Name": "Snickers", "Price": 3, "Stock": 7, "Category": "Chocolate"},
            "CHOCO4": {"Name": "Twix", "Price": 3, "Stock": 8, "Category": "Chocolate"},
            "CHOCO5": {"Name": "Maltesers", "Price": 4, "Stock": 6, "Category": "Chocolate"},

            # Water
            "WATER1": {"Name": "Mai Dubai", "Price": 1, "Stock": 4, "Category": "Water"},
            "WATER2": {"Name": "Al Ain", "Price": 1, "Stock": 8, "Category": "Water"},
            "WATER3": {"Name": "Zulal", "Price": 1, "Stock": 7, "Category": "Water"},
            "WATER4": {"Name": "Oasis", "Price": 1, "Stock": 9, "Category": "Water"},
            "WATER5": {"Name": "Arwa", "Price": 1, "Stock": 5, "Category": "Water"},

            # Hot Drinks
            "HOTDRINK1": {"Name": "Cappuccino", "Price": 5, "Stock": 5, "Category": "Hot Drink"},
            "HOTDRINK2": {"Name": "Espresso", "Price": 5, "Stock": 6, "Category": "Hot Drink"},
            "HOTDRINK3": {"Name": "Americano", "Price": 6, "Stock": 8, "Category": "Hot Drink"},
            "HOTDRINK4": {"Name": "Latte", "Price": 5, "Stock": 2, "Category": "Hot Drink"},
            "HOTDRINK5": {"Name": "Hot Chocolate", "Price": 5, "Stock": 3, "Category": "Hot Drink"},

            # Breads
            "BREAD1": {"Name": "Cheese Croissant", "Price": 5, "Stock": 5, "Category": "Bread"},
            "BREAD2": {"Name": "Butter Croissant", "Price": 5, "Stock": 5, "Category": "Bread"},
            "BREAD3": {"Name": "Bagels", "Price": 5, "Stock": 5, "Category": "Bread"},
            "BREAD4": {"Name": "Chocolate Muffin", "Price": 5, "Stock": 5, "Category": "Bread"},
            "BREAD5": {"Name": "Donut", "Price": 5, "Stock": 5, "Category": "Bread"},
        }
        # This variable is used to store the amount of money that the user has inserted into the vending machine. It is initialized to 0.
        self.user_money = 0
        # This list is used to store the items that the user has selected during a transaction. It is initialized as an empty list and items are added to it as the user makes selections.
        self.selected_items = []
        # This variable stores the name of the currently selected item during a transaction. It is initialized as an empty string and is updated based on the user's selections.
        self.selected_item_name = ""

# The display_categories method is used to display the available categories of items in the vending machine.
    def display_categories(self):
        # Using triple double quotation marks to print ASCII art for the vending machine categories.
        print("""
▒█░░▒█ ▒█▀▀▀ ▒█░░░ ▒█▀▀█ ▒█▀▀▀█ ▒█▀▄▀█ ▒█▀▀▀ 　 ▀▀█▀▀ ▒█▀▀▀█ 　 ▀█▀ ▒█▀▀▀█ ░█▀▀█ ░█▀▀█ ▒█▀▀█ █ ▒█▀▀▀█ 
▒█▒█▒█ ▒█▀▀▀ ▒█░░░ ▒█░░░ ▒█░░▒█ ▒█▒█▒█ ▒█▀▀▀ 　 ░▒█░░ ▒█░░▒█ 　 ▒█░ ░▀▀▀▄▄ ▒█▄▄█ ▒█▄▄█ ▒█░░░ ░ ░▀▀▀▄▄ 
▒█▄▀▄█ ▒█▄▄▄ ▒█▄▄█ ▒█▄▄█ ▒█▄▄▄█ ▒█░░▒█ ▒█▄▄▄ 　 ░▒█░░ ▒█▄▄▄█ 　 ▄█▄ ▒█▄▄▄█ ▒█░▒█ ▒█░▒█ ▒█▄▄█ ░ ▒█▄▄▄█ 

▒█░░▒█ ▒█▀▀▀ ▒█▄░▒█ ▒█▀▀▄ ▀█▀ ▒█▄░▒█ ▒█▀▀█ 　 ▒█▀▄▀█ ░█▀▀█ ▒█▀▀█ ▒█░▒█ ▀█▀ ▒█▄░▒█ ▒█▀▀▀ █ 
░▒█▒█░ ▒█▀▀▀ ▒█▒█▒█ ▒█░▒█ ▒█░ ▒█▒█▒█ ▒█░▄▄ 　 ▒█▒█▒█ ▒█▄▄█ ▒█░░░ ▒█▀▀█ ▒█░ ▒█▒█▒█ ▒█▀▀▀ ▀ 
░░▀▄▀░ ▒█▄▄▄ ▒█░░▀█ ▒█▄▄▀ ▄█▄ ▒█░░▀█ ▒█▄▄█ 　 ▒█░░▒█ ▒█░▒█ ▒█▄▄█ ▒█░▒█ ▄█▄ ▒█░░▀█ ▒█▄▄▄ ▄ 

▒█▀▀█ ▒█░░░ ▒█▀▀▀ ░█▀▀█ ▒█▀▀▀█ ▒█▀▀▀ 　 ▒█▀▀▀█ ▒█▀▀▀ ▒█░░░ ▒█▀▀▀ ▒█▀▀█ ▀▀█▀▀ 　 ░█▀▀█ 　 ▒█▀▀█ ░█▀▀█ ▀▀█▀▀ ▒█▀▀▀ ▒█▀▀█ ▒█▀▀▀█ ▒█▀▀█ ▒█░░▒█ ▄ 
▒█▄▄█ ▒█░░░ ▒█▀▀▀ ▒█▄▄█ ░▀▀▀▄▄ ▒█▀▀▀ 　 ░▀▀▀▄▄ ▒█▀▀▀ ▒█░░░ ▒█▀▀▀ ▒█░░░ ░▒█░░ 　 ▒█▄▄█ 　 ▒█░░░ ▒█▄▄█ ░▒█░░ ▒█▀▀▀ ▒█░▄▄ ▒█░░▒█ ▒█▄▄▀ ▒█▄▄▄█ ░ 
▒█░░░ ▒█▄▄█ ▒█▄▄▄ ▒█░▒█ ▒█▄▄▄█ ▒█▄▄▄ 　 ▒█▄▄▄█ ▒█▄▄▄ ▒█▄▄█ ▒█▄▄▄ ▒█▄▄█ ░▒█░░ 　 ▒█░▒█ 　 ▒█▄▄█ ▒█░▒█ ░▒█░░ ▒█▄▄▄ ▒█▄▄█ ▒█▄▄▄█ ▒█░▒█ ░░▒█░░ ▀""")
        print("")

        # Creating a for loop which loops through each category and print its corresponding number and name.
        for num, category in self.categories.items():
            print("""
┏━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┓
┗━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┛""")
            print(f"""｜{num}｜: {category}""")
            print("""┏━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┓
┗━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┛""")


# The select_category method is used to prompt the user to select a category by entering the corresponding number. 
# It then calls the display_items method to show the items available in the selected category.
    def select_category(self):
        while True:
            print("")
            # Prompts the user to select a category using ASCII art. Triple double quotation marks are used to print the ASCII art.
            category_choice = input("""

█▀▀ █▄░█ ▀█▀ █▀▀ █▀█   ▀█▀ █░█ █▀▀   █▄░█ █░█ █▀▄▀█ █▄▄ █▀▀ █▀█   █▀▀ █▀█ █▀█ █▀█ █▀▀ █▀ █▀█ █▀█ █▄░█ █▀▄ █ █▄░█ █▀▀   ▀█▀ █▀█
██▄ █░▀█ ░█░ ██▄ █▀▄   ░█░ █▀█ ██▄   █░▀█ █▄█ █░▀░█ █▄█ ██▄ █▀▄   █▄▄ █▄█ █▀▄ █▀▄ ██▄ ▄█ █▀▀ █▄█ █░▀█ █▄▀ █ █░▀█ █▄█   ░█░ █▄█

█▄█ █▀█ █░█ █▀█   █▀▄ █▀▀ █▀ █ █▀█ █▀▀ █▀▄   █▀▀ ▄▀█ ▀█▀ █▀▀ █▀▀ █▀█ █▀█ █▄█ ▀
░█░ █▄█ █▄█ █▀▄   █▄▀ ██▄ ▄█ █ █▀▄ ██▄ █▄▀   █▄▄ █▀█ ░█░ ██▄ █▄█ █▄█ █▀▄ ░█░ ▄  """)
            
            # Checks if the user's input corresponds to a valid category number.
            if category_choice in self.categories:
                # Used to get the name of the selected category.
                selected_category = self.categories[category_choice]
                # Calling the display_items method to display or show items in the selected category.
                self.display_items(selected_category)
                break
            else:
                # Printing a message informing the user of an invalid input and prompting them to input again.
                print("Invalid input. Please try again.")

# The display_items method takes a category as input and displays the available items in that category.
    def display_items(self, category):
        print("")
        # Displaying the header for the items table.
        print(f"Here are the available items in the {category} category:")
        print("")
        print("╭────────────╥──────────────────╥───────────╥─────────╮")
        print("| Code       ║ Name             ║ Price     ║ Stock   |")
        print("╠────────────╬──────────────────╬───────────╬─────────╣")

        # Iterate through each item using a for loop and print its details if it belongs to the specified category.
        for item_code, item in self.items.items():
            if item["Category"] == category:
                print(f"│ {item_code.ljust(10)} ║ {item['Name'].ljust(16)} ║ ${str(item['Price']).ljust(8)} ║ {str(item['Stock']).ljust(7)} │")
        print("╰────────────╨──────────────────╨───────────╨─────────╯")


# The select_item method is used to prompt the user to enter the code of the item they want to purchase. 
    def select_item(self):
        while True:
            print("")
            # Creating a user input that prompts the user to input or enter the code of their desired item.
            item_code = input("""
█▀▀ █▄░█ ▀█▀ █▀▀ █▀█   ▀█▀ █░█ █▀▀   █▀▀ █▀█ █▀▄ █▀▀   █▀█ █▀▀   ▀█▀ █░█ █▀▀   █ ▀█▀ █▀▀ █▀▄▀█   █▄█ █▀█ █░█
██▄ █░▀█ ░█░ ██▄ █▀▄   ░█░ █▀█ ██▄   █▄▄ █▄█ █▄▀ ██▄   █▄█ █▀░   ░█░ █▀█ ██▄   █ ░█░ ██▄ █░▀░█   ░█░ █▄█ █▄█

█░█░█ ▄▀█ █▄░█ ▀█▀   ▀█▀ █▀█   █▀█ █░█ █▀█ █▀▀ █░█ ▄▀█ █▀ █▀▀ ▀
▀▄▀▄▀ █▀█ █░▀█ ░█░   ░█░ █▄█   █▀▀ █▄█ █▀▄ █▄▄ █▀█ █▀█ ▄█ ██▄ ▄ """)
            print("")
            # Code that would determine or check if the entered item code exists in the vending machine's items.
            if item_code in self.items:
                selected_item = self.items[item_code]
                # Code that checks if the selected item is in stock.
                if selected_item["Stock"] > 0:
                    # Add the selected item to the list of items for the current transaction.
                    self.selected_items.append(selected_item)
                    # Stores the name of the selected item for reference.
                    self.selected_item_name = selected_item["Name"]
                    selected_item["Stock"] -= 1
                    break
                else:
                    # Printing a message that would inform the user if the selected item is out of stock and prompts them for another choice.
                    print("Unfortunately, the item you selected is out of stock. Please choose another.")
            else:
                # Printing a message that would Inform the user if the entered item code is invalid and prompt them for another choice.
                print("Invalid item code. Please try again.")

# The insert_money method is used to prompt the user to select a payment method and enter the amount of money they want to insert. It then validates the input and stores the user's money in the user_money variable.
    def insert_money(self):
        while True:
            # Printing or displaying ASCII art for a visual appeal, indicating payment options. Triple double quotation marks are used to print the ASCII art.
            print("""
▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄
░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░""")
            print("""
█▀ █▀▀ █░░ █▀▀ █▀▀ ▀█▀   ▄▀█   █▀█ ▄▀█ █▄█ █▀▄▀█ █▀▀ █▄░█ ▀█▀   █▀▄▀█ █▀▀ ▀█▀ █░█ █▀█ █▀▄ ▀
▄█ ██▄ █▄▄ ██▄ █▄▄ ░█░   █▀█   █▀▀ █▀█ ░█░ █░▀░█ ██▄ █░▀█ ░█░   █░▀░█ ██▄ ░█░ █▀█ █▄█ █▄▀ ▄  """)
            print("""

▄█░ ░ 　 ▒█▀▀█ ░█▀▀█ ▒█▀▀▀█ ▒█░▒█ 
░█░ ▄ 　 ▒█░░░ ▒█▄▄█ ░▀▀▀▄▄ ▒█▀▀█ 
▄█▄ █ 　 ▒█▄▄█ ▒█░▒█ ▒█▄▄▄█ ▒█░▒█""")
            print("""
█▀█ ░ 　 ▒█▀▀▄ ▒█▀▀▀ ▒█▀▀█ ▀█▀ ▀▀█▀▀ 　 ▒█▀▀█ ░█▀▀█ ▒█▀▀█ ▒█▀▀▄ 
░▄▀ ▄ 　 ▒█░▒█ ▒█▀▀▀ ▒█▀▀▄ ▒█░ ░▒█░░ 　 ▒█░░░ ▒█▄▄█ ▒█▄▄▀ ▒█░▒█ 
█▄▄ █ 　 ▒█▄▄▀ ▒█▄▄▄ ▒█▄▄█ ▄█▄ ░▒█░░ 　 ▒█▄▄█ ▒█░▒█ ▒█░▒█ ▒█▄▄▀""")
            print("""
█▀▀█ ░ 　 ▒█▀▀█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀▄ ▀█▀ ▀▀█▀▀ 　 ▒█▀▀█ ░█▀▀█ ▒█▀▀█ ▒█▀▀▄ 
░░▀▄ ▄ 　 ▒█░░░ ▒█▄▄▀ ▒█▀▀▀ ▒█░▒█ ▒█░ ░▒█░░ 　 ▒█░░░ ▒█▄▄█ ▒█▄▄▀ ▒█░▒█ 
█▄▄█ █ 　 ▒█▄▄█ ▒█░▒█ ▒█▄▄▄ ▒█▄▄▀ ▄█▄ ░▒█░░ 　 ▒█▄▄█ ▒█░▒█ ▒█░▒█ ▒█▄▄▀""")
            
            print("""
▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄
░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░""")

            # Creating an input function that prompts the user to choose a payment method using an ASCII art representation for visual appeal. Triple double quotation marks are used to print the ASCII art.
            payment_method_choice = input("""
█▀▀ █▄░█ ▀█▀ █▀▀ █▀█   ▀█▀ █░█ █▀▀   █▄░█ █░█ █▀▄▀█ █▄▄ █▀▀ █▀█   █▀▀ █▀█ █▀█ █▀█ █▀▀ █▀ █▀█ █▀█ █▄░█ █▀▄ █ █▄░█ █▀▀   ▀█▀ █▀█
██▄ █░▀█ ░█░ ██▄ █▀▄   ░█░ █▀█ ██▄   █░▀█ █▄█ █░▀░█ █▄█ ██▄ █▀▄   █▄▄ █▄█ █▀▄ █▀▄ ██▄ ▄█ █▀▀ █▄█ █░▀█ █▄▀ █ █░▀█ █▄█   ░█░ █▄█

█▄█ █▀█ █░█ █▀█   █▀▄ █▀▀ █▀ █ █▀█ █▀▀ █▀▄   █▀█ ▄▀█ █▄█ █▀▄▀█ █▀▀ █▄░█ ▀█▀   █▀▄▀█ █▀▀ ▀█▀ █░█ █▀█ █▀▄ ▀
░█░ █▄█ █▄█ █▀▄   █▄▀ ██▄ ▄█ █ █▀▄ ██▄ █▄▀   █▀▀ █▀█ ░█░ █░▀░█ ██▄ █░▀█ ░█░   █░▀░█ ██▄ ░█░ █▀█ █▄█ █▄▀ ▄  """)
            
            print("""
▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄
░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░""")

# The following code block allows the user to input the amount of cash they want to insert for payment.
# It includes input validation to ensure that the entered value is a positive numeric amount.
            
            if payment_method_choice == "1":  # Cash payment
                while True:
                    try:
                        # Create an input function that would prompt the user to enter the amount of cash. The float function is used to convert the user's input into a floating-point number.
                        self.user_money = float(input("""
█▀▀ █▄░█ ▀█▀ █▀▀ █▀█   ▀█▀ █░█ █▀▀   ▄▀█ █▀▄▀█ █▀█ █░█ █▄░█ ▀█▀   █▀█ █▀▀   █▀▀ ▄▀█ █▀ █░█   █▄█ █▀█ █░█   █░█░█ ▄▀█ █▄░█ ▀█▀
██▄ █░▀█ ░█░ ██▄ █▀▄   ░█░ █▀█ ██▄   █▀█ █░▀░█ █▄█ █▄█ █░▀█ ░█░   █▄█ █▀░   █▄▄ █▀█ ▄█ █▀█   ░█░ █▄█ █▄█   ▀▄▀▄▀ █▀█ █░▀█ ░█░

▀█▀ █▀█   █ █▄░█ █▀ █▀▀ █▀█ ▀█▀ ▀
░█░ █▄█   █ █░▀█ ▄█ ██▄ █▀▄ ░█░ ▄  """))
                        
                        if self.user_money > 0:
                            break
                        else:
                            print("Invalid amount. Please enter a positive value.")
# The except ValueError block captures cases where the entered value cannot be converted to a float, indicating a non-numeric input.
# In such cases, an error message is displayed, and the user is prompted to enter a valid amount.
                    except ValueError:
                        print("Invalid input. Please enter a valid amount.")
                break

# Checks if the user has chosen debit card payment.
            elif payment_method_choice == "2":  # Debit card payment
                while True: #  Create a loop that would ensure that the user gets a chance to input correct details.
                    try:
                        debit_card_number = input("Enter your debit card number: ") # User input to collect the user's Debit Card Number.
                        pin_code = input("Enter your debit card PIN code: ") # User input to collect the user's Debit Card PIN Code.

                        # Takes and converts the user's input for the amount they want to spend using the debit card.
                        self.user_money = float(input("""
█▀▀ █▄░█ ▀█▀ █▀▀ █▀█   ▀█▀ █░█ █▀▀   ▄▀█ █▀▄▀█ █▀█ █░█ █▄░█ ▀█▀   █▄█ █▀█ █░█   █░█░█ ▄▀█ █▄░█ ▀█▀   ▀█▀ █▀█   █░█ █▀ █▀▀ ▀
██▄ █░▀█ ░█░ ██▄ █▀▄   ░█░ █▀█ ██▄   █▀█ █░▀░█ █▄█ █▄█ █░▀█ ░█░   ░█░ █▄█ █▄█   ▀▄▀▄▀ █▀█ █░▀█ ░█░   ░█░ █▄█   █▄█ ▄█ ██▄ ▄  """)) 
                        # If all input is valid and the entered amount is positive, the break statement exits the loop.
                        if self.user_money > 0: # Determines if the entered amount is positive.
                            break
                        else:
                            print("Invalid amount. Please enter a positive value.")
                    except ValueError: # If the user enters invalid data (e.g., non-numeric values for the amount), it catches the ValueError and asks the user to enter a valid amount.
                        print("Invalid input. Please enter a valid amount.")
                break

            elif payment_method_choice == "3":  # Credit card payment
                while True: # Creating a while loop to ensure the user gets a chance to input correct details.
                    try:
                        credit_card_number = input("Enter your Credit Card number: ") # User input to collect the user's Credit Card Number.
                        pin_code = input("Enter your Credit Card PIN code: ") # User input to collect the user's Credit Card PIN Code.

                        # Takes and converts the user's input for the amount they want to spend using the credit card.
                        self.user_money = float(input("""
█▀▀ █▄░█ ▀█▀ █▀▀ █▀█   ▀█▀ █░█ █▀▀   ▄▀█ █▀▄▀█ █▀█ █░█ █▄░█ ▀█▀   █▄█ █▀█ █░█   █░█░█ ▄▀█ █▄░█ ▀█▀   ▀█▀ █▀█   █░█ █▀ █▀▀ ▀
██▄ █░▀█ ░█░ ██▄ █▀▄   ░█░ █▀█ ██▄   █▀█ █░▀░█ █▄█ █▄█ █░▀█ ░█░   ░█░ █▄█ █▄█   ▀▄▀▄▀ █▀█ █░▀█ ░█░   ░█░ █▄█   █▄█ ▄█ ██▄ ▄ """))
                        # If all input is valid and the entered amount is positive, the break statement exits the loop.
                        if self.user_money > 0:
                            break
                        else:
                            print("Invalid amount. Please enter a positive value.")
                    except ValueError: # If the user enters invalid data (e.g., non-numeric values for the amount), it catches the ValueError and asks the user to enter a valid amount.
                        print("Invalid input. Please enter a valid amount.")
                break

            else:
                print("Invalid input. Please enter a valid payment method.")

            print("""
▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄
░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░""")

# The calculate_change method is used to calculate the change to be given to the user based on the selected items' total price and the user's inserted money.
    def calculate_change(self):
        # Calculate the total price of all selected items using a list comprehension.
        total_price = sum(item["Price"] for item in self.selected_items)

        # Calculate the change by subtracting the total price from the user's inserted money.
        change = self.user_money - total_price

        # Round the change to two decimal places to handle potential floating-point precision issues.
        return round(change, 2)

# The display_receipt method is used to display a receipt with the selected items, total price, amount paid by the user, and the change.
    print ("")
    def display_receipt(self, change):
        print("""
▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄   █▀█ █▀▀ █▀▀ █▀▀ █ █▀█ ▀█▀   ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄
░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░   █▀▄ ██▄ █▄▄ ██▄ █ █▀▀ ░█░   ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░""")
        # Prints or displays information for each selected item.
        for item in self.selected_items:
            print("")
            print(f"|Item: {item['Name']}\n|Price: $ {item['Price']}")
        print("---------------------------")
        print(f"""|Total: $ {sum(item['Price'] for item in self.selected_items)}""") # Displays the total price of the item, amount paid by the user, and change that the user would receive.
        print(f"|Paid: $ {self.user_money}")
        print(f"|Change: $ {change}")
        print("""---------------------------""")

        print("""
▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄
░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░""")

# The perform_transaction method is used to handle the overall transaction process. 
# It calls the other methods in a loop to allow the user to select categories, items, insert money, and complete the transaction. 
# It also handles cases of insufficient funds and provides options to insert more money or cancel the transaction. 
# After each transaction, it asks the user if they want to buy again.
    def perform_transaction(self):
        while True:
            # Display categories, select category, select item, insert money, and calculate change.
            self.display_categories()
            self.select_category()
            self.select_item()
            self.insert_money()
            change = self.calculate_change()

            if change >= 0:
                # Display a receipt and ask the user to confirm the transaction
                self.display_receipt(change)
                confirm = input("""
█▀▀ █▀█ █▄░█ █▀▀ █ █▀█ █▀▄▀█   ▀█▀ █▀█ ▄▀█ █▄░█ █▀ ▄▀█ █▀▀ ▀█▀ █ █▀█ █▄░█ ▀   █▀▀ █▄░█ ▀█▀ █▀▀ █▀█   ▄▀ █▄█ █▀▀ █▀ ▀▄
█▄▄ █▄█ █░▀█ █▀░ █ █▀▄ █░▀░█   ░█░ █▀▄ █▀█ █░▀█ ▄█ █▀█ █▄▄ ░█░ █ █▄█ █░▀█ ▄   ██▄ █░▀█ ░█░ ██▄ █▀▄   ▀▄ ░█░ ██▄ ▄█ ▄▀

▀█▀ █▀█   █▀█ █▀█ █▀█ █▀▀ █▀▀ █▀▀ █▀▄   █▀█ █▀█   ▄▀ █▄░█ █▀█ ▀▄   ▀█▀ █▀█   █▀▀ ▄▀█ █▄░█ █▀▀ █▀▀ █░░
░█░ █▄█   █▀▀ █▀▄ █▄█ █▄▄ ██▄ ██▄ █▄▀   █▄█ █▀▄   ▀▄ █░▀█ █▄█ ▄▀   ░█░ █▄█   █▄▄ █▀█ █░▀█ █▄▄ ██▄ █▄▄

▀█▀ █▀█ ▄▀█ █▄░█ █▀ ▄▀█ █▀▀ ▀█▀ █ █▀█ █▄░█ ▀
░█░ █▀▄ █▀█ █░▀█ ▄█ █▀█ █▄▄ ░█░ █ █▄█ █░▀█ ▄ """)

                if confirm.lower() == "yes":
                    if self.selected_items:
                        print("")
                        print("Transaction completed. Enjoy your items!") # Printing a message displaying that the transaction completed successfully.
                        print("Dispensing", self.selected_item_name)  # Display the specific item being dispensed
                        
                        # Suggest a pairing for the selected item.
                        self.suggest_item(self.selected_item_name)

                        # Reset selected items after completing the transaction.
                        self.selected_items = []
                        self.selected_item_name = ""
                    else:
                        print("No items selected. Transaction canceled.")
                else:
                    print("Transaction canceled. Please take your money.")
                    # Refunds the user by adding back the item to the stock.
                    if self.selected_items:
                        selected_item = self.selected_items[0]  # Assuming only one item is selected.
                        selected_item["Stock"] += 1
                        self.selected_items = []
                        self.selected_item_name = ""
            else:
                print("Insufficient funds. Your current balance is not enough to complete the transaction.")

                # Code that handles cases of insufficient funds.
                while True:
                    choice = input("ENTER (1) TO INSERT MORE MONEY OR (2) TO CANCEL THE TRANSACTION: ")
                    if choice == "1": # User chooses to insert more money.
                        self.insert_money()  # Prompts the user to insert more money.
                        change = self.calculate_change()
                        if change >= 0: # Checks if the updated balance is now sufficient.

                            # Code to display a receipt and ask for confirmation again.
                            self.display_receipt(change)
                            confirm = input("""
█▀▀ █▀█ █▄░█ █▀▀ █ █▀█ █▀▄▀█   ▀█▀ █▀█ ▄▀█ █▄░█ █▀ ▄▀█ █▀▀ ▀█▀ █ █▀█ █▄░█ ▀   █▀▀ █▄░█ ▀█▀ █▀▀ █▀█   ▄▀ █▄█ █▀▀ █▀ ▀▄
█▄▄ █▄█ █░▀█ █▀░ █ █▀▄ █░▀░█   ░█░ █▀▄ █▀█ █░▀█ ▄█ █▀█ █▄▄ ░█░ █ █▄█ █░▀█ ▄   ██▄ █░▀█ ░█░ ██▄ █▀▄   ▀▄ ░█░ ██▄ ▄█ ▄▀

▀█▀ █▀█   █▀█ █▀█ █▀█ █▀▀ █▀▀ █▀▀ █▀▄   █▀█ █▀█   ▄▀ █▄░█ █▀█ ▀▄   ▀█▀ █▀█   █▀▀ ▄▀█ █▄░█ █▀▀ █▀▀ █░░
░█░ █▄█   █▀▀ █▀▄ █▄█ █▄▄ ██▄ ██▄ █▄▀   █▄█ █▀▄   ▀▄ █░▀█ █▄█ ▄▀   ░█░ █▄█   █▄▄ █▀█ █░▀█ █▄▄ ██▄ █▄▄

▀█▀ █▀█ ▄▀█ █▄░█ █▀ ▄▀█ █▀▀ ▀█▀ █ █▀█ █▄░█ ▀
░█░ █▀▄ █▀█ █░▀█ ▄█ █▀█ █▄▄ ░█░ █ █▄█ █░▀█ ▄ """)
                            
                            if confirm.lower() == "yes":
                                if self.selected_items:
                                    print("")
                                    print("Transaction completed. Enjoy your items!") # Printing a message displaying that the transaction completed successfully.
                                    print("Dispensing", self.selected_item_name, "...")  # Display the specific item being dispensed

                                    # Suggest a pairing for the selected item.
                                    self.suggest_item(self.selected_item_name)

                                    # Reset selected items after completing the transaction.
                                    self.selected_items = []
                                    self.selected_item_name = ""
                                else:
                                    print("No items selected. Transaction canceled.")
                                break
                            else:
                                print("Transaction canceled. Please take your money.")
                                # Refunds the user by adding back the item to the stock.
                                if self.selected_items:
                                    selected_item = self.selected_items[0]  # Assuming only one item is selected.
                                    selected_item["Stock"] += 1
                                self.selected_items = []
                                self.selected_item_name = ""
                                break
                        else:
                            print("Insufficient funds. Your current balance is still not enough to complete the transaction.")
                    elif choice == "2": # User chooses to cancel the transaction.
                        print("Transaction canceled. Please take your money.")
                        if self.selected_items:
                            selected_item = self.selected_items[0]  # Assuming only one item is selected
                            selected_item["Stock"] += 1
                        self.selected_items = []
                        self.selected_item_name = ""
                        break
                    else: # Printing a message saying invalid choice entered. Enter (1) or (2).
                        print("Invalid choice. Please enter (1) or (2).")

            print("""
▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄
░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░""")

            # Call suggest_item method here to provide recommendations.
            self.suggest_item(self.selected_item_name)
            
            # Initializes the variable for user input on whether to buy again or not.
            buy_again = ""
            while buy_again.lower() != "yes" and buy_again.lower() != "no": # Creating a while loop to ensure valid input for buying again (either "yes" or "no").
                buy_again = input("""
█▀▄ █▀█   █▄█ █▀█ █░█   █░█░█ ▄▀█ █▄░█ ▀█▀   ▀█▀ █▀█   █▀▄▀█ ▄▀█ █▄▀ █▀▀   ▄▀█   █▀█ █░█ █▀█ █▀▀ █░█ ▄▀█ █▀ █▀▀
█▄▀ █▄█   ░█░ █▄█ █▄█   ▀▄▀▄▀ █▀█ █░▀█ ░█░   ░█░ █▄█   █░▀░█ █▀█ █░█ ██▄   █▀█   █▀▀ █▄█ █▀▄ █▄▄ █▀█ █▀█ ▄█ ██▄

▄▀█ █▀▀ ▄▀█ █ █▄░█ ▀█   █▀█ █░░ █▀▀ ▄▀█ █▀ █▀▀   █▀▀ █▄░█ ▀█▀ █▀▀ █▀█   ▄▀ █▄█ █▀▀ █▀ ░░▄▀ █▄░█ █▀█ ▀▄ ▀
█▀█ █▄█ █▀█ █ █░▀█ ░▄   █▀▀ █▄▄ ██▄ █▀█ ▄█ ██▄   ██▄ █░▀█ ░█░ ██▄ █▀▄   ▀▄ ░█░ ██▄ ▄█ ▄▀░░ █░▀█ █▄█ ▄▀ ▄ """)
                
            if buy_again.lower() != "yes": # Determines if the user choses not to buy again and exit the loop.
                break

# Code that enables recommendations after each succesful transaction.
            if self.selected_item_name:
                # Call the suggest_item method to provide recommendations based on the selected item.
                self.suggest_item(self.selected_item_name)
        
    # Method to provide recommendations for paired items.    
    def suggest_item(self, item_name):
        # Creating a dictionary containing item pairs for recommendations.
        suggestions = {
            "Doritos": "Coca Cola",
            "Piatos ": "Sprite",
            "Cheetos": "Pepsi",
            "Takis": "Mountain Dew",
            "Lays": "Fanta",
            "Coca Cola": "Doritos",
            "Sprite": "Piatos ",
            "Pepsi": "Cheetos",
            "Mountain Dew": "Takis",
            "Fanta": "Lays",

            "Toblerone": "Cappuccino",
            "Kit Kat": "Cappuccino",
            "Snickers": "Cappuccino",
            "Twix": "Cappuccino",
            "Maltesers": "Cappuccino",

            "Mai Dubai": "Cheese Croissant",
            "Al Ain": "Butter Croissant",
            "Zulal": "Cheese Croissant",
            "Oasis": "Butter Croissant",
            "Arwa": "Donut",

            "Donut": "Hot Chocolate",
            "Chocolate Muffin": "Latte",
            "Bagels": "Cappuccino",
            "Cheese Croissant": "Americano",
            "Butter Croissant": "Espresso",
            "Hot Chocolate": "Donut",
            "Latte": "Chocolate Muffin",
            "Cappuccino": "Bagels",
            "Americano": "Cheese Croissant",
            "Espresso": "Butter Croissant",
        }

        # Checks if the selected item has a recommendation.
        if item_name in suggestions:
            # Retrieves the pairing suggestion and displays the recommendation.
            suggestion = suggestions[item_name]
            print(f"We recommend pairing your {item_name} with {suggestion}. Enjoy!")

# Creating an instance of the vending machine to start the transaction process.
vending_machine = IsaacMarquezVendingMachine()
vending_machine.perform_transaction()

print("""
▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄
░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░""")

# Displaying a message thanking the user for using the vending the machine. It uses triple double quotation marks to print ASCII art.
print("""
▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█   █▀▀ █▀█ █▀█   █░█ █▀ █ █▄░█ █▀▀   █ █▀ ▄▀█ ▄▀█ █▀▀ ▀ █▀
░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█   █▀░ █▄█ █▀▄   █▄█ ▄█ █ █░▀█ █▄█   █ ▄█ █▀█ █▀█ █▄▄ ░ ▄█

█░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀   █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀ █
▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█   █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄ ▄""")

print("""
▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄
░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░""")