def tax( price, rate ):
    return price + tax_amount( price, rate )

def tax_amount( price, rate ):
    return price * rate