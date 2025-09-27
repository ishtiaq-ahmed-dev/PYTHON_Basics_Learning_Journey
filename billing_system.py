def print_menu():
    """
    Print the list of available items and prompt for correct spelling.
    """
    print('''We have:
  - eggs
  - biscuit
  - book
  - iphone
  - macbook

Please enter the correct spelling of the items.
''')
      
def get_item_name():
    """
    Prompt the user to enter an item name.
    Returns:
        str: the entered item name (lowercased)
    """
    name = input("Enter item name: ").strip().lower()
    return name


def get_quantity():
    """
    Prompt the user to enter a quantity.
    Returns:
        int: the entered quantity (must be nonnegative)
    """
    while True:
        try:
            quantity = int(input("Enter quantity: ").strip())
            if quantity < 0:
                print("Quantity cannot be negative. Try again.")
                continue
            return quantity
        except ValueError:
            print("Invalid input. Please enter a valid integer for quantity.")

def compute_price(name, quantity):
    """
    Compute total price (before discount) for a given item and quantity.
    Args:
        name (str): name of the item (lowercase)
        quantity (int): number of units
    Returns:
        int or float: total price, or None if item name is invalid
    """
    # Price dictionary for quick lookup
    price_map = {
        "eggs": 20,
        "biscuit": 50,
        "book": 200,
        "iphone": 50000,
        "macbook": 100000
    }
    unit_price = price_map.get(name)
    if unit_price is None:
        # invalid item
        return None
    return unit_price * quantity

def determine_discount_percent(amount):
    """
    Determine the discount percentage based on the amount value.
    Args:
        amount (float): amount before discount
    Returns:
        float: discount percentage (0 if no discount)
    """
    if amount <= 50:
        return 0.0
    elif amount <= 100:
        return 5.0
    elif amount <= 200:
        return 10.0
    elif amount <= 500:
        return 15.0
    else:  # amount > 500
        return 20.0

def compute_discounted_amount(amount, discount_percent):
    """
    Compute how much money is discounted.
    Args:
        amount (float): original amount
        discount_percent (float): discount in percent
    Returns:
        float: discount amount (in currency)
    """
    return (amount * discount_percent) / 100.0

def apply_discount(amount, discount_amt):
    """
    Subtract discount from the original amount.
    Args:
        amount (float): original price
        discount_amt (float): discount in currency
    Returns:
        float: amount after discount
    """
    return amount - discount_amt

def compute_tax(amount_after_discount):
    """
    Compute sales tax on the discounted amount.
    Args:
        amount_after_discount (float): amount after discount
    Returns:
        float: tax amount
    """
    TAX_RATE = 0.085  # 8.5% tax
    return amount_after_discount * TAX_RATE


def compute_total(amount_after_discount, tax_amount):
    """
    Compute final total to pay (after discount + tax).
    Args:
        amount_after_discount (float): discounted amount
        tax_amount (float): tax
    Returns:
        float: total payable
    """
    return amount_after_discount + tax_amount

def main():
    # Print menu / items
    print_menu()

    # Get user input
    name = get_item_name()
    quantity = get_quantity()

    # Compute price
    price = compute_price(name, quantity)
    if price is None:
        print(f"Error: '{name}' is not a valid item.")
        return

    # Compute discount
    discount_pct = determine_discount_percent(price)
    discount_amt = compute_discounted_amount(price, discount_pct)
    after_discount_amt = apply_discount(price, discount_amt)

    # Compute tax and total
    tax_amt = compute_tax(after_discount_amt)
    total_to_pay = compute_total(after_discount_amt, tax_amt)

    # Print results nicely formatted
    print("\n===== Invoice / Summary =====")
    print(f"Item: {name}")
    print(f"Quantity: {quantity}")
    print(f"Item Price (before discount): {price:.2f}")
    print(f"Discount Rate: {discount_pct:.1f}%")
    print(f"Discount Amount: {discount_amt:.2f}")
    print(f"Amount After Discount: {after_discount_amt:.2f}")
    print(f"Sales Tax (8.5%): {tax_amt:.2f}")
    print(f"Total Amount to Pay: {total_to_pay:.2f}")
    print("=============================")


if __name__ == "__main__":
    main()
