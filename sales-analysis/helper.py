
def calculate_total(quantity, price):
    """Calculate total for a single item 
    this is just a helper function to calculate total for a single item based on quantity and price.
    """
    return quantity * price

def format_currency(amount):
    """Format number as currency"""
    return f"${amount:,.2f}"