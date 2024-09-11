class Order:
    all_orders = []  # Class variable to keep track of all orders

    def __init__(self, customer, coffee, price):
        # Validation for customer, coffee, and price
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be an instance of Customer")
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be an instance of Coffee")
        if not isinstance(price, (float, int)) or not 1.0 <= price <= 10.0:
            raise ValueError("Price must be a number between 1.0 and 10.0")
        
        self._customer = customer
        self._coffee = coffee
        self._price = float(price)
        Order.all_orders.append(self)

    # Getter for customer
    def get_customer(self):
        """Returns the customer associated with this order."""
        return self._customer

    # Getter for coffee
    def get_coffee(self):
        """Returns the coffee associated with this order."""
        return self._coffee

    # Getter for price
    def get_price(self):
        """Returns the price of this order."""
        return self._price

