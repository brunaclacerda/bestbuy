class Product:

    @staticmethod
    def validate_arg_quantity(quantity):
        if type(quantity) is not int:
           raise TypeError("Invalid quantity!")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

    @staticmethod
    def validate_arg_price(price):
        if not isinstance(price, int) and not isinstance(price, float):
            raise TypeError("Price must be a number.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        

    def __init__(self, name : str, price : float, quantity : int):
        if not isinstance(name, str) :
             raise TypeError("Invalid name.")
        
        name = name.strip()

        if len(name) == 0:
            raise ValueError("Name must be provided.")
        

        Product.validate_arg_quantity(quantity)
        Product.validate_arg_price(price)
        
        self.name = name
        self.price = float(price)
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity : int):
        Product.validate_arg_quantity(quantity)
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def get_price(self) -> float:
        return self.price

    def set_price(self, price : float):
        Product.validate_arg_price(price)
        self.price = float(price)

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f'Product: {self.name}, Price: ${self.price}, Quantity: {self.quantity}')

    def buy(self, quantity) -> float:
        if not self.active:
            raise Exception("Operation invalid. Product is not active!")
        
        Product.validate_arg_quantity(quantity)
        if quantity == 0:
            raise ValueError("Quantity value should be higher than 0!")
        if quantity > self.quantity:
            raise ValueError("Quantity not available!")

        new_quantity = self.quantity - quantity
        self.set_quantity(new_quantity)

        total_price = self.price * quantity
        return total_price