class Customer:
    def __init__(self, name):
        # Validation for name
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 15 characters")
    
    # Getter for name
    def get_name(self):
        """Returns the customer's name."""
        return self._name

    # Setter for name
    def set_name(self, name):
        """Sets the customer's name with validation."""
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 15 characters")

    # Returns a list of the customer's orders
    def orders(self):
        """Returns a list of orders for this customer."""
        return [order for order in Order.all_orders if order.customer == self]

    # Returns a list of coffees the customer has ordered
    def coffees(self):
        """Returns a unique list of coffees the customer has ordered."""
        return list({order.coffee for order in self.orders()})

    # Creates a new order for the customer
    def create_order(self, coffee, price):
        """Creates and returns a new order associated with the customer and coffee."""
        return Order(self, coffee, price)

    # Finds the customer who has spent the most on a specific coffee
    def most_aficionado(coffee):
        """Returns the customer who has spent the most on the specified coffee."""
        customer_spendings = {}
        for order in coffee.orders():
            customer_spendings[order.customer] = customer_spendings.get(order.customer, 0) + order.price

        if not customer_spendings:
            return None

        return max(customer_spendings, key=customer_spendings.get)

