class Product:
    def __init__(self):
        self.products = {}

    def add_product(self):
        print("----- Products Adder -----")
        Adds = int(input("How many products do you want to add? : "))
        for i in range(Adds):
            product_name = input("Enter product name: ")
            __product_price = int(input("Enter product price : "))
            __product_stock = int(input("Enter product stock : "))
            self.products[product_name] = (__product_price , __product_stock)

    def show_products(self):
        if not self.products:
            print("No products in sale.")
        else:
            print("----- Products Info -----")
            for product_name, product_info in self.products.items():
                __product_price, __product_stock = product_info
                print(f"Name: {product_name} | Price: {__product_price} | Stock: {__product_stock}")

    def restock_product(self):
        print("----- Products Restocker -----")
        product_name = input("Enter the name of the product to restock: ")
        if product_name in self.products:
            additional_stock = int(input("Enter the quantity to add: "))
            __product_price, __product_stock = self.products[product_name]
            self.products[product_name] = (__product_price, __product_stock + additional_stock)
            print(f"Stock updated. New stock for {product_name}: {__product_stock + additional_stock}")
        else:
            print("Product not found.")

    def reduce_stock_product(self):
        print("----- Products Stock Reducer -----")
        product_name = input("Enter the name of the product to reduce stock: ")
        if product_name in self.products:
            reduction_stock = int(input("Enter the quantity to reduce: "))
            __product_price, __product_stock = self.products[product_name]
            if reduction_stock <= __product_stock:
                self.products[product_name] = (__product_price, __product_stock - reduction_stock)
                print(f"Stock updated. New stock for {product_name}: {__product_stock - reduction_stock}")
            else:
                print("Error: Not enough stock to reduce.")
        else:
            print("Product not found.")

    def update_product_price(self):
        print("----- Products Price Updater -----")
        product_name = input("Enter the name of the product to update price: ")
        if product_name in self.products:
            new_price = int(input("Enter the new price: "))
            __product_price, __product_stock = self.products[product_name]
            self.products[product_name] = (new_price, __product_stock)
            print(f"Price updated. New price for {product_name}: {new_price}")
        else:
            print("Product not found.")

my_product = Product()

my_product.add_product()
my_product.show_products()
my_product.restock_product()
my_product.show_products()
my_product.reduce_stock_product()
my_product.show_products()
my_product.update_product_price()
my_product.show_products()