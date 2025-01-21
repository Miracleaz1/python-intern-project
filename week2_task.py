def add_to_cart(item_name, price, *args, **kwargs):
    # Calculate final price after applying discounts
    final_price = price
    for discount in args:
        final_price -= final_price * (discount / 100)
    
    # Store item details
    item_details = kwargs
    item_details['final_price'] = final_price
    
    return item_details

def main():
    cart = {}
    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        
        if item_name in cart:
            print(f"{item_name} is already in the cart. Skipping duplicate.")
            continue
        
        try:
            price = float(input("Enter item price: "))
        except ValueError:
            print("Invalid price. Please enter a numeric value.")
            continue
        
        discounts = input("Enter discounts (if any, separated by spaces): ")
        try:
            discounts = [float(d) for d in discounts.split()] if discounts else []
        except ValueError:
            print("Invalid discount format. Please enter numeric values separated by spaces.")
            continue
        
        details = {}
        while True:
            detail = input("Enter item detail (key=value) or 'done' to finish: ")
            if detail.lower() == 'done':
                break
            if '=' not in detail:
                print("Invalid detail format. Please enter in key=value format.")
                continue
            key, value = detail.split('=', 1)
            details[key] = value
        
        item_details = add_to_cart(item_name, price, *discounts, **details)
        cart[item_name] = item_details
        print(f"Item added: {item_name} - Final Price: ${item_details['final_price']:.2f}")
    
    # Display cart summary
    print("\n--- Cart Summary ---")
    total_cost = 0
    for item, details in cart.items():
        final_price = details.pop('final_price')
        total_cost += final_price
        details_str = ', '.join(f"{key}={value}" for key, value in details.items())
        print(f"{item} - ${final_price:.2f} ({details_str})")
    print(f"Total Cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()