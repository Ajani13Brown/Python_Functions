# Task 1: Write a function that lets the user add items to a list until the user replies "stop", and then returns the shopping list.
shopping_list =[]
def modify_list(shopping_list):
        shopping = True
        while shopping :
            add_item = input('Would you like to "add item" or "stop" ')
            if add_item == "add item":
                item = input("what would you like to add ")
                shopping_list.append(item)
            elif add_item == "stop":
                print(f"ok, well this is what you have so far {shopping_list}")
                break
            else:
                 print(f"Sorry but {add_item} isn't one of the options")



# Task 2: Include a feature to remove items from the list.              
       

shopping_list =[]
def modify_list(shopping_list):
        shopping = True
        while shopping :
            add_item = input('Would you like to "add", "remove" or "stop" ')
            if add_item == "add":
                item = input("what would you like to add ")
                shopping_list.append(item)
            elif add_item == "remove":
                    r_item = input("what item would you like to remove? ")
                    shopping_list.remove(r_item)
            elif add_item == "stop":
                print(f"ok, well this is what you have so far {shopping_list}")
                break
            else:
                 print(f"Sorry but {add_item} isn't one of the options")
modify_list(shopping_list)

# #Task 3: Add a feature that prints out the entire list in a formatted way.

shopping_list =[]
def modify_list(shopping_list):
        shopping = True
        while shopping :
            add_item = input('Would you like to "add", "remove", "show" or "stop" ')
            if add_item == "add":
                item = input("what would you like to add ")
                shopping_list.append(item)
            elif add_item == "remove":
                    r_item = input("what item would you like to remove? ")
                    shopping_list.remove(r_item)
            elif add_item == "show":
                  for item in shopping_list:
                        print(f"Item number {shopping_list.index(item)+1}.) : {item}")
            elif add_item == "stop":
                print(f"ok, well this is what you have so far {shopping_list}")
                break
            else:
                 print(f"Sorry but {add_item} isn't one of the options")
modify_list(shopping_list)