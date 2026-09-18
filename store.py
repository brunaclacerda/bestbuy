from products import Product 

class Store:

    def __init__(self, products : list[Product] = None):
        self.products = []
        if products is not None:
            for product in products:
                if not isinstance(product, Product):
                    raise TypeError("Invalid product.")
                
            self.products.extend(products)

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Product provided is invalid.")
        self.products.append(product)

    def remove_product(self, product : Product):
        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError("Product not found.")

    def get_total_quantity(self) -> int:
        total_quantity = 0
        for product in self.products:
            if product.is_active():
                total_quantity += product.get_quantity()

        return total_quantity

    def get_all_products(self) -> list[Product]:
        active_products = [product for product in self.products if product.is_active()]
        return active_products

    def validate_order_item(self, item_id, item):
        if not isinstance(item, tuple):
            raise TypeError(f'Item {item_id} is not a tuple')
        
        if len(item) != 2:
            raise ValueError("Item must be provided with only: product and quantity.")

        if not isinstance(item[0], Product):
            raise TypeError(f'Invalid product provided for item {item_id}.')
        
        if type(item[1]) is not int:
            raise TypeError(f'Invalid product provided for item {item_id}.')

        if int(item[1]) < 1:
            raise ValueError("Quantity value must be higher than 0.")

        if item[0] not in self.products or not item[0].is_active():
            raise ValueError(f'Product provided for item {item_id} is not available.')


    def create_order(self, shopping_list : list[tuple[Product, int]] ) -> list[list]:
        order_items = []
        products_ordered = []

        for item_id, item in enumerate(shopping_list, start=1):
            self.validate_order_item(item_id, item)

            product = item[0]
            order_qt = item[1]

            if product not in products_ordered:
                order_items.append([product, order_qt])
                products_ordered.append(product)
            else:  # add quantity in the existent order's item
               order_item_idx = products_ordered.index(product)
               order_items[order_item_idx][1] += order_qt
               order_qt = order_items[order_item_idx][1] 

            if product.get_quantity() < order_qt:
                raise ValueError(f'Item {item_id}: Quantity requested is not available.')

        return order_items
                
    def update_inventory(self, order: list[list]):
        
        for item in order:
            order_product = item[0]
            order_qt = item[1]
            order_product.buy(order_qt)

    @staticmethod
    def calculate_total_order(order : list[list]) -> float:
        total = 0.0

        for item in order:
            total += (item[0].price * item[1])

        return total

    def order(self, shopping_list : list[tuple[Product, int]]) -> float:
        if not isinstance(shopping_list, list):
            raise TypeError("No valid shopping list provided.")
        if len(shopping_list) == 0:
            raise ValueError("No items provided.")

        order = self.create_order(shopping_list)
        self.update_inventory(order)
        return Store.calculate_total_order(order)

    def show_all_products(self):
        products = self.get_all_products()
        if products:
            print("------")
            for i, product in enumerate(products, start=1):
                print(f'{i}. {product.name}, Price: ${product.get_price()}, Quantity: {product.get_quantity()}')
            print("------")
            print("")


            
            
            