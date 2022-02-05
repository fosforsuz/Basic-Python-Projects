import requests


def cache(content):
    check_list.append(content)
    pass


def main():
    currency_code = input()  # main money code
    while True:
        target_code = input()
        if target_code == "":
            break
        count = int(input())
        if target_code == "usd" or target_code == "eur" or target_code in check_list:
            eur_usd_print()
        else:
            other_print()
        calculate(currency_code, target_code, count)
        cache(target_code)


def retrieve_data(content_name):
    url = f"http://www.floatrates.com/daily/{content_name}.json"
    return requests.get(url).json()


def eur_usd_print():
    print("""Checking the cache...
Oh! It is in the cache!""")


def other_print():
    print("""Checking the cache...
Sorry, but it is not in the cache!""")


def calculate(main_content, target_content, money):
    data = retrieve_data(main_content)
    price = f"You received {round(money * float(data[target_content]['rate']), 2)} {target_content.upper()}."
    print(price)


check_list = []
main()
