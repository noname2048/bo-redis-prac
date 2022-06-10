import time

# block / sync


def wash_clothes(basket):
    next_basket = []
    for clothes in basket:
        print(f"{time.strftime('%M:%S')} ... ▷wash {clothes}")
        time.sleep(3)
        print(f"{time.strftime('%M:%S')} ... ▶wash {clothes}")
        next_basket += [clothes]

    return next_basket


def hang_clothes(basket):
    next_basket = []
    for clothes in basket:
        print(f"{time.strftime('%M:%S')} ... ▷hang clothes {clothes}")
        time.sleep(3)
        print(f"{time.strftime('%M:%S')} ... ▶hang clothes {clothes}")
        next_basket += [clothes]

    return next_basket


def clean_myroom():
    print(f"{time.strftime('%M:%S')} ... ▷clean my room")
    time.sleep(20)
    print(f"{time.strftime('%M:%S')} ... ▶clean my room ")


def main():
    basket = ["socks", "pants", "t-shirts", "towels"]
    basket = wash_clothes(basket)
    drying_rack = hang_clothes(basket)
    clean_myroom()


main()
