def calculate_checkout(cart_total, shipping_speed):
    if shipping_speed == "express":
        shipping = 20
    elif shipping_speed == "overnight":
        shipping = 35
    elif shipping_speed == "standard" and cart_total >= 100:
        shipping = 0
    elif shipping_speed == "standard":
        shipping = 10
    else:
        print("Error: Invalid shipping speed!")
        shipping = 0
        
    final_bill = cart_total + shipping
    return final_bill

print(calculate_checkout(10000,"express"))
print(calculate_checkout(120, "express"))
