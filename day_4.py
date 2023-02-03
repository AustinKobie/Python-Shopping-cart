class shopping_cart():
    def __init__(self):
        self.cart = []

    def add_item(self):
        name = input('What item would you like to add:')

        price = float(input('What is the price of the item:'))

        new_item = item(name, price)
        self.cart.append(new_item)

    def delete_item(self):
        delete_product = input('What item would you like to delete:')

        for i in range(len(self.cart)):
            if self.cart[i].name.lower() == delete_product.lower():
                self.cart.pop(i)
                print('Removed item')
                return
        print(f'{delete_product} was not found.')

    def print_cart(self):
        for cart in self.cart:
            print(f'{cart.name}: {cart.price}')

    def run(self):
        while True:
            user_choice = input(
                'What would you like to do? (add/delete/show/quit)').lower()

            if user_choice == 'add':
                self.add_item()
            elif user_choice == 'delete':
                self.delete_item()
            elif user_choice == 'show':
                self.print_cart()
            elif user_choice == 'quit':
                self.print_cart()
                return
            else:
                print('That was not valid input, please try again.')


class item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = shopping_cart()

cart.run()
