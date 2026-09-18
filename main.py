from products import Product
from store import Store


# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250)
            ]
best_buy = Store(product_list)

def buy():
    """ Menu to create a new order"""
    VOID_STR = ""
    isBuying = True
    order = []
    products_list = best_buy.get_all_products()

    best_buy.show_all_products()
    print( "When you want to finish order, enter empty text.")

    # user input order items
    while isBuying == True:
        product_input = input("Which product # do you want? ") 

        if product_input.strip() == VOID_STR:
            break    

        if not product_input.isnumeric():
           print("Product ID must be a number.")
           continue

        product_input = int(product_input)
        if product_input > len(best_buy.products) or \
            product_input <= 0:
           print("Provide valid a product.")
           continue

        # waiting for user input a valid number   
        isValidNumber = False
        while not isValidNumber:
            quantity_input = input("What amount do you want? ")
            if not quantity_input.isnumeric(): 
                print("Quantity must be a number")
                continue
            
            quantity_input = int(quantity_input)
            if quantity_input <= 0:
                print("Provide a quantity higher than 0.")
                continue
            isValidNumber = True
            
        product_selected = products_list[product_input - 1]
        order.append((product_selected, quantity_input))

        print("Product added to list!")
        print("")

    if len(order) == 0:
        print("Order cancelled by the user.")
        return
    try:
        total = best_buy.order(order)
        print(f'Order made! Total payment: ${total}')
    except (TypeError, ValueError) as e:
        print("Error while making order!", e)
    except:
        print("Error while making order! Please try again.")

if __name__ == "__main__":

    open = True

    while open:

        print("     Store Menu")
        print("     ----------")

        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        option = input("Please choose a number: ")

        match option:
            case "1":
                best_buy.show_all_product()
            case "2":
                total = best_buy.get_total_quantity()
                print(f'Total of {total} items in store')
            case "3":
                buy()
            case "4":
                open = False
            case _:
                print("Invalid operation.")
