class CustomerData:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchase_history = []
    
    def add_purchase(self, item, price):
        self.purchase_history.append((item, price))
    
    def display_purchases(self):
        for item, price in self.purchase_history:
            print(f"{item}: ${price}")