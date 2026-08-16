def discount(price, grade):
    if grade == "VIP":
        return price * 0.8
    elif grade == "GOLD":
        return price * 0.9
    else:
        return price

