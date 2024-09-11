class Coffee:
    def __init__(self, name):
        # Validation for coffee name
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Name must be a string with at least 3 characters.")
    
    # Getter for coffee name
    def get_name(self):
        """Returns the coffee's name."""
        return self._name

    # Returns a list of all orders for this coffee
    def orders(self):
        """Returns a list of all orders for this coffee."""
        return [order for order in Order.all_orders if order.coffee == self]

    # Returns a unique list of customers who ordered this coffee
    def customers(self):
        """Returns a unique list of all customers who have ordered this coffee."""
        return list({order.customer for order in self.orders()})

    # Returns the number of times this coffee has been ordered
    def num_orders(self):
        """Returns the total number of times the coffee has been ordered."""
        return len(self.orders())

    # Returns the average price of orders for this coffee
    def average_price(self):
        """Returns the average price of the coffee based on orders."""
        orders = self.orders()
        if orders:
            return sum(order.price for order in orders) / len(orders)
        return 0

